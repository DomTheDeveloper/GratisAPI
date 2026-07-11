"""Per-year calendar APIs — one API per year, computed from the Gregorian rules.

Each /api/calendar-<year> lists the twelve months with their correct lengths
(February adjusts for leap years). Leap-year status and the weekday of Jan 1
are computed (Zeller's congruence), never fabricated.
"""
START_YEAR = 1600
END_YEAR = 2200

_MONTHS = [
    ("january", "January", 31), ("february", "February", 28),
    ("march", "March", 31), ("april", "April", 30), ("may", "May", 31),
    ("june", "June", 30), ("july", "July", 31), ("august", "August", 31),
    ("september", "September", 30), ("october", "October", 31),
    ("november", "November", 30), ("december", "December", 31),
]
_WEEKDAYS = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]


def _is_leap(y):
    return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)


def _weekday(y, m, d):
    # Zeller's congruence (Gregorian). Returns 0=Sunday .. 6=Saturday.
    if m < 3:
        m += 12
        y -= 1
    k, j = y % 100, y // 100
    h = (d + (13 * (m + 1)) // 5 + k + k // 4 + j // 4 + 5 * j) % 7
    return (h + 6) % 7  # convert Zeller (0=Sat) to 0=Sunday


assert _is_leap(2000) and not _is_leap(1900) and _is_leap(2024)
assert _WEEKDAYS[_weekday(2000, 1, 1)] == "Saturday"
assert _WEEKDAYS[_weekday(2024, 1, 1)] == "Monday"

DATASETS = []
for _y in range(START_YEAR, END_YEAR + 1):
    _leap = _is_leap(_y)
    _items = []
    for i, (mid, mname, mdays) in enumerate(_MONTHS, start=1):
        days = 29 if (mid == "february" and _leap) else mdays
        _items.append({
            "id": mid, "month": mname, "number": i, "days": days,
            "first_weekday": _WEEKDAYS[_weekday(_y, i, 1)],
        })
    DATASETS.append({
        "meta": {
            "name": f"calendar-{_y}",
            "title": f"Calendar {_y}",
            "description": (f"The {_y} calendar: {'a leap year' if _leap else 'a common year'} "
                           f"of {366 if _leap else 365} days, starting on a "
                           f"{_WEEKDAYS[_weekday(_y, 1, 1)]}."),
            "emoji": "\U0001F4C5",
            "list_only": True,
            "family": True,
        },
        "items": _items,
    })
