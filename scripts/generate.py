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
BASE_URL = "https://domthedeveloper.github.io/GratisAPI"

# Order in which datasets appear in listings (by module name). Any module not
# listed here is appended automatically, so new datasets show up without edits.
DATASET_ORDER = [
    # World & geography
    "countries", "us_states", "continents", "oceans", "mountains", "rivers",
    "lakes", "deserts", "waterfalls", "currencies", "languages",
    # Life & nature
    "animals", "dinosaurs", "dog_breeds", "cat_breeds", "birds", "sharks",
    "trees", "flowers", "fruits", "vegetables", "spices",
    # Science
    "elements", "physical_constants", "math_constants", "si_prefixes",
    "vitamins", "blood_types", "beaufort_scale",
    # Space
    "planets", "moons", "constellations", "stars", "zodiac",
    # Computing & web
    "http_status", "http_methods", "mime_types", "tcp_ports",
    "programming_languages", "ascii",
    # Language & symbols
    "greek_alphabet", "nato_alphabet", "morse_code", "roman_numerals",
    # Culture, myth & history
    "quotes", "us_presidents", "greek_gods", "norse_gods", "egyptian_gods",
    "seven_wonders", "chinese_zodiac", "birthstones", "tarot_major_arcana",
    "gemstones",
    # Arts, food & games
    "colors", "musical_instruments", "cocktails", "chess_pieces",
    "playing_cards", "calendar",
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
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
        f.write("\n")


def item_url(api_name, item_id):
    return f"{BASE_URL}/api/{api_name}/{item_id}.json"


def build_dataset(module):
    meta = module.META
    name = meta["name"]
    items = module.ITEMS
    api_out = os.path.join(API_DIR, name)

    results = []
    for item in items:
        enriched = dict(item)
        enriched["url"] = item_url(name, item["id"])
        results.append(enriched)
        # Individual endpoint: /api/<name>/<id>.json
        write_json(os.path.join(api_out, f"{item['id']}.json"), enriched)

    index = {
        "api": name,
        "title": meta["title"],
        "description": meta["description"],
        "emoji": meta.get("emoji", ""),
        "license": "GPL-2.0-or-later",
        "count": len(results),
        "self": f"{BASE_URL}/api/{name}/index.json",
        "endpoints": {
            "list": f"{BASE_URL}/api/{name}/index.json",
            "item": f"{BASE_URL}/api/{name}/{{id}}.json",
        },
        "fields": sorted({k for it in items for k in it.keys()}),
        "results": results,
    }
    write_json(os.path.join(api_out, "index.json"), index)
    return {
        "api": name,
        "title": meta["title"],
        "description": meta["description"],
        "emoji": meta.get("emoji", ""),
        "count": len(results),
        "url": f"{BASE_URL}/api/{name}/index.json",
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
        "/api/index.json": {
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
        paths[f"/api/{name}/index.json"] = {
            "get": {
                "summary": f"List all {meta['title'].lower()}",
                "operationId": f"list_{name.replace('-', '_')}",
                "tags": [name],
                "responses": {"200": {"description": f"All {meta['title'].lower()} records."}},
            }
        }
        paths[f"/api/{name}/{{id}}.json"] = {
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
                "GratisAPI is served entirely from static JSON files on GitHub "
                "Pages. Every path below resolves to a real file you can `curl` "
                "or `fetch` directly — no authentication, no rate limits, "
                "no cost. Only HTTP GET is supported."
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
    urls = [f"{BASE_URL}/", f"{BASE_URL}/docs/", f"{BASE_URL}/openapi.json",
            f"{BASE_URL}/api/index.json"]
    for module in modules:
        name = module.META["name"]
        urls.append(f"{BASE_URL}/api/{name}/index.json")
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
