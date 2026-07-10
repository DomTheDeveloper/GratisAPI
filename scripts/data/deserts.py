"""Major deserts of the world with area and type."""

META = {
    "name": "deserts",
    "title": "Deserts",
    "description": "Major deserts of the world with approximate area, continent, and type.",
    "emoji": "\U0001F3DC",
}

_RAW = [
    ("antarctic", "Antarctic Desert", 14000000, "Antarctica", "Cold (polar)"),
    ("arctic", "Arctic Desert", 13900000, "Arctic", "Cold (polar)"),
    ("sahara", "Sahara", 9200000, "Africa", "Hot"),
    ("arabian", "Arabian Desert", 2330000, "Asia", "Hot"),
    ("gobi", "Gobi Desert", 1295000, "Asia", "Cold"),
    ("kalahari", "Kalahari Desert", 900000, "Africa", "Hot"),
    ("patagonian", "Patagonian Desert", 673000, "South America", "Cold"),
    ("great-victoria", "Great Victoria Desert", 348750, "Oceania", "Hot"),
    ("syrian", "Syrian Desert", 500000, "Asia", "Hot"),
    ("great-basin", "Great Basin Desert", 492000, "North America", "Cold"),
    ("chihuahuan", "Chihuahuan Desert", 362000, "North America", "Hot"),
    ("great-sandy", "Great Sandy Desert", 284993, "Oceania", "Hot"),
    ("kyzylkum", "Kyzylkum Desert", 298000, "Asia", "Cold"),
    ("sonoran", "Sonoran Desert", 260000, "North America", "Hot"),
    ("taklamakan", "Taklamakan Desert", 337000, "Asia", "Cold"),
    ("thar", "Thar Desert", 200000, "Asia", "Hot"),
    ("karakum", "Karakum Desert", 350000, "Asia", "Cold"),
    ("namib", "Namib Desert", 81000, "Africa", "Coastal"),
    ("atacama", "Atacama Desert", 105000, "South America", "Coastal"),
    ("mojave", "Mojave Desert", 124000, "North America", "Hot"),
    ("simpson", "Simpson Desert", 176500, "Oceania", "Hot"),
]

ITEMS = [
    {
        "id": r[0],
        "name": r[1],
        "area_km2": r[2],
        "continent": r[3],
        "type": r[4],
    }
    for r in _RAW
]
