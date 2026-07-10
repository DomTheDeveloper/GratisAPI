"""Common cooking measurement units and conversions (US customary and metric)."""

META = {
    "name": "cooking-measurements",
    "title": "Cooking Measurements",
    "description": "Common cooking measurement units with volume (ml) and weight (g) conversions.",
    "emoji": "🥄",
}

# unit, abbreviation, type, milliliters, grams, note
_RAW = [
    ("Pinch", "pinch", "Volume", 0.31, None, "About 1/16 teaspoon."),
    ("Dash", "dash", "Volume", 0.62, None, "About 1/8 teaspoon."),
    ("Teaspoon", "tsp", "Volume", 4.93, None, "US teaspoon; often rounded to 5 ml."),
    ("Tablespoon", "tbsp", "Volume", 14.79, None, "US tablespoon; equals 3 teaspoons."),
    ("Fluid Ounce", "fl oz", "Volume", 29.57, None, "US fluid ounce; equals 2 tablespoons."),
    ("Cup", "c", "Volume", 236.59, None, "US cup; equals 8 fluid ounces."),
    ("Pint", "pt", "Volume", 473.18, None, "US pint; equals 2 cups."),
    ("Quart", "qt", "Volume", 946.35, None, "US quart; equals 2 pints."),
    ("Gallon", "gal", "Volume", 3785.41, None, "US gallon; equals 4 quarts."),
    ("Milliliter", "ml", "Volume", 1.0, None, "Metric base unit of volume for cooking."),
    ("Deciliter", "dl", "Volume", 100.0, None, "Equals 100 milliliters."),
    ("Liter", "l", "Volume", 1000.0, None, "Equals 1000 milliliters."),
    ("Milligram", "mg", "Weight", None, 0.001, "Equals 1/1000 of a gram."),
    ("Gram", "g", "Weight", None, 1.0, "Metric base unit of weight for cooking."),
    ("Kilogram", "kg", "Weight", None, 1000.0, "Equals 1000 grams."),
    ("Ounce", "oz", "Weight", None, 28.35, "Avoirdupois ounce of weight."),
    ("Pound", "lb", "Weight", None, 453.59, "Equals 16 ounces."),
    ("Stick of Butter", "stick", "Weight", None, 113.4, "US stick of butter; equals 1/2 cup or 8 tablespoons."),
    ("Metric Cup", "cup", "Volume", 250.0, None, "Metric cup used in Australia and parts of Europe."),
    ("Metric Tablespoon", "tbsp", "Volume", 15.0, None, "Metric tablespoon; equals 15 ml."),
]

ITEMS = [
    {
        "id": i + 1,
        "unit": unit,
        "abbreviation": abbr,
        "type": kind,
        "milliliters": ml,
        "grams": g,
        "note": note,
    }
    for i, (unit, abbr, kind, ml, g, note) in enumerate(_RAW)
]
