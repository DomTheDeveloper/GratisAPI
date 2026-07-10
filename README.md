# GratisAPI 🆓

**A completely free, 100% static, open-data API.**

_Gratis_ means free — and GratisAPI is free in every sense. No API keys, no rate
limits, no sign-up, no tracking, no cost. Ever. Every endpoint is a plain JSON
file served straight from GitHub Pages' global CDN.

**116 APIs · 3,890 records · 120 articles · 0 dollars.**

🌐 **Live:** https://domthedeveloper.github.io/GratisAPI/
📖 **Docs (Swagger UI):** https://domthedeveloper.github.io/GratisAPI/docs/
📝 **Articles:** https://domthedeveloper.github.io/GratisAPI/articles/
🆓 **Philosophy:** https://domthedeveloper.github.io/GratisAPI/philosophy/
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

There are **116 APIs** in total — from `amino-acids` to `volcanoes`. The live,
always-current directory of every one is at
[`/api/index.json`](https://domthedeveloper.github.io/GratisAPI/api/index.json).
A selection is listed below.

| API | Records | What's in it |
| --- | ---: | --- |
| 🌍 `countries` | 197 | Capital, ISO codes, continent, currency, population, flag |
| 🇺🇸 `us-states` | 51 | Capital, largest city, population, area, region |
| 🗺️ `continents` | 7 | Area, population, country counts |
| 🌊 `oceans` | 5 | Area, average/max depth, deepest point |
| ⛰️ `mountains` | 31 | Elevation, range, first-ascent year |
| 🏞️ `rivers` | 31 | Length, continent, outflow |
| 🏞️ `lakes` | 25 | Area, depth, type |
| 🏜️ `deserts` | 21 | Area, continent, type |
| 💦 `waterfalls` | 16 | Height, river, location |
| 💱 `currencies` | 101 | ISO 4217 code, symbol, minor unit |
| 🗣️ `languages` | 81 | ISO 639-1 code, native name, direction |
| 🦊 `animals` | 71 | Full taxonomy kingdom → species |
| 🦖 `dinosaurs` | 40 | Period, diet, size, region |
| 🐕 `dog-breeds` | 51 | Group, origin, size, temperament |
| 🐈 `cat-breeds` | 31 | Origin, coat, temperament |
| 🐦 `birds` | 41 | Family, habitat, diet, wingspan |
| 🦈 `sharks` | 25 | Size, habitat, danger rating |
| 🌳 `trees` | 32 | Leaf type, height, native region |
| 🌷 `flowers` | 30 | Color, bloom season, meaning |
| 🍎 `fruits` | 40 | Botanical type, origin, calories |
| 🥕 `vegetables` | 36 | Type, color, calories |
| 🌶️ `spices` | 36 | Plant part, origin, heat level |
| 🧪 `elements` | 118 | All 118 chemical elements |
| 🔬 `physical-constants` | 25 | Symbol, value, unit |
| ➗ `math-constants` | 20 | Symbol, value, description |
| 🔢 `si-prefixes` | 24 | Symbol, power of ten |
| 💊 `vitamins` | 13 | Function, solubility, sources |
| 🩸 `blood-types` | 8 | Donor/recipient compatibility |
| 💨 `beaufort-scale` | 13 | Wind force 0–12 |
| 🪐 `planets` | 9 | Planets & dwarf planets |
| 🌙 `moons` | 30 | Parent planet, discovery |
| ✨ `constellations` | 88 | All 88 IAU constellations |
| ⭐ `stars` | 30 | Magnitude, distance, spectral type |
| ♌ `zodiac` | 12 | Western zodiac signs |
| 📡 `http-status` | 63 | Status codes & reason phrases |
| 🔗 `http-methods` | 9 | Safety, idempotency, caching |
| 📄 `mime-types` | 61 | Category & file extensions |
| 🔌 `tcp-ports` | 62 | Well-known ports & services |
| 💻 `programming-languages` | 50 | Year, paradigm, typing |
| 🔤 `ascii` | 95 | Printable ASCII table |
| 🇬🇷 `greek-alphabet` | 24 | Transliteration, numeric value |
| 📶 `nato-alphabet` | 26 | Code words & pronunciation |
| ·−· `morse-code` | 54 | Letters, digits, punctuation |
| Ⅼ `roman-numerals` | 33 | Arabic ↔ Roman |
| 💬 `quotes` | 122 | Famous quotes with authors & tags |
| 🏛️ `us-presidents` | 46 | Party, term, vice president |
| ⚡ `greek-gods` | 34 | Domain, Roman equivalent |
| ⚔️ `norse-gods` | 22 | Domain, type, symbol |
| 𓂀 `egyptian-gods` | 21 | Domain, symbol, depiction |
| 🗿 `seven-wonders` | 14 | Ancient + New wonders |
| 🐉 `chinese-zodiac` | 12 | Element, yin-yang, traits |
| 💎 `birthstones` | 12 | Monthly stones & meanings |
| 🔮 `tarot-major-arcana` | 22 | Keywords, element |
| 💠 `gemstones` | 31 | Color, Mohs hardness |
| 🎨 `colors` | 141 | Hex, RGB, HSL |
| 🎸 `musical-instruments` | 42 | Family, classification |
| 🍸 `cocktails` | 41 | Base spirit, glass, IBA status |
| ♟️ `chess-pieces` | 6 | Symbols, value, movement |
| 🃏 `playing-cards` | 52 | A standard 52-card deck |
| 📅 `calendar` | 19 | Months & days of the week |

## Articles & Philosophy

GratisAPI is more than data. The [**Articles**](https://domthedeveloper.github.io/GratisAPI/articles/)
section has **120 articles** across five categories — Tutorials, Philosophy,
Science, Culture and Reference — covering how to use the APIs from any language,
deep-dives into the datasets, and essays on free data. Even the articles are an
API: they're served from [`/api/articles/`](https://domthedeveloper.github.io/GratisAPI/api/articles/index.json).

The [**Philosophy**](https://domthedeveloper.github.io/GratisAPI/philosophy/) page
explains the two meanings of "free" — _gratis_ (free of charge) and _libre_ (free
as in freedom) — the free software movement, Richard Stallman and the FSF, and why
GratisAPI is deliberately both.

## Building locally

The JSON files under `api/`, plus `openapi.json` and `sitemap.xml`, are all
**generated** from the dataset modules in `scripts/data/`.

```bash
python3 -m scripts.generate      # regenerates /api, openapi.json and sitemap.xml
```

To add a new API, drop a module in `scripts/data/` that exposes a `META` dict
and an `ITEMS` list (each item needs a unique `id`), then re-run the generator.
The new dataset is auto-discovered — no other file needs editing.

```python
# scripts/data/example.py
META = {"name": "example", "title": "Example", "description": "...", "emoji": "📦"}
ITEMS = [{"id": "one", "value": 1}, {"id": "two", "value": 2}]
```

## Deployment & CI

Two GitHub Actions workflows keep the site honest and live:

- **`.github/workflows/ci.yml`** — on every push/PR, regenerates the API and
  fails if the committed output is stale or any JSON is invalid.
- **`.github/workflows/deploy.yml`** — on push to `gh-pages`, rebuilds and
  publishes to GitHub Pages. Requires **Settings → Pages → Source = "GitHub
  Actions"**. (If you instead serve directly from the `gh-pages` branch, the
  committed files already work as-is and this workflow is optional.)

## Contributing

Pull requests welcome — new datasets, corrections, more records. Keep data
accurate and sourced from public/open information.

## License

GratisAPI is licensed under the **GNU General Public License v2.0 or later**
(GPL-2.0-or-later). See [`LICENSE`](./LICENSE).
