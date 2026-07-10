"""The Saffir-Simpson hurricane wind scale."""

META = {
    "name": "saffir-simpson",
    "title": "Saffir-Simpson Scale",
    "description": "Hurricane wind categories with wind speeds, damage, and storm surge.",
    "emoji": "\U0001F32A",
}

# id, category, wind_kmh_min, wind_kmh_max, damage, storm_surge_m
_RAW = [
    ("tropical-depression", "Tropical Depression", 0, 62,
     "No significant damage; heavy rain and flooding possible.", None),
    ("tropical-storm", "Tropical Storm", 63, 118,
     "Minor damage to trees and unanchored objects.", None),
    ("category-1", "Category 1", 119, 153,
     "Very dangerous winds; damage to roofs, siding, and trees.", 1.5),
    ("category-2", "Category 2", 154, 177,
     "Extremely dangerous winds; major roof and siding damage.", 2.5),
    ("category-3", "Category 3", 178, 208,
     "Devastating damage; well-built homes may lose roof decking.", 3.5),
    ("category-4", "Category 4", 209, 251,
     "Catastrophic damage; severe damage to walls and roofs.", 5.5),
    ("category-5", "Category 5", 252, None,
     "Catastrophic damage; a high percentage of homes destroyed.", 6.0),
]

ITEMS = [
    {
        "id": r[0],
        "category": r[1],
        "wind_kmh_min": r[2],
        "wind_kmh_max": r[3],
        "damage": r[4],
        "storm_surge_m": r[5],
    }
    for r in _RAW
]
