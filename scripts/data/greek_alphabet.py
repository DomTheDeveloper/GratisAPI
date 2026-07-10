"""The Greek alphabet: 24 letters with transliteration and numeric values."""

META = {
    "name": "greek_alphabet",
    "title": "Greek Alphabet",
    "description": "The 24 letters of the Greek alphabet with transliteration and numeric value.",
    "emoji": "\U0001F1EC\U0001F1F7",
}

# name, uppercase, lowercase, transliteration, numeric_value
_RAW = [
    ("alpha", "Α", "α", "a", 1),
    ("beta", "Β", "β", "b", 2),
    ("gamma", "Γ", "γ", "g", 3),
    ("delta", "Δ", "δ", "d", 4),
    ("epsilon", "Ε", "ε", "e", 5),
    ("zeta", "Ζ", "ζ", "z", 7),
    ("eta", "Η", "η", "e", 8),
    ("theta", "Θ", "θ", "th", 9),
    ("iota", "Ι", "ι", "i", 10),
    ("kappa", "Κ", "κ", "k", 20),
    ("lambda", "Λ", "λ", "l", 30),
    ("mu", "Μ", "μ", "m", 40),
    ("nu", "Ν", "ν", "n", 50),
    ("xi", "Ξ", "ξ", "x", 60),
    ("omicron", "Ο", "ο", "o", 70),
    ("pi", "Π", "π", "p", 80),
    ("rho", "Ρ", "ρ", "r", 100),
    ("sigma", "Σ", "σ", "s", 200),
    ("tau", "Τ", "τ", "t", 300),
    ("upsilon", "Υ", "υ", "y", 400),
    ("phi", "Φ", "φ", "ph", 500),
    ("chi", "Χ", "χ", "ch", 600),
    ("psi", "Ψ", "ψ", "ps", 700),
    ("omega", "Ω", "ω", "o", 800),
]

ITEMS = [
    {"id": name, "name": name.capitalize(), "uppercase": upper, "lowercase": lower,
     "transliteration": translit, "numeric_value": numeric}
    for name, upper, lower, translit, numeric in _RAW
]
