"""The modern Russian Cyrillic alphabet: 33 letters with transliteration."""

META = {
    "name": "cyrillic_alphabet",
    "title": "Cyrillic Alphabet",
    "description": "The 33 letters of the modern Russian Cyrillic alphabet with transliteration and sound.",
    "emoji": "\U0001F1F7\U0001F1FA",
}

# name, uppercase, lowercase, transliteration, sound, order
_RAW = [
    ("a", "А", "а", "a", "a as in father", 1),
    ("be", "Б", "б", "b", "b as in bad", 2),
    ("ve", "В", "в", "v", "v as in van", 3),
    ("ge", "Г", "г", "g", "g as in go", 4),
    ("de", "Д", "д", "d", "d as in do", 5),
    ("ye", "Е", "е", "ye", "ye as in yes", 6),
    ("yo", "Ё", "ё", "yo", "yo as in yonder", 7),
    ("zhe", "Ж", "ж", "zh", "s as in measure", 8),
    ("ze", "З", "з", "z", "z as in zoo", 9),
    ("i", "И", "и", "i", "ee as in meet", 10),
    ("i_kratkoye", "Й", "й", "y", "y as in boy", 11),
    ("ka", "К", "к", "k", "k as in kept", 12),
    ("el", "Л", "л", "l", "l as in lamp", 13),
    ("em", "М", "м", "m", "m as in map", 14),
    ("en", "Н", "н", "n", "n as in not", 15),
    ("o", "О", "о", "o", "o as in more", 16),
    ("pe", "П", "п", "p", "p as in pet", 17),
    ("er", "Р", "р", "r", "rolled r", 18),
    ("es", "С", "с", "s", "s as in see", 19),
    ("te", "Т", "т", "t", "t as in top", 20),
    ("u", "У", "у", "u", "oo as in boot", 21),
    ("ef", "Ф", "ф", "f", "f as in face", 22),
    ("ha", "Х", "х", "kh", "ch as in Scottish loch", 23),
    ("tse", "Ц", "ц", "ts", "ts as in sits", 24),
    ("che", "Ч", "ч", "ch", "ch as in check", 25),
    ("sha", "Ш", "ш", "sh", "sh as in shop", 26),
    ("shcha", "Щ", "щ", "shch", "soft sh as in fresh cheese", 27),
    ("tvyordy_znak", "Ъ", "ъ", "″", "hard sign (silent)", 28),
    ("y", "Ы", "ы", "y", "i as in ill (back)", 29),
    ("myagky_znak", "Ь", "ь", "'", "soft sign (silent)", 30),
    ("e", "Э", "э", "e", "e as in met", 31),
    ("yu", "Ю", "ю", "yu", "yu as in universe", 32),
    ("ya", "Я", "я", "ya", "ya as in yard", 33),
]

ITEMS = [
    {"id": name, "name": name.replace("_", " ").title(), "uppercase": upper,
     "lowercase": lower, "transliteration": translit, "sound": sound, "order": order}
    for name, upper, lower, translit, sound, order in _RAW
]
