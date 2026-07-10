"""Major and longest rivers of the world."""

META = {
    "name": "rivers",
    "title": "Rivers",
    "description": "Major rivers of the world with length, continent, and drainage information.",
    "emoji": "\U0001F30A",
}

_RAW = [
    ("nile", "Nile", 6650, "Africa", "Mediterranean Sea", "Egypt, Sudan, Uganda"),
    ("amazon", "Amazon", 6400, "South America", "Atlantic Ocean", "Brazil, Peru, Colombia"),
    ("yangtze", "Yangtze", 6300, "Asia", "East China Sea", "China"),
    ("mississippi-missouri", "Mississippi-Missouri", 6275, "North America", "Gulf of Mexico", "United States"),
    ("yenisei", "Yenisei", 5539, "Asia", "Arctic Ocean (Kara Sea)", "Russia, Mongolia"),
    ("yellow-river", "Yellow River (Huang He)", 5464, "Asia", "Bohai Sea", "China"),
    ("ob-irtysh", "Ob-Irtysh", 5410, "Asia", "Arctic Ocean (Gulf of Ob)", "Russia, Kazakhstan, China"),
    ("parana", "Parana", 4880, "South America", "Atlantic Ocean (Rio de la Plata)", "Brazil, Argentina, Paraguay"),
    ("congo", "Congo", 4700, "Africa", "Atlantic Ocean", "DR Congo, Congo, Angola"),
    ("amur", "Amur", 4444, "Asia", "Sea of Okhotsk", "Russia, China"),
    ("lena", "Lena", 4400, "Asia", "Arctic Ocean (Laptev Sea)", "Russia"),
    ("mekong", "Mekong", 4350, "Asia", "South China Sea", "China, Laos, Cambodia, Vietnam"),
    ("mackenzie", "Mackenzie", 4241, "North America", "Arctic Ocean (Beaufort Sea)", "Canada"),
    ("niger", "Niger", 4200, "Africa", "Gulf of Guinea (Atlantic Ocean)", "Nigeria, Mali, Niger"),
    ("murray-darling", "Murray-Darling", 3672, "Oceania", "Southern Ocean", "Australia"),
    ("volga", "Volga", 3530, "Europe", "Caspian Sea", "Russia"),
    ("indus", "Indus", 3180, "Asia", "Arabian Sea", "Pakistan, India, China"),
    ("purus", "Purus", 3211, "South America", "Amazon River", "Brazil, Peru"),
    ("madeira", "Madeira", 3250, "South America", "Amazon River", "Brazil, Bolivia"),
    ("sao-francisco", "Sao Francisco", 2900, "South America", "Atlantic Ocean", "Brazil"),
    ("yukon", "Yukon", 3190, "North America", "Bering Sea", "United States, Canada"),
    ("rio-grande", "Rio Grande", 3057, "North America", "Gulf of Mexico", "United States, Mexico"),
    ("danube", "Danube", 2850, "Europe", "Black Sea", "Germany, Austria, Hungary, Romania"),
    ("brahmaputra", "Brahmaputra", 2900, "Asia", "Bay of Bengal", "China, India, Bangladesh"),
    ("ganges", "Ganges", 2525, "Asia", "Bay of Bengal", "India, Bangladesh"),
    ("euphrates", "Euphrates", 2800, "Asia", "Persian Gulf", "Turkey, Syria, Iraq"),
    ("zambezi", "Zambezi", 2574, "Africa", "Indian Ocean (Mozambique Channel)", "Zambia, Mozambique, Zimbabwe"),
    ("orinoco", "Orinoco", 2140, "South America", "Atlantic Ocean", "Venezuela, Colombia"),
    ("colorado", "Colorado", 2330, "North America", "Gulf of California", "United States, Mexico"),
    ("rhine", "Rhine", 1233, "Europe", "North Sea", "Switzerland, Germany, Netherlands"),
    ("tigris", "Tigris", 1850, "Asia", "Persian Gulf", "Turkey, Iraq, Syria"),
]

ITEMS = [
    {
        "id": r[0],
        "name": r[1],
        "length_km": r[2],
        "continent": r[3],
        "outflow": r[4],
        "countries": r[5],
    }
    for r in _RAW
]
