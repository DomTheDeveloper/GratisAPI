# GratisAPI 🆓

**A completely free, 100% static, open-data API.**

_Gratis_ means free — and GratisAPI is free in every sense. No API keys, no rate
limits, no sign-up, no tracking, no cost. Ever. Every endpoint is a plain JSON
file served straight from GitHub Pages' global CDN.

🌐 **Live:** https://domthedeveloper.github.io/GratisAPI/
📖 **Docs (Swagger UI):** https://domthedeveloper.github.io/GratisAPI/docs/
📄 **OpenAPI spec:** https://domthedeveloper.github.io/GratisAPI/openapi.json

---

## How it works

There is no server. Every "endpoint" is a static `.json` file. You `GET` it with
`curl`, `fetch`, or anything that speaks HTTP:

```bash
# List every available API
curl https://domthedeveloper.github.io/GratisAPI/api/index.json

# Get one record
curl https://domthedeveloper.github.io/GratisAPI/api/animals/lion.json

# Get a whole dataset
curl https://domthedeveloper.github.io/GratisAPI/api/elements/index.json
```

```js
// Random quote in the browser (CORS is enabled)
const { results } = await fetch(
  "https://domthedeveloper.github.io/GratisAPI/api/quotes/index.json"
).then((r) => r.json());
const q = results[Math.floor(Math.random() * results.length)];
console.log(`"${q.quote}" — ${q.author}`);
```

### Endpoint shape

| Endpoint | Returns |
| --- | --- |
| `/api/index.json` | Directory of every dataset |
| `/api/<name>/index.json` | Metadata + **all** records for one dataset |
| `/api/<name>/<id>.json` | A single record |

Each dataset index looks like:

```json
{
  "api": "animals",
  "title": "Animals",
  "count": 20,
  "endpoints": { "list": ".../index.json", "item": ".../{id}.json" },
  "fields": ["class", "common_name", "..."],
  "results": [ { "id": "lion", "...": "..." } ]
}
```

## Available APIs

| API | What's in it |
| --- | --- |
| 🦊 `animals` | Full taxonomy — kingdom, phylum, class, order, family, genus, species |
| 💬 `quotes` | Famous quotes with authors and tags |
| 🎨 `colors` | Named web colors with hex, RGB and HSL |
| 🌍 `countries` | Capital, ISO codes, continent, currency, population |
| 🗺️ `continents` | The seven continents with area and population |
| 🪐 `planets` | Planets and dwarf planets of the Solar System |
| 🧪 `elements` | All 118 chemical elements |
| 📡 `http-status` | HTTP status codes and reason phrases |
| 💱 `currencies` | ISO 4217 currency codes and symbols |
| 🗣️ `languages` | ISO 639-1 language codes and native names |
| ♌ `zodiac` | The twelve zodiac signs |
| 📅 `calendar` | Months and days of the week |

## Building locally

The JSON files under `api/` are generated from the datasets in `scripts/data/`.

```bash
python3 -m scripts.generate      # regenerates /api and openapi.json
```

To add a new API, drop a module in `scripts/data/` that exposes a `META` dict
and an `ITEMS` list, then re-run the generator. That's it.

## Contributing

Pull requests welcome — new datasets, corrections, more records. Keep data
accurate and sourced from public/open information.

## License

GratisAPI is licensed under the **GNU General Public License v2.0 or later**
(GPL-2.0-or-later). See [`LICENSE`](./LICENSE).
