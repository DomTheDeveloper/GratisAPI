"""Multiples APIs — one API per integer N listing its first multiples.

/api/multiples-of-<n> gives N x 1 .. N x 60. Computed, exact.
"""
COUNT = 2500   # multiples-of-1 .. multiples-of-2500
TERMS = 60

DATASETS = []
for _n in range(1, COUNT + 1):
    DATASETS.append({
        "meta": {
            "name": f"multiples-of-{_n}",
            "title": f"Multiples of {_n}",
            "description": f"The first {TERMS} multiples of {_n}.",
            "emoji": "✖️", "list_only": True, "family": True,
        },
        "items": [{"id": k, "index": k, "multiple": _n * k} for k in range(1, TERMS + 1)],
    })
