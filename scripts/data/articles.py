"""Articles — GratisAPI's own writing, served as data.

Even the blog is an API. Article bodies live as JSON batches under
content/articles/ so they are easy to author and review; this module loads
and merges them into a single dataset.
"""
import glob
import json
import os

META = {
    "name": "articles",
    "title": "Articles",
    "description": "Guides, explainers and essays about free data, the APIs and the philosophy behind GratisAPI.",
    "emoji": "\U0001F4DD",
}

_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
_ARTICLES_DIR = os.path.join(_ROOT, "content", "articles")


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
    return items


ITEMS = _load()
