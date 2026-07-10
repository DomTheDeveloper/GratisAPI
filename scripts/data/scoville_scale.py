"""Scoville heat scale for peppers, hot sauces, and extracts."""

META = {
    "name": "scoville-scale",
    "title": "Scoville Scale",
    "description": "Peppers, hot sauces, and extracts ranked by Scoville heat units (SHU).",
    "emoji": "\U0001F336",
}

# name, scoville_min, scoville_max, type
_RAW = [
    ("Bell Pepper", 0, 0, "Pepper"),
    ("Pepperoncini", 100, 500, "Pepper"),
    ("Poblano", 1000, 2000, "Pepper"),
    ("Sriracha Sauce", 1000, 2500, "Sauce"),
    ("Tabasco Sauce", 2500, 5000, "Sauce"),
    ("Jalapeno", 2500, 8000, "Pepper"),
    ("Chipotle", 2500, 8000, "Pepper"),
    ("Serrano", 10000, 23000, "Pepper"),
    ("Cayenne", 30000, 50000, "Pepper"),
    ("Tabasco Pepper", 30000, 50000, "Pepper"),
    ("Thai Pepper", 50000, 100000, "Pepper"),
    ("Habanero", 100000, 350000, "Pepper"),
    ("Scotch Bonnet", 100000, 350000, "Pepper"),
    ("Ghost Pepper (Bhut Jolokia)", 855000, 1041427, "Pepper"),
    ("Trinidad Scorpion", 1200000, 2000000, "Pepper"),
    ("Carolina Reaper", 1400000, 2200000, "Pepper"),
    ("Pepper X", 2693000, 2693000, "Pepper"),
    ("Dave's Insanity Sauce", 180000, 180000, "Sauce"),
    ("Blair's 16 Million Reserve", 16000000, 16000000, "Extract"),
    ("Pure Capsaicin", 16000000, 16000000, "Extract"),
]

ITEMS = [
    {
        "id": i + 1,
        "name": name,
        "scoville_min": lo,
        "scoville_max": hi,
        "type": kind,
    }
    for i, (name, lo, hi, kind) in enumerate(_RAW)
]
