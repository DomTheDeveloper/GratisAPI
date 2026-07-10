"""Printable ASCII table (decimal 32-126)."""

import unicodedata

META = {
    "name": "ascii",
    "title": "Printable ASCII Table",
    "description": "The printable ASCII characters from decimal 32 to 126 with their numeric representations.",
    "emoji": "\U0001F524",
}


def _name(code):
    char = chr(code)
    try:
        return unicodedata.name(char).title()
    except ValueError:
        return None


ITEMS = [
    {
        "id": code,
        "decimal": code,
        "hex": "0x{:02X}".format(code),
        "octal": "0o{:03o}".format(code),
        "binary": format(code, "08b"),
        "character": chr(code),
        "description": _name(code),
    }
    for code in range(32, 127)
]
