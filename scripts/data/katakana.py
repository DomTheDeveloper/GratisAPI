"""The 46 basic katakana characters of the Japanese syllabary."""

META = {
    "name": "katakana",
    "title": "Katakana",
    "description": "The 46 basic katakana characters of the Japanese syllabary with romaji.",
    "emoji": "\U0001F1EF\U0001F1F5",
}

# romaji, character, vowel_row, consonant_group
_RAW = [
    ("a", "ア", "a", ""), ("i", "イ", "i", ""), ("u", "ウ", "u", ""), ("e", "エ", "e", ""), ("o", "オ", "o", ""),
    ("ka", "カ", "a", "k"), ("ki", "キ", "i", "k"), ("ku", "ク", "u", "k"), ("ke", "ケ", "e", "k"), ("ko", "コ", "o", "k"),
    ("sa", "サ", "a", "s"), ("shi", "シ", "i", "s"), ("su", "ス", "u", "s"), ("se", "セ", "e", "s"), ("so", "ソ", "o", "s"),
    ("ta", "タ", "a", "t"), ("chi", "チ", "i", "t"), ("tsu", "ツ", "u", "t"), ("te", "テ", "e", "t"), ("to", "ト", "o", "t"),
    ("na", "ナ", "a", "n"), ("ni", "ニ", "i", "n"), ("nu", "ヌ", "u", "n"), ("ne", "ネ", "e", "n"), ("no", "ノ", "o", "n"),
    ("ha", "ハ", "a", "h"), ("hi", "ヒ", "i", "h"), ("fu", "フ", "u", "h"), ("he", "ヘ", "e", "h"), ("ho", "ホ", "o", "h"),
    ("ma", "マ", "a", "m"), ("mi", "ミ", "i", "m"), ("mu", "ム", "u", "m"), ("me", "メ", "e", "m"), ("mo", "モ", "o", "m"),
    ("ya", "ヤ", "a", "y"), ("yu", "ユ", "u", "y"), ("yo", "ヨ", "o", "y"),
    ("ra", "ラ", "a", "r"), ("ri", "リ", "i", "r"), ("ru", "ル", "u", "r"), ("re", "レ", "e", "r"), ("ro", "ロ", "o", "r"),
    ("wa", "ワ", "a", "w"), ("wo", "ヲ", "o", "w"),
    ("n", "ン", "", ""),
]

ITEMS = [
    {"id": romaji, "character": char, "romaji": romaji,
     "vowel_row": vowel, "consonant_group": group}
    for romaji, char, vowel, group in _RAW
]
