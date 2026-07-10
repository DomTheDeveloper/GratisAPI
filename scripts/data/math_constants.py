"""Notable mathematical constants."""

META = {
    "name": "math_constants",
    "title": "Math Constants",
    "description": "Notable mathematical constants with symbols, values and descriptions.",
    "emoji": "➗",
}

# (id, name, symbol, value, description)
_ROWS = [
    ("pi", "Pi", "pi", 3.141592653589793, "Ratio of a circle's circumference to its diameter."),
    ("e", "Euler's number", "e", 2.718281828459045, "Base of the natural logarithm."),
    ("golden-ratio", "Golden ratio", "phi", 1.618033988749895, "Ratio where (a+b)/a equals a/b."),
    ("square-root-2", "Square root of 2", "sqrt(2)", 1.4142135623730951, "Pythagoras' constant, diagonal of a unit square."),
    ("square-root-3", "Square root of 3", "sqrt(3)", 1.7320508075688772, "Theodorus' constant."),
    ("square-root-5", "Square root of 5", "sqrt(5)", 2.23606797749979, "Appears in the golden ratio formula."),
    ("euler-mascheroni", "Euler-Mascheroni constant", "gamma", 0.5772156649015329, "Limit of harmonic series minus natural logarithm."),
    ("natural-log-2", "Natural logarithm of 2", "ln(2)", 0.6931471805599453, "Natural logarithm of two."),
    ("natural-log-10", "Natural logarithm of 10", "ln(10)", 2.302585092994046, "Natural logarithm of ten."),
    ("apery-constant", "Apery's constant", "zeta(3)", 1.2020569031595943, "Value of the Riemann zeta function at 3."),
    ("catalan-constant", "Catalan's constant", "G", 0.915965594177219, "Sum of alternating reciprocals of odd squares."),
    ("feigenbaum-delta", "Feigenbaum constant delta", "delta", 4.669201609102990, "Ratio of bifurcation intervals in chaotic maps."),
    ("feigenbaum-alpha", "Feigenbaum constant alpha", "alpha", 2.502907875095892, "Reduction scaling in period-doubling bifurcations."),
    ("twin-prime-constant", "Twin prime constant", "C_2", 0.6601618158468696, "Density constant for twin primes."),
    ("khinchin-constant", "Khinchin's constant", "K_0", 2.685452001065306, "Geometric mean of continued fraction terms."),
    ("plastic-number", "Plastic number", "rho", 1.324717957244746, "Real root of x^3 = x + 1."),
    ("silver-ratio", "Silver ratio", "delta_S", 2.414213562373095, "1 + square root of 2."),
    ("golden-angle", "Golden angle", "g", 2.399963229728653, "The golden ratio angle in radians."),
    ("tau", "Tau", "tau", 6.283185307179586, "Ratio of a circle's circumference to its radius, 2*pi."),
    ("glaisher-kinkelin", "Glaisher-Kinkelin constant", "A", 1.2824271291006226, "Appears in asymptotics of the hyperfactorial."),
]

ITEMS = [
    {
        "id": _id,
        "name": name,
        "symbol": symbol,
        "value": value,
        "description": description,
    }
    for (_id, name, symbol, value, description) in _ROWS
]
