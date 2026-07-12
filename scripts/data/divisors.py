"""Divisors APIs — one API per integer N listing all of its divisors.

/api/divisors-of-<n> gives every positive divisor of N, plus their count and
sum in the index description. Computed, exact.
"""
COUNT = 2500   # divisors-of-1 .. divisors-of-2500


def _divisors(n):
    ds = []
    d = 1
    while d * d <= n:
        if n % d == 0:
            ds.append(d)
            if d != n // d:
                ds.append(n // d)
        d += 1
    return sorted(ds)


DATASETS = []
for _n in range(1, COUNT + 1):
    _ds = _divisors(_n)
    DATASETS.append({
        "meta": {
            "name": f"divisors-of-{_n}",
            "title": f"Divisors of {_n}",
            "description": (f"The {len(_ds)} divisor{'s' if len(_ds) != 1 else ''} of {_n} "
                            f"(sum {sum(_ds)})" + (", a prime" if len(_ds) == 2 else "") + "."),
            "emoji": "➗", "list_only": True, "family": True,
        },
        "items": [{"id": i, "index": i + 1, "divisor": d} for i, d in enumerate(_ds)],
    })
