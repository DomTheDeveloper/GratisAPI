"""Largest and most notable lakes of the world."""

META = {
    "name": "lakes",
    "title": "Lakes",
    "description": "Large and notable lakes of the world with surface area, depth, and type.",
    "emoji": "\U0001F3DE",
}

_RAW = [
    ("caspian-sea", "Caspian Sea", 371000, 1025, "Asia / Europe", "Salt"),
    ("superior", "Lake Superior", 82100, 406, "North America", "Freshwater"),
    ("victoria", "Lake Victoria", 68870, 84, "Africa", "Freshwater"),
    ("huron", "Lake Huron", 59600, 229, "North America", "Freshwater"),
    ("michigan", "Lake Michigan", 58000, 281, "North America", "Freshwater"),
    ("tanganyika", "Lake Tanganyika", 32900, 1470, "Africa", "Freshwater"),
    ("baikal", "Lake Baikal", 31500, 1642, "Asia", "Freshwater"),
    ("great-bear", "Great Bear Lake", 31000, 446, "North America", "Freshwater"),
    ("malawi", "Lake Malawi", 29500, 706, "Africa", "Freshwater"),
    ("great-slave", "Great Slave Lake", 27000, 614, "North America", "Freshwater"),
    ("erie", "Lake Erie", 25700, 64, "North America", "Freshwater"),
    ("winnipeg", "Lake Winnipeg", 24400, 36, "North America", "Freshwater"),
    ("ontario", "Lake Ontario", 18960, 244, "North America", "Freshwater"),
    ("ladoga", "Lake Ladoga", 17700, 230, "Europe", "Freshwater"),
    ("balkhash", "Lake Balkhash", 16400, 26, "Asia", "Salt"),
    ("vostok", "Lake Vostok", 12500, 800, "Antarctica", "Freshwater"),
    ("onega", "Lake Onega", 9700, 127, "Europe", "Freshwater"),
    ("titicaca", "Lake Titicaca", 8372, 281, "South America", "Freshwater"),
    ("nicaragua", "Lake Nicaragua", 8264, 26, "North America", "Freshwater"),
    ("athabasca", "Lake Athabasca", 7850, 124, "North America", "Freshwater"),
    ("turkana", "Lake Turkana", 6405, 109, "Africa", "Salt"),
    ("issyk-kul", "Issyk-Kul", 6236, 668, "Asia", "Salt"),
    ("great-salt-lake", "Great Salt Lake", 4400, 10, "North America", "Salt"),
    ("vanern", "Lake Vanern", 5650, 106, "Europe", "Freshwater"),
    ("tahoe", "Lake Tahoe", 495, 501, "North America", "Freshwater"),
]

ITEMS = [
    {
        "id": r[0],
        "name": r[1],
        "area_km2": r[2],
        "max_depth_m": r[3],
        "continent": r[4],
        "type": r[5],
    }
    for r in _RAW
]
