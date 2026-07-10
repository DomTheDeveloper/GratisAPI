"""ISO 216 A-series and B-series paper sizes."""

META = {
    "name": "paper-sizes",
    "title": "Paper Sizes",
    "description": "ISO 216 A-series and B-series paper sizes with dimensions in millimetres.",
    "emoji": "📄",
}

# name, series, width_mm, height_mm
_RAW = [
    ("A0", "A", 841, 1189),
    ("A1", "A", 594, 841),
    ("A2", "A", 420, 594),
    ("A3", "A", 297, 420),
    ("A4", "A", 210, 297),
    ("A5", "A", 148, 210),
    ("A6", "A", 105, 148),
    ("A7", "A", 74, 105),
    ("A8", "A", 52, 74),
    ("A9", "A", 37, 52),
    ("A10", "A", 26, 37),
    ("B0", "B", 1000, 1414),
    ("B1", "B", 707, 1000),
    ("B2", "B", 500, 707),
    ("B3", "B", 353, 500),
    ("B4", "B", 250, 353),
    ("B5", "B", 176, 250),
    ("B6", "B", 125, 176),
    ("B7", "B", 88, 125),
    ("B8", "B", 62, 88),
    ("B9", "B", 44, 62),
    ("B10", "B", 31, 44),
]

ITEMS = [
    {
        "id": name,
        "name": name,
        "series": series,
        "width_mm": w,
        "height_mm": h,
    }
    for name, series, w, h in _RAW
]
