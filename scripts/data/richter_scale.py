"""The Richter / moment magnitude scale of earthquake classes."""

META = {
    "name": "richter-scale",
    "title": "Richter Scale",
    "description": "Earthquake magnitude classes from 0 to 10 with effects and frequency.",
    "emoji": "\U0001F30B",
}

# id, magnitude_range, class, effects, approx_frequency_per_year
_RAW = [
    (0, "0.0-0.9", "Micro", "Not felt by people; recorded only by seismographs.", None),
    (1, "1.0-1.9", "Micro", "Not felt; detected only by instruments.", None),
    (2, "2.0-2.9", "Minor", "Generally not felt, but recorded.", 1000000),
    (3, "3.0-3.9", "Minor", "Often felt indoors; rarely causes damage.", 100000),
    (4, "4.0-4.9", "Light", "Noticeable shaking; minor damage to objects.", 10000),
    (5, "5.0-5.9", "Moderate", "Damage to weak or poorly built structures.", 1000),
    (6, "6.0-6.9", "Strong", "Damage in populated areas over tens of kilometers.", 100),
    (7, "7.0-7.9", "Major", "Serious damage over large areas.", 10),
    (8, "8.0-8.9", "Great", "Severe damage and destruction across hundreds of kilometers.", 1),
    (9, "9.0-9.9", "Great", "Devastating; near-total destruction near the epicenter.", None),
    (10, "10.0 and greater", "Epic", "Never recorded; theoretical extreme magnitude.", None),
]

ITEMS = [
    {
        "id": r[0],
        "magnitude_range": r[1],
        "class": r[2],
        "effects": r[3],
        "approx_frequency_per_year": r[4],
    }
    for r in _RAW
]
