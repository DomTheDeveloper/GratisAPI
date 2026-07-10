"""Cat breeds: country of origin, coat length, temperament and life expectancy."""

META = {
    "name": "cat_breeds",
    "title": "Cat Breeds",
    "description": "Popular cat breeds with country of origin, coat type and temperament.",
    "emoji": "\U0001F408",
}

ITEMS = [
    {
        "id": "persian", "name": "Persian", "origin": "Iran", "coat": "Long",
        "temperament": "Gentle, quiet and affectionate", "life_expectancy_years": "12-17",
    },
    {
        "id": "maine-coon", "name": "Maine Coon", "origin": "United States", "coat": "Long",
        "temperament": "Gentle, friendly and playful", "life_expectancy_years": "12-15",
    },
    {
        "id": "siamese", "name": "Siamese", "origin": "Thailand", "coat": "Short",
        "temperament": "Vocal, social and intelligent", "life_expectancy_years": "12-20",
    },
    {
        "id": "ragdoll", "name": "Ragdoll", "origin": "United States", "coat": "Long",
        "temperament": "Docile, calm and affectionate", "life_expectancy_years": "12-17",
    },
    {
        "id": "bengal", "name": "Bengal", "origin": "United States", "coat": "Short",
        "temperament": "Active, curious and playful", "life_expectancy_years": "12-16",
    },
    {
        "id": "british-shorthair", "name": "British Shorthair", "origin": "United Kingdom", "coat": "Short",
        "temperament": "Calm, easygoing and loyal", "life_expectancy_years": "12-17",
    },
    {
        "id": "abyssinian", "name": "Abyssinian", "origin": "Ethiopia", "coat": "Short",
        "temperament": "Active, curious and playful", "life_expectancy_years": "9-15",
    },
    {
        "id": "sphynx", "name": "Sphynx", "origin": "Canada", "coat": "Hairless",
        "temperament": "Energetic, affectionate and mischievous", "life_expectancy_years": "8-14",
    },
    {
        "id": "scottish-fold", "name": "Scottish Fold", "origin": "United Kingdom", "coat": "Short",
        "temperament": "Sweet, calm and adaptable", "life_expectancy_years": "11-14",
    },
    {
        "id": "russian-blue", "name": "Russian Blue", "origin": "Russia", "coat": "Short",
        "temperament": "Gentle, reserved and affectionate", "life_expectancy_years": "15-20",
    },
    {
        "id": "american-shorthair", "name": "American Shorthair", "origin": "United States", "coat": "Short",
        "temperament": "Easygoing, affectionate and adaptable", "life_expectancy_years": "15-20",
    },
    {
        "id": "norwegian-forest-cat", "name": "Norwegian Forest Cat", "origin": "Norway", "coat": "Long",
        "temperament": "Friendly, gentle and independent", "life_expectancy_years": "14-16",
    },
    {
        "id": "birman", "name": "Birman", "origin": "France", "coat": "Long",
        "temperament": "Affectionate, gentle and social", "life_expectancy_years": "12-16",
    },
    {
        "id": "oriental-shorthair", "name": "Oriental Shorthair", "origin": "United States", "coat": "Short",
        "temperament": "Vocal, curious and social", "life_expectancy_years": "12-15",
    },
    {
        "id": "devon-rex", "name": "Devon Rex", "origin": "United Kingdom", "coat": "Short",
        "temperament": "Playful, mischievous and affectionate", "life_expectancy_years": "9-15",
    },
    {
        "id": "cornish-rex", "name": "Cornish Rex", "origin": "United Kingdom", "coat": "Short",
        "temperament": "Active, playful and affectionate", "life_expectancy_years": "11-15",
    },
    {
        "id": "burmese", "name": "Burmese", "origin": "Myanmar", "coat": "Short",
        "temperament": "Affectionate, social and playful", "life_expectancy_years": "16-18",
    },
    {
        "id": "tonkinese", "name": "Tonkinese", "origin": "Canada", "coat": "Short",
        "temperament": "Playful, curious and social", "life_expectancy_years": "12-16",
    },
    {
        "id": "exotic-shorthair", "name": "Exotic Shorthair", "origin": "United States", "coat": "Short",
        "temperament": "Gentle, calm and affectionate", "life_expectancy_years": "12-15",
    },
    {
        "id": "himalayan", "name": "Himalayan", "origin": "United States", "coat": "Long",
        "temperament": "Sweet, calm and gentle", "life_expectancy_years": "9-15",
    },
    {
        "id": "turkish-angora", "name": "Turkish Angora", "origin": "Turkey", "coat": "Long",
        "temperament": "Playful, intelligent and affectionate", "life_expectancy_years": "12-18",
    },
    {
        "id": "manx", "name": "Manx", "origin": "Isle of Man", "coat": "Short",
        "temperament": "Playful, gentle and social", "life_expectancy_years": "9-13",
    },
    {
        "id": "savannah", "name": "Savannah", "origin": "United States", "coat": "Short",
        "temperament": "Adventurous, active and loyal", "life_expectancy_years": "12-20",
    },
    {
        "id": "somali", "name": "Somali", "origin": "United States", "coat": "Long",
        "temperament": "Active, curious and playful", "life_expectancy_years": "11-16",
    },
    {
        "id": "ocicat", "name": "Ocicat", "origin": "United States", "coat": "Short",
        "temperament": "Social, playful and confident", "life_expectancy_years": "12-18",
    },
    {
        "id": "cymric", "name": "Cymric", "origin": "Isle of Man", "coat": "Long",
        "temperament": "Playful, gentle and even-tempered", "life_expectancy_years": "8-14",
    },
    {
        "id": "chartreux", "name": "Chartreux", "origin": "France", "coat": "Short",
        "temperament": "Quiet, gentle and affectionate", "life_expectancy_years": "11-15",
    },
    {
        "id": "korat", "name": "Korat", "origin": "Thailand", "coat": "Short",
        "temperament": "Affectionate, gentle and intelligent", "life_expectancy_years": "10-15",
    },
    {
        "id": "singapura", "name": "Singapura", "origin": "Singapore", "coat": "Short",
        "temperament": "Playful, curious and affectionate", "life_expectancy_years": "11-15",
    },
    {
        "id": "turkish-van", "name": "Turkish Van", "origin": "Turkey", "coat": "Long",
        "temperament": "Energetic, playful and loyal", "life_expectancy_years": "12-17",
    },
    {
        "id": "selkirk-rex", "name": "Selkirk Rex", "origin": "United States", "coat": "Long",
        "temperament": "Patient, tolerant and affectionate", "life_expectancy_years": "10-15",
    },
]
