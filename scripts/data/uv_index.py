"""World Health Organization UV Index categories."""

META = {
    "name": "uv-index",
    "title": "UV Index",
    "description": "WHO UV Index exposure categories with associated risk and protection advice.",
    "emoji": "☀️",
}

# range, category, risk, protection_advice
_RAW = [
    ("0-2", "Low", "Minimal danger from the sun for the average person.",
     "No protection needed. You can safely stay outside."),
    ("3-5", "Moderate", "Moderate risk of harm from unprotected sun exposure.",
     "Seek shade during midday hours; wear sunscreen, a hat, and sunglasses."),
    ("6-7", "High", "High risk of harm from unprotected sun exposure.",
     "Reduce time in the sun between 10am and 4pm; apply SPF 30+ sunscreen, cover up, and wear a hat."),
    ("8-10", "Very High", "Very high risk of harm; unprotected skin can burn quickly.",
     "Minimize sun exposure midday; sunscreen, protective clothing, hat, and sunglasses are a must."),
    ("11+", "Extreme", "Extreme risk of harm; unprotected skin can burn in minutes.",
     "Avoid the sun midday; take all precautions including shade, clothing, hat, sunglasses, and SPF 30+ sunscreen."),
]

ITEMS = [
    {
        "id": i + 1,
        "range": rng,
        "category": cat,
        "risk": risk,
        "protection_advice": advice,
    }
    for i, (rng, cat, risk, advice) in enumerate(_RAW)
]
