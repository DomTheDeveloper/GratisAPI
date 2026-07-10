"""Calendar reference data: months and days of the week."""

META = {
    "name": "calendar",
    "title": "Calendar",
    "description": "Months of the year and days of the week with ordinal, length and abbreviation.",
    "emoji": "\U0001F4C5",
}

_MONTHS = [
    ("january", "January", 1, 31, "Jan", "Winter"),
    ("february", "February", 2, 28, "Feb", "Winter"),
    ("march", "March", 3, 31, "Mar", "Spring"),
    ("april", "April", 4, 30, "Apr", "Spring"),
    ("may", "May", 5, 31, "May", "Spring"),
    ("june", "June", 6, 30, "Jun", "Summer"),
    ("july", "July", 7, 31, "Jul", "Summer"),
    ("august", "August", 8, 31, "Aug", "Summer"),
    ("september", "September", 9, 30, "Sep", "Autumn"),
    ("october", "October", 10, 31, "Oct", "Autumn"),
    ("november", "November", 11, 30, "Nov", "Autumn"),
    ("december", "December", 12, 31, "Dec", "Winter"),
]

_DAYS = [
    ("monday", "Monday", 1, "Mon", False),
    ("tuesday", "Tuesday", 2, "Tue", False),
    ("wednesday", "Wednesday", 3, "Wed", False),
    ("thursday", "Thursday", 4, "Thu", False),
    ("friday", "Friday", 5, "Fri", False),
    ("saturday", "Saturday", 6, "Sat", True),
    ("sunday", "Sunday", 7, "Sun", True),
]

ITEMS = []
for cid, name, num, days, abbr, season in _MONTHS:
    ITEMS.append({
        "id": cid, "type": "month", "name": name, "number": num,
        "days": days, "abbreviation": abbr, "season_northern": season,
    })
for cid, name, num, abbr, weekend in _DAYS:
    ITEMS.append({
        "id": cid, "type": "weekday", "name": name, "number": num,
        "abbreviation": abbr, "is_weekend": weekend,
    })
