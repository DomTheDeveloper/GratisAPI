"""The Enhanced Fujita tornado intensity scale."""

META = {
    "name": "fujita-scale",
    "title": "Enhanced Fujita Scale",
    "description": "Tornado intensity ratings EF0 to EF5 with wind speeds and damage.",
    "emoji": "\U0001F32A",
}

# id, scale, wind_kmh_min, wind_kmh_max, damage_description
_RAW = [
    ("ef0", "EF0", 105, 137, "Minor damage; peeled roof surfaces, broken tree branches."),
    ("ef1", "EF1", 138, 177, "Moderate damage; roofs stripped, mobile homes overturned."),
    ("ef2", "EF2", 178, 217, "Considerable damage; roofs torn off, large trees snapped."),
    ("ef3", "EF3", 218, 266, "Severe damage; entire stories of well-built houses destroyed."),
    ("ef4", "EF4", 267, 322, "Devastating damage; well-built houses leveled."),
    ("ef5", "EF5", 323, None, "Incredible damage; strong houses swept away, cars thrown far."),
]

ITEMS = [
    {
        "id": r[0],
        "scale": r[1],
        "wind_kmh_min": r[2],
        "wind_kmh_max": r[3],
        "damage_description": r[4],
    }
    for r in _RAW
]
