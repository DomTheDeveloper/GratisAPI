/**
 * GratisAPI — Dynamic API (Cloudflare Worker)
 *
 * The static API answers "give me this dataset". This Worker adds the dynamic
 * verbs on top of it — filter, search, sort, paginate, random — with no
 * database. It fetches the matching static collection from the edge cache and
 * applies the query in memory, so it stays cheap and shares the same data.
 *
 * Production hardening: edge response caching (Cache API), an upstream fetch
 * timeout, strict input validation (SSRF-safe), structured JSON errors,
 * security headers, and CORS. See README.md for routes and deploy steps.
 */

const VERSION = "1.1.0";
const RESERVED = new Set(["q", "sort", "order", "limit", "offset", "fields", "count"]);
const MAX_LIMIT = 1000;
const DEFAULT_LIMIT = 50;
const CACHE_TTL = 3600;          // seconds, edge + browser
const UPSTREAM_TIMEOUT_MS = 8000;
const MAX_Q_LEN = 200;
const MAX_FILTERS = 25;
const API_RE = /^[a-z0-9][a-z0-9-]{0,63}$/;   // dataset slugs only
const ID_RE = /^[A-Za-z0-9._-]{1,128}$/;

const OPS = {
  gt: (a, b) => cmp(a, b) > 0,
  gte: (a, b) => cmp(a, b) >= 0,
  lt: (a, b) => cmp(a, b) < 0,
  lte: (a, b) => cmp(a, b) <= 0,
  ne: (a, b) => String(a).toLowerCase() !== String(b).toLowerCase(),
  contains: (a, b) => String(a).toLowerCase().includes(String(b).toLowerCase()),
  eq: (a, b) => String(a).toLowerCase() === String(b).toLowerCase(),
};

function cmp(a, b) {
  const na = Number(a), nb = Number(b);
  if (!Number.isNaN(na) && !Number.isNaN(nb)) return na - nb;
  return String(a).localeCompare(String(b));
}

const BASE_HEADERS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "GET, OPTIONS",
  "Access-Control-Allow-Headers": "*",
  "X-Content-Type-Options": "nosniff",
  "Referrer-Policy": "no-referrer",
  "X-GratisAPI-Version": VERSION,
};

function json(obj, status = 200, extra = {}) {
  return new Response(JSON.stringify(obj, null, 2) + "\n", {
    status,
    headers: {
      "Content-Type": "application/json; charset=utf-8",
      "Cache-Control": `public, max-age=${CACHE_TTL}`,
      ...BASE_HEADERS,
      ...extra,
    },
  });
}
const err = (status, message, extra) => json({ error: message, status }, status, extra);

function help(base) {
  return json({
    name: "GratisAPI Dynamic API",
    version: VERSION,
    description: "Filter, search, sort, paginate and randomize any GratisAPI dataset — a thin compute layer over the free static API.",
    source: "https://github.com/DomTheDeveloper/GratisAPI",
    static_api: base,
    usage: {
      collection: "/:api?q=&<field>=&<field>__gt=&sort=&order=&fields=&limit=&offset=",
      random: "/:api/random?count=N",
      item: "/:api/:id",
      openapi: "/openapi.json",
      health: "/health",
    },
    operators: ["eq (default)", "gt", "gte", "lt", "lte", "ne", "contains"],
    examples: [
      "/quotes/random",
      "/animals?class=Mammalia&sort=common_name&limit=5",
      "/elements?category=Noble%20gas&fields=name,symbol,atomic_number",
      "/countries?population_millions__gt=100&sort=population_millions&order=desc",
      "/colors?q=blue&limit=10",
    ],
    catalog: base + "/api/index",
    license: "GPL-2.0-or-later",
  });
}

function openapi(base, host) {
  return json({
    openapi: "3.1.0",
    info: { title: "GratisAPI Dynamic API", version: VERSION, description: "Dynamic query layer over the free GratisAPI static data." },
    servers: [{ url: `https://${host}` }],
    paths: {
      "/{api}": {
        get: {
          summary: "Query a dataset",
          parameters: [
            { name: "api", in: "path", required: true, schema: { type: "string" }, description: "Dataset slug (see " + base + "/api/index)." },
            { name: "q", in: "query", schema: { type: "string" }, description: "Full-text search across all fields." },
            { name: "sort", in: "query", schema: { type: "string" } },
            { name: "order", in: "query", schema: { type: "string", enum: ["asc", "desc"] } },
            { name: "fields", in: "query", schema: { type: "string" }, description: "Comma-separated projection." },
            { name: "limit", in: "query", schema: { type: "integer", default: DEFAULT_LIMIT, maximum: MAX_LIMIT } },
            { name: "offset", in: "query", schema: { type: "integer", default: 0 } },
          ],
          responses: { "200": { description: "Matching records." }, "404": { description: "Unknown dataset." } },
        },
      },
      "/{api}/random": { get: { summary: "Random record(s)", parameters: [{ name: "api", in: "path", required: true, schema: { type: "string" } }, { name: "count", in: "query", schema: { type: "integer", default: 1, maximum: 100 } }], responses: { "200": { description: "Random record(s)." } } } },
      "/{api}/{id}": { get: { summary: "Single record", parameters: [{ name: "api", in: "path", required: true, schema: { type: "string" } }, { name: "id", in: "path", required: true, schema: { type: "string" } }], responses: { "200": { description: "The record." }, "404": { description: "Not found." } } } },
    },
  });
}

async function loadCollection(base, api) {
  const url = `${base}/api/${api}/index`;
  const ctrl = new AbortController();
  const timer = setTimeout(() => ctrl.abort(), UPSTREAM_TIMEOUT_MS);
  let res;
  try {
    res = await fetch(url, { signal: ctrl.signal, cf: { cacheEverything: true, cacheTtl: CACHE_TTL } });
  } catch (e) {
    throw new HttpError(502, "Upstream data source is unavailable. Try again shortly.");
  } finally {
    clearTimeout(timer);
  }
  if (res.status === 404) return null;
  if (!res.ok) throw new HttpError(502, `Upstream returned ${res.status}.`);
  try {
    return await res.json();
  } catch (e) {
    throw new HttpError(502, "Upstream returned invalid JSON.");
  }
}

class HttpError extends Error {
  constructor(status, message) { super(message); this.status = status; }
}

function applyQuery(results, params) {
  let rows = results;

  const q = (params.get("q") || "").trim().toLowerCase().slice(0, MAX_Q_LEN);
  if (q) rows = rows.filter((r) => Object.keys(r).some((k) => k !== "url" && String(r[k]).toLowerCase().includes(q)));

  let filters = 0;
  for (const [key, value] of params) {
    if (RESERVED.has(key)) continue;
    if (++filters > MAX_FILTERS) throw new HttpError(400, `Too many filters (max ${MAX_FILTERS}).`);
    let field = key, op = "eq";
    const m = key.match(/^(.+)__(gt|gte|lt|lte|ne|contains|eq)$/);
    if (m) { field = m[1]; op = m[2]; }
    const fn = OPS[op];
    rows = rows.filter((r) => r[field] !== undefined && r[field] !== null && fn(r[field], value));
  }

  const sort = params.get("sort");
  if (sort) {
    const dir = (params.get("order") || "asc").toLowerCase() === "desc" ? -1 : 1;
    rows = rows.slice().sort((a, b) => dir * cmp(a[sort], b[sort]));
  }
  return rows;
}

function project(rows, fieldsParam) {
  if (!fieldsParam) return rows;
  const fields = fieldsParam.split(",").map((s) => s.trim()).filter(Boolean);
  if (!fields.length) return rows;
  const keep = new Set(["id", ...fields]);
  return rows.map((r) => { const o = {}; for (const k of Object.keys(r)) if (keep.has(k)) o[k] = r[k]; return o; });
}

function pickRandom(rows, count) {
  const pool = rows.slice();
  const out = [];
  const n = Math.min(count, pool.length);
  for (let i = 0; i < n; i++) out.push(pool.splice(Math.floor(Math.random() * pool.length), 1)[0]);
  return out;
}

async function handle(request, env) {
  if (request.method === "OPTIONS") return new Response(null, { headers: BASE_HEADERS });
  if (request.method !== "GET" && request.method !== "HEAD") return err(405, "Only GET is supported.", { Allow: "GET, OPTIONS" });

  const base = ((env && env.STATIC_BASE) || "https://gratisapi.com").replace(/\/+$/, "");
  const url = new URL(request.url);
  const parts = url.pathname.split("/").filter(Boolean).map(decodeURIComponent);

  if (parts.length === 0) return help(base);
  if (parts.length === 1 && parts[0] === "health") return json({ ok: true, service: "gratisapi-dynamic", version: VERSION });
  if (parts.length === 1 && parts[0] === "openapi.json") return openapi(base, url.host);

  const api = parts[0];
  if (!API_RE.test(api)) return err(404, `Unknown API '${api}'.`);

  const data = await loadCollection(base, api);
  if (!data || !Array.isArray(data.results)) return err(404, `Unknown API '${api}'. See ${base}/api/index for the catalog.`);
  const all = data.results;

  if (parts.length >= 2) {
    const sub = parts[1];
    if (sub === "random") {
      const count = Math.max(1, Math.min(100, parseInt(url.searchParams.get("count") || "1", 10) || 1));
      const picked = pickRandom(all, count);
      return count === 1 ? json(picked[0] || null) : json({ api, random: true, count: picked.length, results: picked });
    }
    if (!ID_RE.test(sub)) return err(404, `No record '${sub}' in '${api}'.`);
    const rec = all.find((r) => String(r.id) === sub);
    return rec ? json(rec) : err(404, `No record '${sub}' in '${api}'.`);
  }

  const filtered = applyQuery(all, url.searchParams);
  const offset = Math.max(0, parseInt(url.searchParams.get("offset") || "0", 10) || 0);
  let limit = parseInt(url.searchParams.get("limit") || String(DEFAULT_LIMIT), 10);
  if (Number.isNaN(limit) || limit < 0) limit = DEFAULT_LIMIT;
  limit = Math.min(limit, MAX_LIMIT);
  const page = project(filtered.slice(offset, offset + limit), url.searchParams.get("fields"));

  return json({
    api, title: data.title, total_records: data.count,
    matched: filtered.length, offset, limit, count: page.length, results: page,
  });
}

export default {
  async fetch(request, env, ctx) {
    // Edge response cache — serve repeat queries without recomputing.
    const cacheable = request.method === "GET" && typeof caches !== "undefined" && caches.default;
    if (cacheable) {
      const hit = await caches.default.match(request);
      if (hit) return hit;
    }
    let response;
    try {
      response = await handle(request, env);
    } catch (e) {
      response = e instanceof HttpError ? err(e.status, e.message) : err(500, "Internal error.");
    }
    if (cacheable && response.status === 200 && ctx && ctx.waitUntil) {
      ctx.waitUntil(caches.default.put(request, response.clone()));
    }
    return response;
  },
};
