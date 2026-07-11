"""Math sequence APIs — one API per famous integer sequence.

Every term is computed. Term counts are chosen so all values stay within the
exact-integer range (< 2^53), so the JSON numbers are precise everywhere,
including in JavaScript.
"""
import math

SAFE = 2 ** 53


def _first_primes(k):
    out, n = [], 2
    while len(out) < k:
        if all(n % p for p in out if p * p <= n):
            out.append(n)
        n += 1
    return out


def _fib():
    out, a, b = [], 0, 1
    while a < SAFE:
        out.append(a)
        a, b = b, a + b
    return out


def _lucas():
    out, a, b = [], 2, 1
    while a < SAFE:
        out.append(a)
        a, b = b, a + b
    return out


def _tribonacci():
    out, a, b, c = [], 0, 0, 1
    while a < SAFE:
        out.append(a)
        a, b, c = b, c, a + b + c
    return out


def _poly(fn, limit):
    return [fn(n) for n in range(1, limit + 1)]


def _factorials():
    out, f = [], 1
    n = 0
    while f < SAFE:
        out.append(f)
        n += 1
        f *= n
    return out


def _powers(base, cap=SAFE):
    out, v = [], 1
    while v < cap:
        out.append(v)
        v *= base
    return out


def _catalan():
    out, c, n = [], 1, 0
    while c < SAFE:
        out.append(c)
        n += 1
        c = c * 2 * (2 * n - 1) // (n + 1)
    return out


def _perfect_numbers():
    # Even perfect numbers via Mersenne primes (Euclid–Euler), within range.
    out = []
    for p in (2, 3, 5, 7, 13, 17, 19, 31):
        mp = (1 << p) - 1
        if all(mp % d for d in range(2, int(mp ** 0.5) + 1)):
            perfect = (1 << (p - 1)) * mp
            if perfect < SAFE:
                out.append(perfect)
    return out


def _sieve_upto(limit):
    s = bytearray([1]) * (limit + 1)
    s[0] = s[1] = 0
    for i in range(2, int(limit ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(range(i * i, limit + 1, i)))
    return s


def _num_divisors(n):
    if n < 2:
        return 1 if n == 1 else 0
    total, d = 1, 2
    m = n
    while d * d <= m:
        if m % d == 0:
            e = 0
            while m % d == 0:
                m //= d
                e += 1
            total *= (e + 1)
        d += 1 if d == 2 else 2
    if m > 1:
        total *= 2
    return total


def _sigma(n):
    total, d = 0, 1
    while d * d <= n:
        if n % d == 0:
            total += d
            if d != n // d:
                total += n // d
        d += 1
    return total


def _is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(c) ** 2 for c in str(n))
    return n == 1


def _first(pred, k):
    out, n = [], 1
    while len(out) < k:
        if pred(n):
            out.append(n)
        n += 1
    return out


def _happy(k):
    return _first(_is_happy, k)


def _abundant(k):
    return _first(lambda n: _sigma(n) - n > n, k)


def _deficient(k):
    return _first(lambda n: _sigma(n) - n < n, k)


def _palindromic(k):
    return _first(lambda n: str(n) == str(n)[::-1], k)


def _highly_composite(k):
    out, best = [], 0
    n = 1
    while len(out) < k:
        d = _num_divisors(n)
        if d > best:
            best = d
            out.append(n)
        n += 1
    return out


# name, title, emoji, description, list-of-terms
_SEQUENCES = [
    ("primes", "Prime Numbers", "The first 1,000 prime numbers.", _first_primes(1000)),
    ("fibonacci", "Fibonacci Numbers", "The Fibonacci sequence within exact-integer range.", _fib()),
    ("lucas-numbers", "Lucas Numbers", "The Lucas sequence within exact-integer range.", _lucas()),
    ("tribonacci-numbers", "Tribonacci Numbers", "The Tribonacci sequence within exact-integer range.", _tribonacci()),
    ("square-numbers", "Square Numbers", "Perfect squares n^2 for n = 1..1000.", _poly(lambda n: n * n, 1000)),
    ("cube-numbers", "Cube Numbers", "Perfect cubes n^3 for n = 1..200.", _poly(lambda n: n ** 3, 200)),
    ("fourth-powers", "Fourth Powers", "n^4 for n = 1..100.", _poly(lambda n: n ** 4, 100)),
    ("fifth-powers", "Fifth Powers", "n^5 for n = 1..80.", _poly(lambda n: n ** 5, 80)),
    ("triangular-numbers", "Triangular Numbers", "n(n+1)/2 for n = 1..1000.", _poly(lambda n: n * (n + 1) // 2, 1000)),
    ("tetrahedral-numbers", "Tetrahedral Numbers", "n(n+1)(n+2)/6 for n = 1..500.", _poly(lambda n: n * (n + 1) * (n + 2) // 6, 500)),
    ("square-pyramidal-numbers", "Square Pyramidal Numbers", "n(n+1)(2n+1)/6 for n = 1..500.", _poly(lambda n: n * (n + 1) * (2 * n + 1) // 6, 500)),
    ("pentagonal-numbers", "Pentagonal Numbers", "n(3n-1)/2 for n = 1..1000.", _poly(lambda n: n * (3 * n - 1) // 2, 1000)),
    ("hexagonal-numbers", "Hexagonal Numbers", "n(2n-1) for n = 1..1000.", _poly(lambda n: n * (2 * n - 1), 1000)),
    ("heptagonal-numbers", "Heptagonal Numbers", "n(5n-3)/2 for n = 1..1000.", _poly(lambda n: n * (5 * n - 3) // 2, 1000)),
    ("octagonal-numbers", "Octagonal Numbers", "n(3n-2) for n = 1..1000.", _poly(lambda n: n * (3 * n - 2), 1000)),
    ("factorials", "Factorials", "n! within exact-integer range.", _factorials()),
    ("powers-of-two", "Powers of Two", "2^n within exact-integer range.", _powers(2)),
    ("powers-of-three", "Powers of Three", "3^n within exact-integer range.", _powers(3)),
    ("powers-of-ten", "Powers of Ten", "10^n within exact-integer range.", _powers(10)),
    ("catalan-numbers", "Catalan Numbers", "The Catalan numbers within exact-integer range.", _catalan()),
    ("perfect-numbers", "Perfect Numbers", "Numbers equal to the sum of their proper divisors.", _perfect_numbers()),
    ("happy-numbers", "Happy Numbers", "The first 200 happy numbers.", _happy(200)),
    ("abundant-numbers", "Abundant Numbers", "The first 200 abundant numbers.", _abundant(200)),
    ("deficient-numbers", "Deficient Numbers", "The first 300 deficient numbers.", _deficient(300)),
    ("palindromic-numbers", "Palindromic Numbers", "The first 300 palindromic numbers.", _palindromic(300)),
    ("highly-composite-numbers", "Highly Composite Numbers", "Numbers with more divisors than any smaller number.", _highly_composite(30)),
    ("even-numbers", "Even Numbers", "The first 1,000 even numbers.", [2 * n for n in range(1, 1001)]),
    ("odd-numbers", "Odd Numbers", "The first 1,000 odd numbers.", [2 * n - 1 for n in range(1, 1001)]),
    ("mersenne-numbers", "Mersenne Numbers", "2^n - 1 within exact-integer range.", [(1 << n) - 1 for n in range(1, 53)]),
]

# Sanity checks.
assert _first_primes(5) == [2, 3, 5, 7, 11]
assert _fib()[:8] == [0, 1, 1, 2, 3, 5, 8, 13]
assert _perfect_numbers()[:4] == [6, 28, 496, 8128]

DATASETS = []
for _name, _title, _desc, _terms in _SEQUENCES:
    DATASETS.append({
        "meta": {
            "name": _name, "title": _title, "description": _desc,
            "emoji": "\U0001F9EE", "list_only": True, "family": True,
        },
        "items": [{"id": i, "index": i + 1, "value": v} for i, v in enumerate(_terms)],
    })
