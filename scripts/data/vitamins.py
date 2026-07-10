"""Essential human vitamins."""

META = {
    "name": "vitamins",
    "title": "Vitamins",
    "description": "The 13 essential human vitamins with function, solubility and food sources.",
    "emoji": "\U0001F48A",
}

# id, name, chemical_name, solubility, function, deficiency, sources
_RAW = [
    ("vitamin-a", "Vitamin A", "Retinol", "Fat", "Vision, immune function and skin health", "Night blindness", ["Carrots", "Liver", "Sweet potato"]),
    ("vitamin-b1", "Vitamin B1", "Thiamine", "Water", "Energy metabolism and nerve function", "Beriberi", ["Whole grains", "Pork", "Legumes"]),
    ("vitamin-b2", "Vitamin B2", "Riboflavin", "Water", "Energy production and cellular function", "Ariboflavinosis", ["Eggs", "Milk", "Almonds"]),
    ("vitamin-b3", "Vitamin B3", "Niacin", "Water", "Energy metabolism and DNA repair", "Pellagra", ["Meat", "Fish", "Peanuts"]),
    ("vitamin-b5", "Vitamin B5", "Pantothenic acid", "Water", "Synthesis of coenzyme A and fatty acids", "Paresthesia", ["Avocado", "Eggs", "Mushrooms"]),
    ("vitamin-b6", "Vitamin B6", "Pyridoxine", "Water", "Amino acid metabolism and neurotransmitters", "Anaemia", ["Poultry", "Bananas", "Chickpeas"]),
    ("vitamin-b7", "Vitamin B7", "Biotin", "Water", "Metabolism of fats, carbohydrates and protein", "Dermatitis", ["Eggs", "Nuts", "Salmon"]),
    ("vitamin-b9", "Vitamin B9", "Folate", "Water", "DNA synthesis and cell division", "Neural tube defects", ["Leafy greens", "Legumes", "Citrus"]),
    ("vitamin-b12", "Vitamin B12", "Cobalamin", "Water", "Red blood cell formation and nerve function", "Pernicious anaemia", ["Meat", "Fish", "Dairy"]),
    ("vitamin-c", "Vitamin C", "Ascorbic acid", "Water", "Collagen synthesis and antioxidant defence", "Scurvy", ["Citrus", "Peppers", "Broccoli"]),
    ("vitamin-d", "Vitamin D", "Calciferol", "Fat", "Calcium absorption and bone health", "Rickets", ["Sunlight", "Fatty fish", "Fortified milk"]),
    ("vitamin-e", "Vitamin E", "Tocopherol", "Fat", "Antioxidant protecting cell membranes", "Nerve damage", ["Nuts", "Seeds", "Vegetable oils"]),
    ("vitamin-k", "Vitamin K", "Phylloquinone", "Fat", "Blood clotting and bone metabolism", "Excessive bleeding", ["Leafy greens", "Broccoli", "Natto"]),
]

ITEMS = [
    {
        "id": cid,
        "name": name,
        "chemical_name": chem,
        "solubility": sol,
        "function": func,
        "deficiency_disease": deficiency,
        "food_sources": sources,
    }
    for cid, name, chem, sol, func, deficiency, sources in _RAW
]
