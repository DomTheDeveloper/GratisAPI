"""Bright and notable stars of the night sky."""

META = {
    "name": "stars",
    "title": "Stars",
    "description": "Bright and notable stars with constellation, magnitude, distance and spectral type.",
    "emoji": "⭐",
}

# (id, name, constellation, apparent_magnitude, distance_ly, spectral_type)
_ROWS = [
    ("sirius", "Sirius", "Canis Major", -1.46, 8.6, "A1V"),
    ("canopus", "Canopus", "Carina", -0.74, 310.0, "A9II"),
    ("alpha-centauri", "Alpha Centauri A", "Centaurus", -0.27, 4.37, "G2V"),
    ("arcturus", "Arcturus", "Bootes", -0.05, 36.7, "K0III"),
    ("vega", "Vega", "Lyra", 0.03, 25.0, "A0V"),
    ("capella", "Capella", "Auriga", 0.08, 42.9, "G8III"),
    ("rigel", "Rigel", "Orion", 0.13, 860.0, "B8Ia"),
    ("procyon", "Procyon", "Canis Minor", 0.34, 11.5, "F5IV-V"),
    ("achernar", "Achernar", "Eridanus", 0.46, 139.0, "B6Vpe"),
    ("betelgeuse", "Betelgeuse", "Orion", 0.50, 548.0, "M1-2Ia-ab"),
    ("hadar", "Hadar", "Centaurus", 0.61, 390.0, "B1III"),
    ("altair", "Altair", "Aquila", 0.76, 16.7, "A7V"),
    ("acrux", "Acrux", "Crux", 0.76, 320.0, "B0.5IV"),
    ("aldebaran", "Aldebaran", "Taurus", 0.86, 65.3, "K5III"),
    ("antares", "Antares", "Scorpius", 0.96, 550.0, "M1.5Iab"),
    ("spica", "Spica", "Virgo", 1.04, 250.0, "B1III-IV"),
    ("pollux", "Pollux", "Gemini", 1.14, 33.8, "K0III"),
    ("fomalhaut", "Fomalhaut", "Piscis Austrinus", 1.16, 25.1, "A3V"),
    ("deneb", "Deneb", "Cygnus", 1.25, 2615.0, "A2Ia"),
    ("mimosa", "Mimosa", "Crux", 1.25, 280.0, "B0.5III"),
    ("regulus", "Regulus", "Leo", 1.36, 79.3, "B8IVn"),
    ("adhara", "Adhara", "Canis Major", 1.50, 430.0, "B2II"),
    ("castor", "Castor", "Gemini", 1.57, 51.0, "A1V"),
    ("shaula", "Shaula", "Scorpius", 1.62, 570.0, "B2IV"),
    ("bellatrix", "Bellatrix", "Orion", 1.64, 250.0, "B2III"),
    ("polaris", "Polaris", "Ursa Minor", 1.98, 433.0, "F7Ib"),
    ("alnilam", "Alnilam", "Orion", 1.69, 2000.0, "B0Ia"),
    ("dubhe", "Dubhe", "Ursa Major", 1.79, 123.0, "K0III"),
    ("mizar", "Mizar", "Ursa Major", 2.04, 82.9, "A2Vp"),
    ("gacrux", "Gacrux", "Crux", 1.63, 88.6, "M3.5III"),
]

ITEMS = [
    {
        "id": _id,
        "name": name,
        "constellation": constellation,
        "apparent_magnitude": mag,
        "distance_ly": dist,
        "spectral_type": spectral,
    }
    for (_id, name, constellation, mag, dist, spectral) in _ROWS
]
