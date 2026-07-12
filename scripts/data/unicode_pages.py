"""Unicode code-point page APIs — one API per 256-code-point page.

/api/unicode-page-<hex> lists every assigned, named code point in the page
U+<hex>00 .. U+<hex>FF, with its character, name and general category — all
straight from Python's `unicodedata`, so every record is real Unicode data.
Covers planes 0 (BMP) and 1 (SMP); pages with no named characters are skipped.
"""
import unicodedata

MAX_CP = 0x1FFFF  # planes 0 and 1

DATASETS = []
for _page in range(0, (MAX_CP >> 8) + 1):
    _start = _page << 8
    _items = []
    for _cp in range(_start, _start + 256):
        _ch = chr(_cp)
        _name = unicodedata.name(_ch, None)
        if not _name:
            continue
        _items.append({
            "id": "u" + format(_cp, "04X"),
            "codepoint": _cp,
            "hex": "U+" + format(_cp, "04X"),
            "char": _ch,
            "name": _name,
            "category": unicodedata.category(_ch),
        })
    if not _items:
        continue
    DATASETS.append({
        "meta": {
            "name": "unicode-page-" + format(_page, "02x"),
            "title": "Unicode Page U+" + format(_start, "04X"),
            "description": (f"The {len(_items)} named code points in U+{_start:04X}..U+{_start + 255:04X}."),
            "emoji": "\U0001F521", "list_only": True, "family": True,
        },
        "items": _items,
    })
