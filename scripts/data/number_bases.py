"""Common numeral systems and positional number bases."""

META = {
    "name": "number-bases",
    "title": "Number Bases",
    "description": "Common numeral systems and positional number bases with their digit sets.",
    "emoji": "🔢",
}

# name, base, digits, common_use
_RAW = [
    ("Binary", 2, "01",
     "Digital electronics and computer memory; the native language of computers."),
    ("Ternary", 3, "012",
     "Balanced ternary computing and some theoretical computer science."),
    ("Quaternary", 4, "0123",
     "Genetics (DNA base pairs) and some digital signalling."),
    ("Quinary", 5, "01234",
     "Some tally and abacus systems; historical counting."),
    ("Senary", 6, "012345",
     "Dice games and some counting systems."),
    ("Octal", 8, "01234567",
     "Unix file permissions and older computing systems."),
    ("Decimal", 10, "0123456789",
     "Everyday human arithmetic and the standard number system."),
    ("Duodecimal", 12, "0123456789AB",
     "Clocks, months, dozens, and imperial units."),
    ("Hexadecimal", 16, "0123456789ABCDEF",
     "Memory addresses, color codes, and byte representation in computing."),
    ("Vigesimal", 20, "Digits 0-9 then A-J",
     "Mayan and some historical counting systems."),
    ("Base32", 32, "A-Z and 2-7 (RFC 4648)",
     "Case-insensitive encoding for identifiers and data transfer."),
    ("Base64", 64, "A-Z, a-z, 0-9, + and / (RFC 4648)",
     "Encoding binary data as ASCII text in email and data URLs."),
    ("Sexagesimal", 60, "Sixty distinct values",
     "Time (minutes, seconds) and angular measurement (degrees)."),
]

ITEMS = [
    {
        "id": i + 1,
        "name": name,
        "base": base,
        "digits": digits,
        "common_use": use,
    }
    for i, (name, base, digits, use) in enumerate(_RAW)
]
