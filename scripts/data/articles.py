"""Articles — GratisAPI's own writing, served as data.

Even the blog is an API. Article bodies live as JSON batches under
content/articles/ so they are easy to author and review; this module loads
and merges them into a single dataset.
"""
import glob
import json
import os
import re

META = {
    "name": "articles",
    "title": "Articles",
    "description": "Guides, explainers and essays about free data, the APIs and the philosophy behind GratisAPI.",
    "emoji": "\U0001F4DD",
}

_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
_ARTICLES_DIR = os.path.join(_ROOT, "content", "articles")

# Fun endpoints to attach a "Try it" to when an article names no API of its own
# (mostly the Philosophy pieces). Rotated by index for a bit of variety.
_FALLBACK_APIS = ["quotes", "colors", "animals", "elements", "countries",
                  "planets", "gemstones", "cocktails", "constellations", "birds"]

_API_RE = re.compile(r"/api/([a-z0-9-]+)")


def _pick_try_api(art, index):
    """Find an API slug the article talks about, for a live 'Try it' button."""
    text = " ".join([art.get("body", ""), art.get("summary", ""), " ".join(art.get("tags", []))])
    for match in _API_RE.findall(text):
        if match not in ("index", "articles"):
            return match
    return _FALLBACK_APIS[index % len(_FALLBACK_APIS)]


def _load():
    items = []
    seen = set()
    for path in sorted(glob.glob(os.path.join(_ARTICLES_DIR, "*.json"))):
        with open(path, encoding="utf-8") as f:
            batch = json.load(f)
        for art in batch:
            aid = art["id"]
            if aid in seen:
                raise ValueError(f"Duplicate article id '{aid}' in {os.path.basename(path)}")
            seen.add(aid)
            words = len(str(art.get("body", "")).split())
            art["word_count"] = words
            art["reading_time_min"] = max(1, round(words / 200))
            items.append(art)
    # Newest first.
    items.sort(key=lambda a: (a.get("date", ""), a["id"]), reverse=True)
    for i, art in enumerate(items):
        art["try_api"] = _pick_try_api(art, i)
    return items


ITEMS = _load()
