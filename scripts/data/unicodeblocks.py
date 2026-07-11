"""Unicode block APIs — one API per well-known Unicode block.

Characters, names and categories come from Python's `unicodedata`, so every
record is real Unicode data, not fabricated. Large blocks (CJK, Hangul, ...)
are capped to keep the JSON small; the index notes when it's a partial view.
"""
import unicodedata

CAP = 256  # max records per block

# (block name, start, end) for blocks with well-established ranges.
_BLOCKS = [
    ("Basic Latin", 0x0000, 0x007F),
    ("Latin-1 Supplement", 0x0080, 0x00FF),
    ("Latin Extended-A", 0x0100, 0x017F),
    ("Latin Extended-B", 0x0180, 0x024F),
    ("IPA Extensions", 0x0250, 0x02AF),
    ("Spacing Modifier Letters", 0x02B0, 0x02FF),
    ("Combining Diacritical Marks", 0x0300, 0x036F),
    ("Greek and Coptic", 0x0370, 0x03FF),
    ("Cyrillic", 0x0400, 0x04FF),
    ("Cyrillic Supplement", 0x0500, 0x052F),
    ("Armenian", 0x0530, 0x058F),
    ("Hebrew", 0x0590, 0x05FF),
    ("Arabic", 0x0600, 0x06FF),
    ("Syriac", 0x0700, 0x074F),
    ("Thaana", 0x0780, 0x07BF),
    ("Devanagari", 0x0900, 0x097F),
    ("Bengali", 0x0980, 0x09FF),
    ("Gurmukhi", 0x0A00, 0x0A7F),
    ("Gujarati", 0x0A80, 0x0AFF),
    ("Oriya", 0x0B00, 0x0B7F),
    ("Tamil", 0x0B80, 0x0BFF),
    ("Telugu", 0x0C00, 0x0C7F),
    ("Kannada", 0x0C80, 0x0CFF),
    ("Malayalam", 0x0D00, 0x0D7F),
    ("Sinhala", 0x0D80, 0x0DFF),
    ("Thai", 0x0E00, 0x0E7F),
    ("Lao", 0x0E80, 0x0EFF),
    ("Tibetan", 0x0F00, 0x0FFF),
    ("Myanmar", 0x1000, 0x109F),
    ("Georgian", 0x10A0, 0x10FF),
    ("Hangul Jamo", 0x1100, 0x11FF),
    ("Ethiopic", 0x1200, 0x137F),
    ("Cherokee", 0x13A0, 0x13FF),
    ("Ogham", 0x1680, 0x169F),
    ("Runic", 0x16A0, 0x16FF),
    ("Khmer", 0x1780, 0x17FF),
    ("Mongolian", 0x1800, 0x18AF),
    ("Latin Extended Additional", 0x1E00, 0x1EFF),
    ("Greek Extended", 0x1F00, 0x1FFF),
    ("General Punctuation", 0x2000, 0x206F),
    ("Superscripts and Subscripts", 0x2070, 0x209F),
    ("Currency Symbols", 0x20A0, 0x20CF),
    ("Letterlike Symbols", 0x2100, 0x214F),
    ("Number Forms", 0x2150, 0x218F),
    ("Arrows", 0x2190, 0x21FF),
    ("Mathematical Operators", 0x2200, 0x22FF),
    ("Miscellaneous Technical", 0x2300, 0x23FF),
    ("Control Pictures", 0x2400, 0x243F),
    ("Enclosed Alphanumerics", 0x2460, 0x24FF),
    ("Box Drawing", 0x2500, 0x257F),
    ("Block Elements", 0x2580, 0x259F),
    ("Geometric Shapes", 0x25A0, 0x25FF),
    ("Miscellaneous Symbols", 0x2600, 0x26FF),
    ("Dingbats", 0x2700, 0x27BF),
    ("Braille Patterns", 0x2800, 0x28FF),
    ("CJK Symbols and Punctuation", 0x3000, 0x303F),
    ("Hiragana", 0x3040, 0x309F),
    ("Katakana", 0x30A0, 0x30FF),
    ("Bopomofo", 0x3100, 0x312F),
    ("Hangul Compatibility Jamo", 0x3130, 0x318F),
    ("CJK Unified Ideographs", 0x4E00, 0x9FFF),
    ("Hangul Syllables", 0xAC00, 0xD7A3),
    ("Alphabetic Presentation Forms", 0xFB00, 0xFB4F),
    ("Halfwidth and Fullwidth Forms", 0xFF00, 0xFFEF),
    ("Mahjong Tiles", 0x1F000, 0x1F02F),
    ("Domino Tiles", 0x1F030, 0x1F09F),
    ("Playing Cards", 0x1F0A0, 0x1F0FF),
    ("Enclosed Alphanumeric Supplement", 0x1F100, 0x1F1FF),
    ("Miscellaneous Symbols and Pictographs", 0x1F300, 0x1F5FF),
    ("Emoticons", 0x1F600, 0x1F64F),
    ("Transport and Map Symbols", 0x1F680, 0x1F6FF),
    ("Alchemical Symbols", 0x1F700, 0x1F77F),
    ("Geometric Shapes Extended", 0x1F780, 0x1F7FF),
    ("Supplemental Arrows-C", 0x1F800, 0x1F8FF),
    ("Supplemental Symbols and Pictographs", 0x1F900, 0x1F9FF),
    ("Chess Symbols", 0x1FA00, 0x1FA6F),
    ("Symbols and Pictographs Extended-A", 0x1FA70, 0x1FAFF),
    ("Mathematical Alphanumeric Symbols", 0x1D400, 0x1D7FF),
    ("Musical Symbols", 0x1D100, 0x1D1FF),
]


def _slug(name):
    out = []
    for ch in name.lower():
        out.append(ch if ch.isalnum() else "-")
    s = "".join(out)
    while "--" in s:
        s = s.replace("--", "-")
    return "unicode-" + s.strip("-")


DATASETS = []
for _name, _start, _end in _BLOCKS:
    _items = []
    _total = 0
    for _cp in range(_start, _end + 1):
        _ch = chr(_cp)
        _cname = unicodedata.name(_ch, None)
        if not _cname:
            continue
        _total += 1
        if len(_items) < CAP:
            _items.append({
                "id": "u" + format(_cp, "04X"),
                "codepoint": _cp,
                "hex": "U+" + format(_cp, "04X"),
                "char": _ch,
                "name": _cname,
                "category": unicodedata.category(_ch),
            })
    if not _items:
        continue
    _partial = _total > len(_items)
    _desc = f"The {_name} Unicode block (U+{_start:04X}..U+{_end:04X})"
    if _partial:
        _desc += f" — first {len(_items)} of {_total} named characters"
    DATASETS.append({
        "meta": {
            "name": _slug(_name),
            "title": _name,
            "description": _desc + ".",
            "emoji": "\U0001F524",
            "list_only": True,
            "family": True,
        },
        "items": _items,
    })
