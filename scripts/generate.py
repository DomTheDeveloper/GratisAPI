#!/usr/bin/env python3
"""
GratisAPI static site generator.

Reads the dataset modules in scripts/data/ and emits a fully static JSON API
under /api, plus an OpenAPI 3.1 description and a machine-readable index.

Every "endpoint" is just a JSON file served by GitHub Pages, so the whole API
is 100%% gratis: no server, no database, no rate limits, no keys.
"""
import importlib
import json
import os
import pkgutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
API_DIR = os.path.join(ROOT, "api")
BASE_URL = "https://gratisapi.com"

# Order in which datasets appear in listings (by module name). Any module not
# listed here is appended automatically, so new datasets show up without edits.
DATASET_ORDER = [
    # Reading
    "articles",
    # World & geography
    "countries", "us_states", "continents", "oceans", "mountains", "rivers",
    "lakes", "deserts", "waterfalls", "volcanoes", "national_parks",
    "tallest_buildings", "currencies", "languages",
    # Life & nature
    "animals", "dinosaurs", "dog_breeds", "cat_breeds", "birds", "sharks",
    "trees", "flowers", "fruits", "vegetables", "spices", "biomes",
    # Human body
    "human_bones", "human_organs", "body_systems", "human_senses",
    "amino_acids", "vitamins", "blood_types",
    # Science
    "elements", "minerals", "rock_types", "physical_constants",
    "math_constants", "si_prefixes",
    # Scales & measurement
    "richter_scale", "saffir_simpson", "fujita_scale", "beaufort_scale",
    "mohs_scale", "ph_scale", "scoville_scale", "uv_index", "paper_sizes",
    "cooking_measurements", "number_bases",
    # Space
    "planets", "moons", "constellations", "stars", "galaxies", "space_agencies",
    "space_missions", "mars_rovers", "telescopes", "zodiac",
    # Earth & sky
    "cloud_types",
    # Computing & web
    "http_status", "http_methods", "http_headers", "mime_types", "tcp_ports",
    "programming_languages", "operating_systems", "file_formats", "ascii",
    "css_units", "sql_keywords", "data_structures", "sorting_algorithms",
    "design_patterns", "git_commands", "logic_gates",
    # Language & symbols
    "greek_alphabet", "cyrillic_alphabet", "hebrew_alphabet", "hiragana",
    "katakana", "braille", "nato_alphabet", "morse_code", "roman_numerals",
    # Culture, myth & history
    "quotes", "us_presidents", "greek_gods", "roman_gods", "norse_gods",
    "egyptian_gods", "hindu_gods", "celtic_gods", "world_religions",
    "seven_wonders", "seven_deadly_sins", "chinese_zodiac", "birthstones",
    "tarot_major_arcana", "gemstones",
    # Arts, food & games
    "colors", "art_movements", "music_genres", "film_genres",
    "musical_instruments", "martial_arts", "olympic_sports", "cocktails",
    "teas", "cheeses", "pasta_shapes", "chess_pieces", "playing_cards",
    "calendar",
]


def load_datasets():
    import scripts.data as data_pkg
    found = {}
    for mod in pkgutil.iter_modules(data_pkg.__path__):
        module = importlib.import_module(f"scripts.data.{mod.name}")
        if hasattr(module, "META") and hasattr(module, "ITEMS"):
            found[mod.name] = module
    ordered = [found[n] for n in DATASET_ORDER if n in found]
    ordered += [m for n, m in found.items() if n not in DATASET_ORDER]
    # Normalise every API slug to lowercase-hyphen for consistent URLs.
    seen = {}
    for module in ordered:
        slug = module.META["name"].strip().lower().replace("_", "-")
        if slug in seen:
            raise ValueError(f"Duplicate API slug '{slug}' from {module.__name__} and {seen[slug]}")
        seen[slug] = module.__name__
        module.META["name"] = slug
    return ordered


def write_json(path, obj):
    """Write pretty JSON to `path` and to a clean, extension-less twin.

    GitHub Pages can't serve directory indexes as JSON, so the advertised
    ("developed") links are all extension-less — e.g. /api/animals/lion — and
    a matching .json file is kept alongside for browsers and tooling. The two
    files are byte-identical, so Git stores the blob only once.
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    text = json.dumps(obj, ensure_ascii=False, indent=2) + "\n"
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    # Extension-less twin, but only inside /api (not for openapi.json at root).
    if path.endswith(".json") and os.path.abspath(path).startswith(API_DIR + os.sep):
        with open(path[:-5], "w", encoding="utf-8") as f:
            f.write(text)


# ---- Clean, advertised ("developed") URLs — no .json anywhere ----
def item_url(api_name, item_id):
    return f"{BASE_URL}/api/{api_name}/{item_id}"


def list_url(api_name):
    # Items live under /api/<name>/, so the collection is served at .../index
    # (both /index and /index.json exist; the clean one is advertised).
    return f"{BASE_URL}/api/{api_name}/index"


def catalog_url():
    return f"{BASE_URL}/api/index"


def build_dataset(module):
    meta = module.META
    name = meta["name"]
    items = module.ITEMS
    api_out = os.path.join(API_DIR, name)

    results = []
    for item in items:
        if str(item["id"]) == "index":
            raise ValueError(f"'{name}' has an item id 'index', which clashes with the list endpoint.")
        enriched = dict(item)
        enriched["url"] = item_url(name, item["id"])
        results.append(enriched)
        # Individual endpoint: /api/<name>/<id>
        write_json(os.path.join(api_out, f"{item['id']}.json"), enriched)

    index = {
        "api": name,
        "title": meta["title"],
        "description": meta["description"],
        "emoji": meta.get("emoji", ""),
        "license": "GPL-2.0-or-later",
        "count": len(results),
        "self": list_url(name),
        "endpoints": {
            "list": list_url(name),
            "item": f"{BASE_URL}/api/{name}/{{id}}",
        },
        "fields": sorted({k for it in items for k in it.keys()}),
        "results": results,
    }
    # List endpoint lives at /api/<name> (twin: /api/<name>/index for browsers).
    write_json(os.path.join(api_out, "index.json"), index)
    return {
        "api": name,
        "title": meta["title"],
        "description": meta["description"],
        "emoji": meta.get("emoji", ""),
        "count": len(results),
        "url": list_url(name),
        "sample": item_url(name, items[0]["id"]) if items else list_url(name),
    }


def build_root_index(summaries):
    root = {
        "name": "GratisAPI",
        "tagline": "A completely free, 100% static, open-data API.",
        "description": (
            "GratisAPI is a collection of static JSON APIs hosted on GitHub "
            "Pages. Every endpoint is a plain JSON file: no keys, no rate "
            "limits, no tracking, no cost. Gratis means free."
        ),
        "license": "GPL-2.0-or-later",
        "base_url": BASE_URL,
        "self": f"{BASE_URL}/api/index",
        "documentation": f"{BASE_URL}/docs/",
        "openapi": f"{BASE_URL}/openapi.json",
        "source": "https://github.com/DomTheDeveloper/GratisAPI",
        "api_count": len(summaries),
        "total_records": sum(s["count"] for s in summaries),
        "apis": summaries,
    }
    write_json(os.path.join(API_DIR, "index.json"), root)
    return root


def build_openapi(modules, summaries):
    paths = {
        "/api/index": {
            "get": {
                "summary": "List all available APIs",
                "operationId": "listApis",
                "tags": ["meta"],
                "responses": {"200": {"description": "Directory of every GratisAPI dataset."}},
            }
        }
    }
    tags = [{"name": "meta", "description": "Discovery and metadata endpoints."}]
    for module in modules:
        meta = module.META
        name = meta["name"]
        tags.append({"name": name, "description": meta["description"]})
        paths[f"/api/{name}/index"] = {
            "get": {
                "summary": f"List all {meta['title'].lower()}",
                "operationId": f"list_{name.replace('-', '_')}",
                "tags": [name],
                "responses": {"200": {"description": f"All {meta['title'].lower()} records."}},
            }
        }
        paths[f"/api/{name}/{{id}}"] = {
            "get": {
                "summary": f"Get a single {meta['title'].lower()} record by id",
                "operationId": f"get_{name.replace('-', '_')}",
                "tags": [name],
                "parameters": [{
                    "name": "id", "in": "path", "required": True,
                    "description": "The record identifier.",
                    "schema": {"type": "string"},
                }],
                "responses": {
                    "200": {"description": "The requested record."},
                    "404": {"description": "No file exists for that id."},
                },
            }
        }
    spec = {
        "openapi": "3.1.0",
        "info": {
            "title": "GratisAPI",
            "version": "1.0.0",
            "summary": "A completely free, static, open-data API.",
            "description": (
                "GratisAPI is served entirely from static files on GitHub Pages. "
                "Every path below resolves to a real, clean, extension-less URL "
                "you can `curl` or `fetch` directly — for example "
                "`GET /api/animals/lion` — with no authentication, no rate "
                "limits, no keys and no cost. Only HTTP GET is supported. "
                "Gratis means free, and libre means free too."
            ),
            "license": {"name": "GPL-2.0-or-later", "url": "https://www.gnu.org/licenses/old-licenses/gpl-2.0.html"},
            "contact": {"name": "GratisAPI on GitHub", "url": "https://github.com/DomTheDeveloper/GratisAPI"},
        },
        "servers": [{"url": BASE_URL, "description": "GitHub Pages (production)"}],
        "tags": tags,
        "paths": paths,
    }
    write_json(os.path.join(ROOT, "openapi.json"), spec)
    return spec


def build_sitemap(modules):
    urls = [f"{BASE_URL}/", f"{BASE_URL}/articles/", f"{BASE_URL}/philosophy/",
            f"{BASE_URL}/about/", f"{BASE_URL}/history/", f"{BASE_URL}/tech/",
            f"{BASE_URL}/cost/", f"{BASE_URL}/docs/", f"{BASE_URL}/openapi.json",
            catalog_url()]
    for module in modules:
        name = module.META["name"]
        urls.append(list_url(name))
        for item in module.ITEMS:
            urls.append(item_url(name, item["id"]))
    body = "\n".join(f"  <url><loc>{u}</loc></url>" for u in urls)
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           f"{body}\n</urlset>\n")
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(xml)


def main():
    modules = load_datasets()
    summaries = [build_dataset(m) for m in modules]
    root = build_root_index(summaries)
    build_openapi(modules, summaries)
    build_sitemap(modules)
    print(f"Generated {root['api_count']} APIs, {root['total_records']} records.")
    for s in summaries:
        print(f"  - {s['api']:<14} {s['count']:>4} records")


if __name__ == "__main__":
    main()
