"""The Beaufort wind force scale."""

META = {
    "name": "beaufort-scale",
    "title": "Beaufort Scale",
    "description": "The Beaufort wind force scale from 0 (calm) to 12 (hurricane).",
    "emoji": "\U0001F4A8",
}

# force, description, wind_kmh_min, wind_kmh_max, sea/land conditions
_RAW = [
    (0, "Calm", 0, 1, "Smoke rises vertically; sea like a mirror."),
    (1, "Light air", 1, 5, "Smoke drifts; ripples on the water."),
    (2, "Light breeze", 6, 11, "Leaves rustle; small wavelets."),
    (3, "Gentle breeze", 12, 19, "Leaves and twigs in motion; large wavelets."),
    (4, "Moderate breeze", 20, 28, "Dust and loose paper raised; small waves."),
    (5, "Fresh breeze", 29, 38, "Small trees sway; moderate waves with whitecaps."),
    (6, "Strong breeze", 39, 49, "Large branches move; large waves, some spray."),
    (7, "Near gale", 50, 61, "Whole trees in motion; sea heaps up, foam streaks."),
    (8, "Gale", 62, 74, "Twigs break off trees; moderately high waves."),
    (9, "Strong gale", 75, 88, "Slight structural damage; high waves, dense foam."),
    (10, "Storm", 89, 102, "Trees uprooted; very high waves, sea white with foam."),
    (11, "Violent storm", 103, 117, "Widespread damage; exceptionally high waves."),
    (12, "Hurricane force", 118, None, "Devastation; air filled with foam and spray."),
]

ITEMS = [
    {
        "id": force,
        "force": force,
        "description": desc,
        "wind_kmh_min": lo,
        "wind_kmh_max": hi,
        "conditions": cond,
    }
    for force, desc, lo, hi, cond in _RAW
]
