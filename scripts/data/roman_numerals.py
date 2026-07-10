"""Roman numeral mappings for useful Arabic numbers."""

META = {
    "name": "roman_numerals",
    "title": "Roman Numerals",
    "description": "Roman numeral representations for a selection of useful Arabic numbers.",
    "emoji": "\U0001F3DB️",
}

# arabic, roman
_RAW = [
    (1, "I"),
    (2, "II"),
    (3, "III"),
    (4, "IV"),
    (5, "V"),
    (6, "VI"),
    (7, "VII"),
    (8, "VIII"),
    (9, "IX"),
    (10, "X"),
    (11, "XI"),
    (12, "XII"),
    (13, "XIII"),
    (14, "XIV"),
    (15, "XV"),
    (16, "XVI"),
    (17, "XVII"),
    (18, "XVIII"),
    (19, "XIX"),
    (20, "XX"),
    (30, "XXX"),
    (40, "XL"),
    (50, "L"),
    (90, "XC"),
    (100, "C"),
    (400, "CD"),
    (500, "D"),
    (900, "CM"),
    (1000, "M"),
    (1984, "MCMLXXXIV"),
    (2000, "MM"),
    (2024, "MMXXIV"),
    (2025, "MMXXV"),
]

ITEMS = [
    {"id": arabic, "arabic": arabic, "roman": roman}
    for arabic, roman in _RAW
]
