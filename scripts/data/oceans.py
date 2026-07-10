"""The five oceans of the world with area and depth statistics."""

META = {
    "name": "oceans",
    "title": "Oceans",
    "description": "The five oceans of the world with area, average and maximum depth.",
    "emoji": "\U0001F30A",
}

# id, name, area_km2, avg_depth_m, max_depth_m, deepest_point
_RAW = [
    ("pacific", "Pacific Ocean", 165250000, 4280, 10935, "Challenger Deep (Mariana Trench)"),
    ("atlantic", "Atlantic Ocean", 106460000, 3646, 8376, "Milwaukee Deep (Puerto Rico Trench)"),
    ("indian", "Indian Ocean", 70560000, 3741, 7290, "Java Trench (Sunda Trench)"),
    ("southern", "Southern Ocean", 21960000, 3270, 7434, "Factorian Deep (South Sandwich Trench)"),
    ("arctic", "Arctic Ocean", 15558000, 1205, 5550, "Molloy Deep (Fram Strait)"),
]

ITEMS = []
for oid, name, area, avg_d, max_d, deep in _RAW:
    ITEMS.append({
        "id": oid,
        "name": name,
        "area_km2": area,
        "avg_depth_m": avg_d,
        "max_depth_m": max_d,
        "deepest_point": deep,
    })
