"""Powers APIs — one API per base N listing N^k within exact-integer range.

/api/powers-of-<n> gives N^0, N^1, ... up to the largest power below 2^53
(so every value is an exact JSON integer).
"""
SAFE = 2 ** 53
BASES = range(2, 201)   # powers-of-2 .. powers-of-200

DATASETS = []
for _n in BASES:
    _terms, _v, _k = [], 1, 0
    while _v < SAFE:
        _terms.append((_k, _v))
        _k += 1
        _v *= _n
    DATASETS.append({
        "meta": {
            "name": f"powers-of-{_n}",
            "title": f"Powers of {_n}",
            "description": f"{_n}^k for k = 0 .. {_terms[-1][0]} (every power below 2^53).",
            "emoji": "\U0001F53A", "list_only": True, "family": True,
        },
        "items": [{"id": k, "exponent": k, "value": v} for k, v in _terms],
    })
