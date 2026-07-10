"""Types of tea, categorized by processing style, origin, and caffeine level."""

META = {
    "name": "teas",
    "title": "Types of Tea",
    "description": "A collection of well-known teas with their type, origin, and caffeine level.",
    "emoji": "\U0001F375",
}

ITEMS = [
    # --- Black ---
    {"id": "english-breakfast", "name": "English Breakfast", "type": "Black", "origin_region": "Blend (India, Sri Lanka, Kenya)", "caffeine": "High", "notes": "Full-bodied, robust blend traditionally taken with milk."},
    {"id": "earl-grey", "name": "Earl Grey", "type": "Black", "origin_region": "Blend (China/India base)", "caffeine": "High", "notes": "Black tea flavored with oil of bergamot, giving a citrusy aroma."},
    {"id": "assam", "name": "Assam", "type": "Black", "origin_region": "Assam, India", "caffeine": "High", "notes": "Malty and brisk, grown in the lowlands of northeast India."},
    {"id": "darjeeling", "name": "Darjeeling", "type": "Black", "origin_region": "Darjeeling, India", "caffeine": "Medium", "notes": "Light, floral and muscatel; called the 'champagne of teas'."},
    {"id": "ceylon", "name": "Ceylon", "type": "Black", "origin_region": "Sri Lanka", "caffeine": "High", "notes": "Bright and citrusy black tea from the island of Sri Lanka."},
    {"id": "keemun", "name": "Keemun", "type": "Black", "origin_region": "Anhui, China", "caffeine": "Medium", "notes": "Wine-like and slightly smoky, a classic Chinese black tea."},
    {"id": "lapsang-souchong", "name": "Lapsang Souchong", "type": "Black", "origin_region": "Fujian, China", "caffeine": "Medium", "notes": "Dried over pinewood fires for a distinctive smoky flavor."},

    # --- Green ---
    {"id": "sencha", "name": "Sencha", "type": "Green", "origin_region": "Japan", "caffeine": "Medium", "notes": "Steamed green tea, grassy and refreshing; Japan's most common tea."},
    {"id": "matcha", "name": "Matcha", "type": "Green", "origin_region": "Japan", "caffeine": "High", "notes": "Stone-ground shade-grown leaves whisked into a frothy suspension."},
    {"id": "gyokuro", "name": "Gyokuro", "type": "Green", "origin_region": "Japan", "caffeine": "High", "notes": "Shade-grown before harvest, prized for its sweet umami character."},
    {"id": "dragon-well", "name": "Dragon Well (Longjing)", "type": "Green", "origin_region": "Zhejiang, China", "caffeine": "Medium", "notes": "Pan-fired flat leaves with a nutty, chestnut-like taste."},
    {"id": "gunpowder", "name": "Gunpowder", "type": "Green", "origin_region": "Zhejiang, China", "caffeine": "Medium", "notes": "Rolled into small pellets; bold and slightly smoky."},
    {"id": "genmaicha", "name": "Genmaicha", "type": "Green", "origin_region": "Japan", "caffeine": "Low", "notes": "Green tea blended with roasted brown rice for a toasty flavor."},

    # --- White ---
    {"id": "silver-needle", "name": "Silver Needle (Baihao Yinzhen)", "type": "White", "origin_region": "Fujian, China", "caffeine": "Low", "notes": "Made only from young buds; delicate, sweet and mellow."},
    {"id": "white-peony", "name": "White Peony (Bai Mudan)", "type": "White", "origin_region": "Fujian, China", "caffeine": "Low", "notes": "Buds and leaves; fuller and more floral than Silver Needle."},

    # --- Oolong ---
    {"id": "tieguanyin", "name": "Tieguanyin", "type": "Oolong", "origin_region": "Fujian, China", "caffeine": "Medium", "notes": "Iron Goddess of Mercy; orchid-like and lightly oxidized."},
    {"id": "da-hong-pao", "name": "Da Hong Pao", "type": "Oolong", "origin_region": "Wuyi, Fujian, China", "caffeine": "Medium", "notes": "Roasted rock oolong with a rich mineral, roasted character."},
    {"id": "dong-ding", "name": "Dong Ding", "type": "Oolong", "origin_region": "Taiwan", "caffeine": "Medium", "notes": "Traditional Taiwanese oolong, smooth with a roasted finish."},
    {"id": "milk-oolong", "name": "Milk Oolong (Jin Xuan)", "type": "Oolong", "origin_region": "Taiwan", "caffeine": "Medium", "notes": "Naturally creamy, buttery aroma from the Jin Xuan cultivar."},

    # --- Pu-erh ---
    {"id": "sheng-puerh", "name": "Sheng Pu-erh (Raw)", "type": "Pu-erh", "origin_region": "Yunnan, China", "caffeine": "Medium", "notes": "Naturally aged fermented tea; grassy young, mellowing over years."},
    {"id": "shou-puerh", "name": "Shou Pu-erh (Ripe)", "type": "Pu-erh", "origin_region": "Yunnan, China", "caffeine": "Medium", "notes": "Pile-fermented for an earthy, smooth, dark liquor."},

    # --- Herbal (tisanes, caffeine-free) ---
    {"id": "chamomile", "name": "Chamomile", "type": "Herbal", "origin_region": "Europe/Western Asia", "caffeine": "None", "notes": "Dried flowers with an apple-like aroma; calming before sleep."},
    {"id": "peppermint", "name": "Peppermint", "type": "Herbal", "origin_region": "Europe", "caffeine": "None", "notes": "Cooling, minty infusion often used to aid digestion."},
    {"id": "rooibos", "name": "Rooibos", "type": "Herbal", "origin_region": "South Africa", "caffeine": "None", "notes": "Naturally sweet red bush tisane rich in antioxidants."},
    {"id": "hibiscus", "name": "Hibiscus", "type": "Herbal", "origin_region": "Tropical regions", "caffeine": "None", "notes": "Tart, ruby-red infusion of dried hibiscus flowers."},
    {"id": "ginger", "name": "Ginger", "type": "Herbal", "origin_region": "Asia", "caffeine": "None", "notes": "Spicy, warming root infusion often taken for colds."},
]
