"""Famous and high mountains of the world with key data."""

META = {
    "name": "mountains",
    "title": "Mountains",
    "description": "Notable and high mountains of the world with elevation, range, and first ascent data.",
    "emoji": "\U000026F0",
}

_RAW = [
    ("everest", "Mount Everest", 8849, "Himalayas", "Nepal / China", "Asia", 1953),
    ("k2", "K2", 8611, "Karakoram", "Pakistan / China", "Asia", 1954),
    ("kangchenjunga", "Kangchenjunga", 8586, "Himalayas", "Nepal / India", "Asia", 1955),
    ("lhotse", "Lhotse", 8516, "Himalayas", "Nepal / China", "Asia", 1956),
    ("makalu", "Makalu", 8485, "Himalayas", "Nepal / China", "Asia", 1955),
    ("cho-oyu", "Cho Oyu", 8188, "Himalayas", "Nepal / China", "Asia", 1954),
    ("dhaulagiri", "Dhaulagiri I", 8167, "Himalayas", "Nepal", "Asia", 1960),
    ("manaslu", "Manaslu", 8163, "Himalayas", "Nepal", "Asia", 1956),
    ("nanga-parbat", "Nanga Parbat", 8126, "Himalayas", "Pakistan", "Asia", 1953),
    ("annapurna", "Annapurna I", 8091, "Himalayas", "Nepal", "Asia", 1950),
    ("gasherbrum-i", "Gasherbrum I", 8080, "Karakoram", "Pakistan / China", "Asia", 1958),
    ("broad-peak", "Broad Peak", 8051, "Karakoram", "Pakistan / China", "Asia", 1957),
    ("gasherbrum-ii", "Gasherbrum II", 8035, "Karakoram", "Pakistan / China", "Asia", 1956),
    ("shishapangma", "Shishapangma", 8027, "Himalayas", "China", "Asia", 1964),
    ("denali", "Denali", 6190, "Alaska Range", "United States", "North America", 1913),
    ("aconcagua", "Aconcagua", 6961, "Andes", "Argentina", "South America", 1897),
    ("kilimanjaro", "Mount Kilimanjaro", 5895, "Eastern Rift mountains", "Tanzania", "Africa", 1889),
    ("elbrus", "Mount Elbrus", 5642, "Caucasus", "Russia", "Europe", 1874),
    ("vinson", "Mount Vinson", 4892, "Sentinel Range", "Antarctica", "Antarctica", 1966),
    ("puncak-jaya", "Puncak Jaya", 4884, "Sudirman Range", "Indonesia", "Oceania", 1962),
    ("mont-blanc", "Mont Blanc", 4809, "Alps", "France / Italy", "Europe", 1786),
    ("matterhorn", "Matterhorn", 4478, "Alps", "Switzerland / Italy", "Europe", 1865),
    ("mount-kenya", "Mount Kenya", 5199, "None", "Kenya", "Africa", 1899),
    ("mount-fuji", "Mount Fuji", 3776, "None", "Japan", "Asia", 663),
    ("mount-kosciuszko", "Mount Kosciuszko", 2228, "Great Dividing Range", "Australia", "Oceania", 1840),
    ("mount-rainier", "Mount Rainier", 4392, "Cascade Range", "United States", "North America", 1870),
    ("pikes-peak", "Pikes Peak", 4302, "Rocky Mountains", "United States", "North America", 1820),
    ("eiger", "Eiger", 3967, "Alps", "Switzerland", "Europe", 1858),
    ("mount-cook", "Aoraki / Mount Cook", 3724, "Southern Alps", "New Zealand", "Oceania", 1894),
    ("mount-whitney", "Mount Whitney", 4421, "Sierra Nevada", "United States", "North America", 1873),
    ("ojos-del-salado", "Ojos del Salado", 6893, "Andes", "Argentina / Chile", "South America", 1937),
]

ITEMS = [
    {
        "id": r[0],
        "name": r[1],
        "height_m": r[2],
        "range": None if r[3] == "None" else r[3],
        "country": r[4],
        "continent": r[5],
        "first_ascent_year": r[6],
    }
    for r in _RAW
]
