# GratisAPI — Dynamic API (Cloudflare Worker)

The static API answers *"give me this dataset."* This Worker adds the dynamic
verbs on top of it — **filter, search, sort, paginate, random** — with no
database. It fetches the matching static collection from Cloudflare's edge cache
and applies the query in memory, so it shares the same free data and stays cheap.

## Endpoints

| Route | What it does |
| --- | --- |
| `GET /` | Help / capabilities |
| `GET /health` | `{ "ok": true }` |
| `GET /:api` | A collection, with query operators (below) |
| `GET /:api/random?count=N` | One (or `N`) random record(s) |
| `GET /:api/:id` | A single record |
| `GET /openapi.json` | OpenAPI 3.1 description of the dynamic API |

Production hardening: edge response caching (Cache API), an 8s upstream fetch
timeout, strict input validation (SSRF-safe slugs), filter/query caps, CORS +
security headers, structured JSON errors, smart placement and observability.

### Query operators on `/:api`

- `?q=text` — case-insensitive search across all fields
- `?<field>=value` — exact match
- `?<field>__gt=` `__gte=` `__lt=` `__lte=` `__ne=` `__contains=` — comparisons
- `?sort=field&order=asc|desc`
- `?fields=a,b,c` — project only these fields (`id` always kept)
- `?limit=N` (default 50, max 1000) `&offset=M`

### Examples

```
/quotes/random
/animals?class=Mammalia&sort=common_name&limit=5
/elements?category=Noble%20gas&fields=name,symbol,atomic_number
/countries?population_millions__gt=100&sort=population_millions&order=desc
/colors?q=blue&limit=10
```

Every non-paginated GratisAPI dataset works (10,000+ of them). The `numbers`
family is paginated on the static side, so use its static page files for bulk.

## Test

```bash
node test.mjs      # 16 unit tests, no network (mocks the upstream)
```

## Deploy

Two ways — pick one.

**A. Automatic (GitHub Actions).** Add one repo secret and push:

1. In Cloudflare, create an API token with the **Edit Cloudflare Workers** template.
2. In GitHub → Settings → Secrets and variables → Actions, add
   `CLOUDFLARE_API_TOKEN` (and optionally `CLOUDFLARE_ACCOUNT_ID`).
3. Push any change under `workers/dynamic-api/` (or run the *Deploy Dynamic API
   Worker* workflow manually). The workflow tests then `wrangler deploy`s it.

**B. Local.**

```bash
cd workers/dynamic-api
npm install
npx wrangler login        # or export CLOUDFLARE_API_TOKEN=...
npx wrangler deploy
```

After deploy it's live at `https://gratisapi-dynamic.<your-subdomain>.workers.dev`.
To put it on a custom domain (e.g. `api.gratisapi.com`), uncomment the `routes`
block in `wrangler.toml` (the zone must be in your Cloudflare account).

## Configuration

`wrangler.toml` sets `STATIC_BASE` (default `https://gratisapi.com`) — the static
API this Worker reads from. Point it at a fork to serve your own data.

Licensed GPL-2.0-or-later.
