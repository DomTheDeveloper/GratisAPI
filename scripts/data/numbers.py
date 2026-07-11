"""The numbers API: computed integer facts for 0 .. 999,999.

One million records, every value computed (never fabricated): parity,
primality (sieve of Eratosthenes), perfect squares and hexadecimal. Served
paginated so the generator emits ~100 page files plus individual endpoints for
the first 1,000 integers, instead of a million separate files.
"""
import math

N = 1_000_000

# Sieve of Eratosthenes over [0, N).
_sieve = bytearray([1]) * N
_sieve[0] = 0
_sieve[1] = 0
for _i in range(2, int(N ** 0.5) + 1):
    if _sieve[_i]:
        _sieve[_i * _i::_i] = bytearray(len(range(_i * _i, N, _i)))


def _record(n):
    root = math.isqrt(n)
    return {
        "id": n,
        "is_even": n % 2 == 0,
        "is_prime": bool(_sieve[n]),
        "is_perfect_square": root * root == n,
        "hexadecimal": hex(n),
    }


class _Numbers:
    """Lazy, re-iterable sequence of a million number records."""

    def __len__(self):
        return N

    def __iter__(self):
        for n in range(N):
            yield _record(n)


# Sanity checks — cheap, and they guard against a broken sieve.
assert _record(7)["is_prime"] and not _record(8)["is_prime"]
assert _record(9)["is_perfect_square"] and not _record(10)["is_perfect_square"]
assert _record(255)["hexadecimal"] == "0xff"

META = {
    "name": "numbers",
    "title": "Numbers",
    "description": "Computed facts for every integer from 0 to 999,999: parity, primality, perfect squares and hexadecimal.",
    "emoji": "\U0001F522",
    "paginated": True,
    "page_size": 10000,
    "individual_cap": 1000,
}

ITEMS = _Numbers()
