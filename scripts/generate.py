#!/usr/bin/env python3
"""
GratisAPI static site generator.

Reads the dataset modules in scripts/data/ and emits a fully static JSON API
under /api, plus an OpenAPI 3.1 description and a machine-readable index.

Every "endpoint" is just a static JSON file, so the whole API is 100%% gratis:
no server, no database, no rate limits, no keys.

A module contributes datasets in one of two ways:
  * `META` (dict) + `ITEMS` (iterable of dicts)          -> a single API
  * `DATASETS` (iterable of {"meta": ..., "items": ...})  -> many APIs

Per-dataset META flags:
  * list_only=True  -> no per-record files; the index carries all records
  * paginated=True  -> huge computed sets; emit page files + a capped set of
                       individual records, with a small sample in the index
                       (page_size, individual_cap tune the split)
  * family=True     -> omitted from the (otherwise enormous) OpenAPI spec
"""
import importlib
import json
import os
import pkgutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
API_DIR = os.path.join(ROOT, "api")
BASE_URL = "https://gratisapi.com"

# Order in which curated modules appear first (by module name). Generated
# "family" modules (numbers, unicode blocks, calendars, ...) append after.
DATASET_ORDER = [
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
    # Generated families (large, computed) — numbers last; it's a novelty.
    "unicodeblocks", "unicode_pages", "mathseq", "powers", "collatz",
    "divisors", "multiples", "calendars", "timestables", "numbers",
]


class Dataset:
    """One API: normalised metadata plus its (possibly lazy) items."""
    __slots__ = ("meta", "items", "module")

    def __init__(self, meta, items, module):
        self.meta = meta
        self.items = items
        self.module = module

    @property
    def name(self):
        return self.meta["name"]


def load_datasets():
    import scripts.data as data_pkg
    modules = {}
    for mod in pkgutil.iter_modules(data_pkg.__path__):
        modules[mod.name] = importlib.import_module(f"scripts.data.{mod.name}")

    order = [n for n in DATASET_ORDER if n in modules]
    order += [n for n in modules if n not in DATASET_ORDER]

    datasets = []
    seen = {}
    for n in order:
        m = modules[n]
        raw = []
        if hasattr(m, "DATASETS"):
            for d in m.DATASETS:
                raw.append((d["meta"], d["items"]))
        elif hasattr(m, "META") and hasattr(m, "ITEMS"):
            raw.append((m.META, m.ITEMS))
        else:
            continue
        for meta, items in raw:
            slug = meta["name"].strip().lower().replace("_", "-")
            if slug in seen:
                raise ValueError(f"Duplicate API slug '{slug}' from {n} and {seen[slug]}")
            seen[slug] = n
            nmeta = dict(meta)
            nmeta["name"] = slug
            datasets.append(Dataset(nmeta, items, n))
    return datasets


def write_json(path, obj):
    """Write pretty JSON to `path` plus a clean, extension-less twin.

    GitHub Pages can't serve directory indexes as JSON, so the advertised
    ("developed") links are all extension-less — e.g. /api/animals/lion — and a
    matching .json file sits alongside for browsers. The two files are
    byte-identical, so Git stores the blob only once.
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    text = json.dumps(obj, ensure_ascii=False, indent=2) + "\n"
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    if path.endswith(".json") and os.path.abspath(path).startswith(API_DIR + os.sep):
        with open(path[:-5], "w", encoding="utf-8") as f:
            f.write(text)


def write_single(path_no_ext, obj):
    """Write one compact extension-less JSON file (used for bulk page files)."""
    os.makedirs(os.path.dirname(path_no_ext), exist_ok=True)
    with open(path_no_ext, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, separators=(",", ":"))
        f.write("\n")


# ---- Clean, advertised ("developed") URLs — no .json anywhere ----
def item_url(api_name, item_id):
    return f"{BASE_URL}/api/{api_name}/{item_id}"


def list_url(api_name):
    return f"{BASE_URL}/api/{api_name}/index"


def catalog_url():
    return f"{BASE_URL}/api/index"


def _index_base(meta, name, count):
    return {
        "api": name,
        "title": meta["title"],
        "description": meta["description"],
        "emoji": meta.get("emoji", ""),
        "license": "GPL-2.0-or-later",
        "count": count,
        "self": list_url(name),
        "endpoints": {"list": list_url(name), "item": f"{BASE_URL}/api/{name}/{{id}}"},
    }


def _summary(meta, name, count, first_id):
    return {
        "api": name,
        "title": meta["title"],
        "description": meta["description"],
        "emoji": meta.get("emoji", ""),
        "count": count,
        "url": list_url(name),
        "sample": item_url(name, first_id) if first_id is not None else list_url(name),
    }


def build_dataset(ds):
    meta, name, items = ds.meta, ds.name, ds.items
    api_out = os.path.join(API_DIR, name)
    paginated = meta.get("paginated", False)
    list_only = meta.get("list_only", False)

    if paginated:
        return _build_paginated(ds, api_out)

    fields = set()
    results = []
    first_id = None
    for item in items:
        iid = str(item["id"])
        if iid == "index":
            raise ValueError(f"'{name}' has an item id 'index', which clashes with the list endpoint.")
        if first_id is None:
            first_id = iid
        fields.update(item.keys())
        rec = dict(item)
        rec["url"] = item_url(name, iid)
        results.append(rec)
        if not list_only:
            write_json(os.path.join(api_out, iid + ".json"), rec)

    index = _index_base(meta, name, len(results))
    index["fields"] = sorted(fields)
    index["results"] = results
    if list_only:
        index["endpoints"] = {"list": list_url(name)}
        index["note"] = "All records are included in this response; there are no per-record endpoints."
        # Single file (no .json twin) — keeps the file count sane across
        # thousands of computed family APIs.
        write_single(os.path.join(api_out, "index"), index)
    else:
        write_json(os.path.join(api_out, "index.json"), index)
    return _summary(meta, name, len(results), first_id)


def _build_paginated(ds, api_out):
    meta, name, items = ds.meta, ds.name, ds.items
    page_size = meta.get("page_size", 1000)
    icap = meta.get("individual_cap", 0)

    fields = set()
    sample = []
    count = 0
    first_id = None
    page = []
    page_no = 0

    def flush():
        nonlocal page, page_no
        if not page:
            return
        write_single(os.path.join(api_out, "page", str(page_no)),
                     {"api": name, "page": page_no, "count": len(page), "results": page})
        page_no += 1
        page = []

    for item in items:
        iid = str(item["id"])
        if iid == "index":
            raise ValueError(f"'{name}' item id clashes with 'index'.")
        if first_id is None:
            first_id = iid
        fields.update(item.keys())
        if count < icap:
            rec_i = dict(item)
            rec_i["url"] = item_url(name, iid)
            write_json(os.path.join(api_out, iid + ".json"), rec_i)
        if len(sample) < 50:
            s = dict(item)
            s["url"] = item_url(name, iid)
            sample.append(s)
        page.append(dict(item))
        count += 1
        if len(page) >= page_size:
            flush()
    flush()

    index = _index_base(meta, name, count)
    index["fields"] = sorted(fields)
    index["paginated"] = True
    index["page_size"] = page_size
    index["pages"] = page_no
    index["page_endpoint"] = f"{BASE_URL}/api/{name}/page/{{n}}"
    index["note"] = (f"{count:,} records. Fetch pages of {page_size} at "
                     f"/api/{name}/page/0 .. /api/{name}/page/{page_no - 1}, or single "
                     f"records at /api/{name}/{{id}} for id 0-{icap - 1}.")
    index["results"] = sample
    write_json(os.path.join(api_out, "index.json"), index)
    return _summary(meta, name, count, first_id)


def build_root_index(summaries):
    root = {
        "name": "GratisAPI",
        "tagline": "A completely free, 100% static, open-data API.",
        "description": (
            "GratisAPI is a collection of static JSON APIs. Every endpoint is a "
            "plain file at a clean URL: no keys, no rate limits, no tracking, no "
            "cost. Gratis means free."
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


def build_openapi(datasets):
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
    # Skip generated families to keep the spec (and Swagger UI) usable.
    for ds in datasets:
        meta = ds.meta
        if meta.get("family"):
            continue
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
                "parameters": [{"name": "id", "in": "path", "required": True,
                                "description": "The record identifier.",
                                "schema": {"type": "string"}}],
                "responses": {"200": {"description": "The requested record."},
                              "404": {"description": "No file exists for that id."}},
            }
        }
    spec = {
        "openapi": "3.1.0",
        "info": {
            "title": "GratisAPI",
            "version": "1.0.0",
            "summary": "A completely free, static, open-data API.",
            "description": (
                "GratisAPI is served entirely from static files. Every path below "
                "resolves to a real, clean, extension-less URL you can `curl` or "
                "`fetch` directly — for example `GET /api/animals/lion` — with no "
                "authentication, no rate limits, no keys and no cost. Only HTTP GET "
                "is supported. Large generated families (numbers, unicode blocks, "
                "calendars, times tables, math sequences) are omitted here for "
                "brevity — see /api/index for the full catalog."
            ),
            "license": {"name": "GPL-2.0-or-later", "url": "https://www.gnu.org/licenses/old-licenses/gpl-2.0.html"},
            "contact": {"name": "GratisAPI on GitHub", "url": "https://github.com/DomTheDeveloper/GratisAPI"},
        },
        "servers": [{"url": BASE_URL, "description": "production"}],
        "tags": tags,
        "paths": paths,
    }
    write_json(os.path.join(ROOT, "openapi.json"), spec)
    return spec


def build_sitemap(datasets, summaries):
    urls = [f"{BASE_URL}/", f"{BASE_URL}/builder/", f"{BASE_URL}/features/",
            f"{BASE_URL}/articles/", f"{BASE_URL}/philosophy/",
            f"{BASE_URL}/about/", f"{BASE_URL}/history/", f"{BASE_URL}/tech/",
            f"{BASE_URL}/cost/", f"{BASE_URL}/docs/", f"{BASE_URL}/openapi.json",
            catalog_url()]
    for ds in datasets:
        name = ds.name
        urls.append(list_url(name))
        # Per-record URLs only for "full" datasets (families are list-only/paginated
        # and would bloat the sitemap with millions of entries).
        if not ds.meta.get("list_only") and not ds.meta.get("paginated"):
            for item in ds.items:
                urls.append(item_url(name, item["id"]))
    body = "\n".join(f"  <url><loc>{u}</loc></url>" for u in urls)
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           f"{body}\n</urlset>\n")
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(xml)


def main():
    datasets = load_datasets()
    summaries = [build_dataset(ds) for ds in datasets]
    root = build_root_index(summaries)
    build_openapi(datasets)
    build_sitemap(datasets, summaries)
    print(f"Generated {root['api_count']:,} APIs, {root['total_records']:,} records.")
    families = {}
    for ds in datasets:
        if ds.meta.get("family"):
            families[ds.module] = families.get(ds.module, 0) + 1
    curated = root["api_count"] - sum(families.values())
    print(f"  curated/single APIs: {curated}")
    for mod, n in families.items():
        print(f"  family '{mod}': {n} APIs")


if __name__ == "__main__":
    main()
