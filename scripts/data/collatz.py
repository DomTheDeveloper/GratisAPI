"""Collatz (hailstone) sequence APIs — one API per starting integer N.

/api/collatz-<n> gives the full Collatz sequence from N to 1 (n/2 if even,
3n+1 if odd). Every step is computed; the peak and length are noted.
"""
COUNT = 1000   # collatz-1 .. collatz-1000


def _collatz(n):
    seq = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        seq.append(n)
    return seq


assert _collatz(6) == [6, 3, 10, 5, 16, 8, 4, 2, 1]

DATASETS = []
for _n in range(1, COUNT + 1):
    _seq = _collatz(_n)
    DATASETS.append({
        "meta": {
            "name": f"collatz-{_n}",
            "title": f"Collatz Sequence of {_n}",
            "description": (f"The Collatz (3n+1) sequence starting at {_n}: {len(_seq) - 1} "
                            f"steps to reach 1, peaking at {max(_seq)}."),
            "emoji": "\U0001F300", "list_only": True, "family": True,
        },
        "items": [{"id": i, "step": i, "value": v} for i, v in enumerate(_seq)],
    })
