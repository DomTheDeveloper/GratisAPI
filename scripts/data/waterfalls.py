"""Famous waterfalls of the world with height and location."""

META = {
    "name": "waterfalls",
    "title": "Waterfalls",
    "description": "Famous waterfalls of the world with total height, river, and location.",
    "emoji": "\U0001F4A6",
}

_RAW = [
    ("angel-falls", "Angel Falls", 979, "Churun River", "Venezuela", "South America"),
    ("tugela-falls", "Tugela Falls", 948, "Tugela River", "South Africa", "Africa"),
    ("olo-upena-falls", "Olo'upena Falls", 900, None, "United States", "North America"),
    ("yumbilla-falls", "Yumbilla Falls", 895, None, "Peru", "South America"),
    ("vinnufossen", "Vinnufossen", 860, "Vinnu River", "Norway", "Europe"),
    ("balaifossen", "Balaifossen", 850, "Balaielvi", "Norway", "Europe"),
    ("browne-falls", "Browne Falls", 836, "Browne River", "New Zealand", "Oceania"),
    ("james-bruce-falls", "James Bruce Falls", 840, None, "Canada", "North America"),
    ("niagara-falls", "Niagara Falls", 51, "Niagara River", "United States / Canada", "North America"),
    ("victoria-falls", "Victoria Falls", 108, "Zambezi River", "Zambia / Zimbabwe", "Africa"),
    ("iguazu-falls", "Iguazu Falls", 82, "Iguazu River", "Argentina / Brazil", "South America"),
    ("kaieteur-falls", "Kaieteur Falls", 226, "Potaro River", "Guyana", "South America"),
    ("gullfoss", "Gullfoss", 32, "Hvita River", "Iceland", "Europe"),
    ("sutherland-falls", "Sutherland Falls", 580, "Arthur River", "New Zealand", "Oceania"),
    ("plitvice-falls", "Plitvice (Veliki Slap)", 78, "Plitvica River", "Croatia", "Europe"),
    ("dettifoss", "Dettifoss", 44, "Jokulsa a Fjollum", "Iceland", "Europe"),
]

ITEMS = [
    {
        "id": r[0],
        "name": r[1],
        "height_m": r[2],
        "river": r[3],
        "country": r[4],
        "continent": r[5],
    }
    for r in _RAW
]
