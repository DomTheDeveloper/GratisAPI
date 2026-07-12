// Node test for the dynamic-api Worker. Mocks the upstream static API so the
// Worker's fetch handler can be exercised without a network. Run: node test.mjs
import worker from "./src/index.js";

const COLLECTION = {
  api: "animals", title: "Animals", count: 5,
  results: [
    { id: "lion", common_name: "Lion", class: "Mammalia", diet: "Carnivore", url: "u/lion" },
    { id: "tiger", common_name: "Tiger", class: "Mammalia", diet: "Carnivore", url: "u/tiger" },
    { id: "bald-eagle", common_name: "Bald Eagle", class: "Aves", diet: "Carnivore", url: "u/eagle" },
    { id: "salmon", common_name: "Atlantic Salmon", class: "Actinopterygii", diet: "Carnivore", url: "u/salmon" },
    { id: "human", common_name: "Human", class: "Mammalia", diet: "Omnivore", url: "u/human" },
  ],
};

// Mock global fetch: return the collection for the animals index, 404 otherwise.
globalThis.fetch = async (url) => {
  if (String(url).includes("/api/animals/index")) {
    return new Response(JSON.stringify(COLLECTION), { status: 200 });
  }
  return new Response("not found", { status: 404 });
};

const env = { STATIC_BASE: "https://example.test" };
async function get(path, method = "GET") {
  const res = await worker.fetch(new Request("https://dyn.test" + path, { method }), env, {});
  let body = null;
  try { body = JSON.parse(await res.text()); } catch (e) { /* non-json */ }
  return { status: res.status, body, headers: res.headers };
}

let passed = 0, failed = 0;
function check(name, cond) {
  if (cond) { passed++; console.log("  ✓", name); }
  else { failed++; console.log("  ✗", name); }
}

console.log("dynamic-api worker tests:");

let r = await get("/");
check("root returns help with examples", r.status === 200 && Array.isArray(r.body.examples));

r = await get("/health");
check("health ok", r.body.ok === true);

r = await get("/animals");
check("collection returns all 5", r.body.matched === 5 && r.body.count === 5);

r = await get("/animals?class=Mammalia");
check("filter class=Mammalia → 3", r.body.matched === 3);

r = await get("/animals?diet=Omnivore");
check("filter diet=Omnivore → 1 (human)", r.body.matched === 1 && r.body.results[0].id === "human");

r = await get("/animals?q=eagle");
check("search q=eagle → bald-eagle", r.body.matched === 1 && r.body.results[0].id === "bald-eagle");

r = await get("/animals?sort=common_name&limit=2");
check("sort by common_name asc, limit 2 → Atlantic Salmon first", r.body.results[0].id === "salmon" && r.body.count === 2);

r = await get("/animals?sort=common_name&order=desc&limit=1");
check("sort desc → Tiger first", r.body.results[0].id === "tiger");

r = await get("/animals?limit=2&offset=2");
check("pagination offset=2 limit=2", r.body.offset === 2 && r.body.count === 2 && r.body.matched === 5);

r = await get("/animals?fields=common_name");
check("projection keeps id + common_name only", Object.keys(r.body.results[0]).sort().join(",") === "common_name,id");

r = await get("/animals/lion");
check("item /animals/lion", r.body.id === "lion" && r.body.common_name === "Lion");

r = await get("/animals/nope");
check("missing item → 404", r.status === 404);

r = await get("/animals/random");
check("random returns one record", typeof r.body.id === "string");

r = await get("/animals/random?count=3");
check("random count=3 returns 3", r.body.results && r.body.results.length === 3);

r = await get("/nonexistent");
check("unknown api → 404", r.status === 404);

// operator: numeric compare on a synthetic field
COLLECTION.results.forEach((x, i) => (x.size = (i + 1) * 10));
r = await get("/animals?size__gte=30&sort=size");
check("operator size__gte=30 → 3 rows", r.body.matched === 3 && r.body.results[0].size === 30);

// ---- production hardening ----
r = await get("/openapi.json");
check("openapi.json served", r.body && r.body.openapi === "3.1.0" && !!r.body.paths["/{api}"]);

r = await get("/animals", "POST");
check("POST → 405 with Allow header", r.status === 405 && r.headers.get("Allow") === "GET, OPTIONS");

r = await get("/animals", "OPTIONS");
check("OPTIONS preflight → CORS", r.status === 200 && r.headers.get("Access-Control-Allow-Origin") === "*");

r = await get("/..%2fetc");
check("invalid api slug → 404", r.status === 404);

r = await get("/animals");
check("security header nosniff present", r.headers.get("X-Content-Type-Options") === "nosniff");
check("version header present", !!r.headers.get("X-GratisAPI-Version"));

r = await get("/animals/lion");
check("error/record envelope: cache-control set", r.headers.get("Cache-Control").includes("max-age"));

// too many filters → 400
{
  const qs = Array.from({ length: 30 }, (_, i) => `f${i}=x`).join("&");
  r = await get("/animals?" + qs);
  check("too many filters → 400", r.status === 400);
}

// upstream failure → 502
globalThis.fetch = async () => { throw new Error("network down"); };
r = await get("/animals");
check("upstream failure → 502", r.status === 502);

console.log(`\n${passed} passed, ${failed} failed`);
process.exit(failed ? 1 : 0);
