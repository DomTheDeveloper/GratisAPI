"""Notable volcanoes around the world."""

META = {
    "name": "volcanoes",
    "title": "Notable Volcanoes",
    "description": "Famous volcanoes with their type, location, and most recent major eruption.",
    "emoji": "🌋",
}

# id, name, country, type, elevation_m, last_major_eruption
_RAW = [
    ("vesuvius", "Mount Vesuvius", "Italy", "Complex", 1281, 1944),
    ("etna", "Mount Etna", "Italy", "Stratovolcano", 3357, 2023),
    ("stromboli", "Stromboli", "Italy", "Stratovolcano", 924, 2024),
    ("fuji", "Mount Fuji", "Japan", "Stratovolcano", 3776, 1707),
    ("sakurajima", "Sakurajima", "Japan", "Stratovolcano", 1117, 2022),
    ("krakatoa", "Krakatoa", "Indonesia", "Caldera", 813, 2020),
    ("tambora", "Mount Tambora", "Indonesia", "Stratovolcano", 2850, 1815),
    ("merapi", "Mount Merapi", "Indonesia", "Stratovolcano", 2910, 2023),
    ("pinatubo", "Mount Pinatubo", "Philippines", "Stratovolcano", 1486, 1991),
    ("mayon", "Mayon", "Philippines", "Stratovolcano", 2463, 2018),
    ("taal", "Taal Volcano", "Philippines", "Caldera", 311, 2022),
    ("st-helens", "Mount St. Helens", "United States", "Stratovolcano", 2549, 1980),
    ("kilauea", "Kilauea", "United States", "Shield", 1247, 2023),
    ("mauna-loa", "Mauna Loa", "United States", "Shield", 4169, 2022),
    ("rainier", "Mount Rainier", "United States", "Stratovolcano", 4392, "1450 CE"),
    ("yellowstone", "Yellowstone Caldera", "United States", "Caldera", 2805, "640,000 years ago"),
    ("popocatepetl", "Popocatepetl", "Mexico", "Stratovolcano", 5426, 2023),
    ("colima", "Volcan de Colima", "Mexico", "Stratovolcano", 3820, 2017),
    ("cotopaxi", "Cotopaxi", "Ecuador", "Stratovolcano", 5897, 2023),
    ("villarrica", "Villarrica", "Chile", "Stratovolcano", 2847, 2015),
    ("nevado-del-ruiz", "Nevado del Ruiz", "Colombia", "Stratovolcano", 5321, 1985),
    ("kilimanjaro", "Mount Kilimanjaro", "Tanzania", "Stratovolcano", 5895, "150,000 years ago"),
    ("nyiragongo", "Mount Nyiragongo", "DR Congo", "Stratovolcano", 3470, 2021),
    ("erebus", "Mount Erebus", "Antarctica", "Stratovolcano", 3794, 2024),
    ("eyjafjallajokull", "Eyjafjallajokull", "Iceland", "Stratovolcano", 1651, 2010),
    ("hekla", "Hekla", "Iceland", "Stratovolcano", 1491, 2000),
    ("teide", "Mount Teide", "Spain", "Stratovolcano", 3715, 1909),
]

ITEMS = [
    {
        "id": r[0],
        "name": r[1],
        "country": r[2],
        "type": r[3],
        "elevation_m": r[4],
        "last_major_eruption": r[5],
    }
    for r in _RAW
]
