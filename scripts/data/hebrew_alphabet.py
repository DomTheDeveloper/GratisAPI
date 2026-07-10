"""The Hebrew alphabet: 22 letters with transliteration and gematria values."""

META = {
    "name": "hebrew_alphabet",
    "title": "Hebrew Alphabet",
    "description": "The 22 letters of the Hebrew alphabet with transliteration and numeric (gematria) value.",
    "emoji": "\U0001F1EE\U0001F1F1",
}

# name, letter, transliteration, numeric_value, order
_RAW = [
    ("alef", "א", "'", 1, 1),
    ("bet", "ב", "b", 2, 2),
    ("gimel", "ג", "g", 3, 3),
    ("dalet", "ד", "d", 4, 4),
    ("he", "ה", "h", 5, 5),
    ("vav", "ו", "v", 6, 6),
    ("zayin", "ז", "z", 7, 7),
    ("het", "ח", "kh", 8, 8),
    ("tet", "ט", "t", 9, 9),
    ("yod", "י", "y", 10, 10),
    ("kaf", "כ", "k", 20, 11),
    ("lamed", "ל", "l", 30, 12),
    ("mem", "מ", "m", 40, 13),
    ("nun", "נ", "n", 50, 14),
    ("samekh", "ס", "s", 60, 15),
    ("ayin", "ע", "'", 70, 16),
    ("pe", "פ", "p", 80, 17),
    ("tsadi", "צ", "ts", 90, 18),
    ("qof", "ק", "q", 100, 19),
    ("resh", "ר", "r", 200, 20),
    ("shin", "ש", "sh", 300, 21),
    ("tav", "ת", "t", 400, 22),
]

ITEMS = [
    {"id": name, "name": name.capitalize(), "letter": letter,
     "transliteration": translit, "numeric_value": numeric, "order": order}
    for name, letter, translit, numeric, order in _RAW
]
