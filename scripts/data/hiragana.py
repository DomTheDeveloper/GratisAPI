"""The 46 basic hiragana characters of the Japanese syllabary."""

META = {
    "name": "hiragana",
    "title": "Hiragana",
    "description": "The 46 basic hiragana characters of the Japanese syllabary with romaji.",
    "emoji": "\U0001F1EF\U0001F1F5",
}

# romaji, character, vowel_row, consonant_group
_RAW = [
    ("a", "あ", "a", ""), ("i", "い", "i", ""), ("u", "う", "u", ""), ("e", "え", "e", ""), ("o", "お", "o", ""),
    ("ka", "か", "a", "k"), ("ki", "き", "i", "k"), ("ku", "く", "u", "k"), ("ke", "け", "e", "k"), ("ko", "こ", "o", "k"),
    ("sa", "さ", "a", "s"), ("shi", "し", "i", "s"), ("su", "す", "u", "s"), ("se", "せ", "e", "s"), ("so", "そ", "o", "s"),
    ("ta", "た", "a", "t"), ("chi", "ち", "i", "t"), ("tsu", "つ", "u", "t"), ("te", "て", "e", "t"), ("to", "と", "o", "t"),
    ("na", "な", "a", "n"), ("ni", "に", "i", "n"), ("nu", "ぬ", "u", "n"), ("ne", "ね", "e", "n"), ("no", "の", "o", "n"),
    ("ha", "は", "a", "h"), ("hi", "ひ", "i", "h"), ("fu", "ふ", "u", "h"), ("he", "へ", "e", "h"), ("ho", "ほ", "o", "h"),
    ("ma", "ま", "a", "m"), ("mi", "み", "i", "m"), ("mu", "む", "u", "m"), ("me", "め", "e", "m"), ("mo", "も", "o", "m"),
    ("ya", "や", "a", "y"), ("yu", "ゆ", "u", "y"), ("yo", "よ", "o", "y"),
    ("ra", "ら", "a", "r"), ("ri", "り", "i", "r"), ("ru", "る", "u", "r"), ("re", "れ", "e", "r"), ("ro", "ろ", "o", "r"),
    ("wa", "わ", "a", "w"), ("wo", "を", "o", "w"),
    ("n", "ん", "", ""),
]

ITEMS = [
    {"id": romaji, "character": char, "romaji": romaji,
     "vowel_row": vowel, "consonant_group": group}
    for romaji, char, vowel, group in _RAW
]
