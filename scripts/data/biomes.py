"""The major terrestrial biomes of the world."""

META = {
    "name": "biomes",
    "title": "Terrestrial Biomes",
    "description": "The major land biomes with their climate, rainfall, and typical vegetation.",
    "emoji": "🌍",
}

# id, name, climate, avg_rainfall_mm, example_regions, dominant_vegetation
_RAW = [
    ("tropical-rainforest", "Tropical Rainforest",
     "Hot and humid year-round", 2500,
     "Amazon Basin, Congo Basin, Southeast Asia",
     "Dense broadleaf evergreen trees with layered canopy."),
    ("tropical-savanna", "Tropical Savanna",
     "Warm with distinct wet and dry seasons", 1000,
     "Serengeti, northern Australia, the Cerrado",
     "Grasslands with scattered drought-tolerant trees."),
    ("desert", "Desert",
     "Very hot or cold with extreme aridity", 200,
     "Sahara, Arabian, Mojave, Atacama",
     "Sparse succulents, cacti, and hardy shrubs."),
    ("temperate-grassland", "Temperate Grassland",
     "Warm summers and cold winters, semi-arid", 600,
     "North American prairies, Eurasian steppe, pampas",
     "Grasses and herbaceous plants with few trees."),
    ("temperate-deciduous-forest", "Temperate Deciduous Forest",
     "Four distinct seasons with moderate rainfall", 1200,
     "Eastern North America, Western Europe, East Asia",
     "Broadleaf trees that shed leaves in autumn."),
    ("mediterranean", "Mediterranean (Chaparral)",
     "Hot dry summers and mild wet winters", 500,
     "California, Mediterranean Basin, central Chile",
     "Drought-resistant evergreen shrubs and small trees."),
    ("taiga", "Taiga (Boreal Forest)",
     "Long cold winters and short cool summers", 500,
     "Canada, Scandinavia, Siberia",
     "Coniferous evergreen trees like spruce, fir, and pine."),
    ("tundra", "Tundra",
     "Extremely cold with permafrost and short growing season", 250,
     "Arctic Circle, alpine peaks, northern Alaska",
     "Mosses, lichens, sedges, and dwarf shrubs."),
    ("temperate-rainforest", "Temperate Rainforest",
     "Cool, wet, and mild with high humidity", 2000,
     "Pacific Northwest, southern Chile, New Zealand",
     "Towering conifers with dense ferns and mosses."),
    ("montane", "Montane (Alpine)",
     "Cold temperatures decreasing with elevation", 1000,
     "Andes, Himalayas, Rocky Mountains, Alps",
     "Zoned vegetation from forest to alpine meadow and bare rock."),
    ("mangrove", "Mangrove",
     "Tropical coastal, warm and tidal", 1800,
     "Sundarbans, Florida Everglades, Southeast Asian coasts",
     "Salt-tolerant mangrove trees with stilt roots."),
    ("wetland", "Wetland",
     "Varied, with waterlogged soils year-round", 1200,
     "Pantanal, Okavango Delta, Everglades",
     "Reeds, sedges, grasses, and water-tolerant plants."),
]

ITEMS = [
    {
        "id": r[0],
        "name": r[1],
        "climate": r[2],
        "avg_rainfall_mm": r[3],
        "example_regions": r[4],
        "dominant_vegetation": r[5],
    }
    for r in _RAW
]
