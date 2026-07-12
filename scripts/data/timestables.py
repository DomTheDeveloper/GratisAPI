"""Multiplication table APIs — one API per times table (1x .. N x).

Each /api/times-table-<n> lists n x 1 through n x 20. Computed, exact, and
handy for teaching. Contributes many small list-only APIs to the catalog.
"""
TABLES = 1000     # times-table-1 .. times-table-1000
ROWS = 20         # n x 1 .. n x 20

DATASETS = []
for _n in range(1, TABLES + 1):
    DATASETS.append({
        "meta": {
            "name": f"times-table-{_n}",
            "title": f"{_n} Times Table",
            "description": f"The multiplication table for {_n}: {_n}x1 through {_n}x{ROWS}.",
            "emoji": "✖️",
            "list_only": True,
            "family": True,
        },
        "items": [
            {"id": k, "multiplier": _n, "multiplicand": k, "product": _n * k,
             "expression": f"{_n} x {k} = {_n * k}"}
            for k in range(1, ROWS + 1)
        ],
    })
