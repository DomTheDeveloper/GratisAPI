"""The pH scale with example substances."""

META = {
    "name": "ph-scale",
    "title": "pH Scale",
    "description": "The pH scale from 0 to 14 with an example substance at each value.",
    "emoji": "\U0001F9EA",
}

# id, ph, type, example
_RAW = [
    (0, 0, "Acidic", "Battery acid"),
    (1, 1, "Acidic", "Stomach acid"),
    (2, 2, "Acidic", "Lemon juice"),
    (3, 3, "Acidic", "Vinegar"),
    (4, 4, "Acidic", "Tomato juice"),
    (5, 5, "Acidic", "Black coffee"),
    (6, 6, "Acidic", "Milk"),
    (7, 7, "Neutral", "Pure water"),
    (8, 8, "Basic", "Sea water"),
    (9, 9, "Basic", "Baking soda solution"),
    (10, 10, "Basic", "Milk of magnesia"),
    (11, 11, "Basic", "Ammonia solution"),
    (12, 12, "Basic", "Soapy water"),
    (13, 13, "Basic", "Bleach"),
    (14, 14, "Basic", "Liquid drain cleaner"),
]

ITEMS = [
    {
        "id": r[0],
        "ph": r[1],
        "type": r[2],
        "example": r[3],
    }
    for r in _RAW
]
