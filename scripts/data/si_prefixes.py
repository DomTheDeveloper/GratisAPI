"""SI (metric) prefixes."""

META = {
    "name": "si-prefixes",
    "title": "SI Prefixes",
    "description": "Metric (SI) unit prefixes with symbol and power of ten.",
    "emoji": "\U0001F522",
}

# name, symbol, base-10 exponent
_RAW = [
    ("quetta", "Q", 30), ("ronna", "R", 27), ("yotta", "Y", 24),
    ("zetta", "Z", 21), ("exa", "E", 18), ("peta", "P", 15),
    ("tera", "T", 12), ("giga", "G", 9), ("mega", "M", 6),
    ("kilo", "k", 3), ("hecto", "h", 2), ("deca", "da", 1),
    ("deci", "d", -1), ("centi", "c", -2), ("milli", "m", -3),
    ("micro", "µ", -6), ("nano", "n", -9), ("pico", "p", -12),
    ("femto", "f", -15), ("atto", "a", -18), ("zepto", "z", -21),
    ("yocto", "y", -24), ("ronto", "r", -27), ("quecto", "q", -30),
]

ITEMS = [
    {
        "id": name,
        "name": name,
        "symbol": sym,
        "base_10": exp,
        "factor": f"1e{exp}",
    }
    for name, sym, exp in _RAW
]
