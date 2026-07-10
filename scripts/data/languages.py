"""Human languages (ISO 639-1 subset)."""

META = {
    "name": "languages",
    "title": "Languages",
    "description": "Human languages with ISO 639-1 code, native name and writing direction.",
    "emoji": "\U0001F5E3️",
}

# code, name, native_name, direction, speakers_millions
_RAW = [
    ("en", "English", "English", "ltr", 1456),
    ("zh", "Chinese", "中文", "ltr", 1138),
    ("hi", "Hindi", "हिन्दी", "ltr", 609),
    ("es", "Spanish", "Español", "ltr", 559),
    ("ar", "Arabic", "العربية", "rtl", 422),
    ("fr", "French", "Français", "ltr", 310),
    ("bn", "Bengali", "বাংলা", "ltr", 284),
    ("pt", "Portuguese", "Português", "ltr", 264),
    ("ru", "Russian", "Русский", "ltr", 255),
    ("ur", "Urdu", "اردو", "rtl", 232),
    ("id", "Indonesian", "Bahasa Indonesia", "ltr", 199),
    ("de", "German", "Deutsch", "ltr", 134),
    ("ja", "Japanese", "日本語", "ltr", 125),
    ("sw", "Swahili", "Kiswahili", "ltr", 87),
    ("ko", "Korean", "한국어", "ltr", 81),
    ("it", "Italian", "Italiano", "ltr", 68),
    ("tr", "Turkish", "Türkçe", "ltr", 88),
    ("fa", "Persian", "فارسی", "rtl", 79),
    ("he", "Hebrew", "עברית", "rtl", 9),
    ("nl", "Dutch", "Nederlands", "ltr", 25),
    ("pl", "Polish", "Polski", "ltr", 41),
    ("th", "Thai", "ไทย", "ltr", 61),
    ("vi", "Vietnamese", "Tiếng Việt", "ltr", 85),
    ("el", "Greek", "Ελληνικά", "ltr", 13),
    ("sv", "Swedish", "Svenska", "ltr", 10),
]

ITEMS = [
    {"id": code, "code": code, "name": name, "native_name": native,
     "direction": direction, "speakers_millions": speakers}
    for code, name, native, direction, speakers in _RAW
]
