"""Dog breeds: group, origin, size, life expectancy and temperament."""

META = {
    "name": "dog_breeds",
    "title": "Dog Breeds",
    "description": "Popular dog breeds with breed group, country of origin, size and temperament.",
    "emoji": "\U0001F415",
}

ITEMS = [
    {
        "id": "labrador-retriever", "name": "Labrador Retriever", "group": "Sporting",
        "origin": "Canada", "size": "Large", "life_expectancy_years": "10-12",
        "temperament": "Friendly, active and outgoing",
    },
    {
        "id": "german-shepherd", "name": "German Shepherd", "group": "Herding",
        "origin": "Germany", "size": "Large", "life_expectancy_years": "9-13",
        "temperament": "Confident, courageous and smart",
    },
    {
        "id": "golden-retriever", "name": "Golden Retriever", "group": "Sporting",
        "origin": "United Kingdom", "size": "Large", "life_expectancy_years": "10-12",
        "temperament": "Intelligent, friendly and devoted",
    },
    {
        "id": "french-bulldog", "name": "French Bulldog", "group": "Non-Sporting",
        "origin": "France", "size": "Small", "life_expectancy_years": "10-12",
        "temperament": "Playful, adaptable and alert",
    },
    {
        "id": "bulldog", "name": "Bulldog", "group": "Non-Sporting",
        "origin": "United Kingdom", "size": "Medium", "life_expectancy_years": "8-10",
        "temperament": "Calm, courageous and friendly",
    },
    {
        "id": "poodle", "name": "Poodle", "group": "Non-Sporting",
        "origin": "Germany", "size": "Medium", "life_expectancy_years": "10-18",
        "temperament": "Active, proud and very smart",
    },
    {
        "id": "beagle", "name": "Beagle", "group": "Hound",
        "origin": "United Kingdom", "size": "Small", "life_expectancy_years": "10-15",
        "temperament": "Curious, merry and friendly",
    },
    {
        "id": "rottweiler", "name": "Rottweiler", "group": "Working",
        "origin": "Germany", "size": "Large", "life_expectancy_years": "9-10",
        "temperament": "Loyal, loving and confident guardian",
    },
    {
        "id": "german-shorthaired-pointer", "name": "German Shorthaired Pointer", "group": "Sporting",
        "origin": "Germany", "size": "Large", "life_expectancy_years": "10-12",
        "temperament": "Friendly, smart and willing to please",
    },
    {
        "id": "dachshund", "name": "Dachshund", "group": "Hound",
        "origin": "Germany", "size": "Small", "life_expectancy_years": "12-16",
        "temperament": "Spunky, curious and friendly",
    },
    {
        "id": "pembroke-welsh-corgi", "name": "Pembroke Welsh Corgi", "group": "Herding",
        "origin": "United Kingdom", "size": "Small", "life_expectancy_years": "12-13",
        "temperament": "Affectionate, smart and alert",
    },
    {
        "id": "australian-shepherd", "name": "Australian Shepherd", "group": "Herding",
        "origin": "United States", "size": "Medium", "life_expectancy_years": "12-15",
        "temperament": "Smart, work-oriented and exuberant",
    },
    {
        "id": "yorkshire-terrier", "name": "Yorkshire Terrier", "group": "Toy",
        "origin": "United Kingdom", "size": "Small", "life_expectancy_years": "11-15",
        "temperament": "Affectionate, sprightly and tomboyish",
    },
    {
        "id": "boxer", "name": "Boxer", "group": "Working",
        "origin": "Germany", "size": "Large", "life_expectancy_years": "10-12",
        "temperament": "Bright, fun-loving and active",
    },
    {
        "id": "cavalier-king-charles-spaniel", "name": "Cavalier King Charles Spaniel", "group": "Toy",
        "origin": "United Kingdom", "size": "Small", "life_expectancy_years": "12-15",
        "temperament": "Affectionate, gentle and graceful",
    },
    {
        "id": "siberian-husky", "name": "Siberian Husky", "group": "Working",
        "origin": "Russia", "size": "Medium", "life_expectancy_years": "12-14",
        "temperament": "Loyal, outgoing and mischievous",
    },
    {
        "id": "great-dane", "name": "Great Dane", "group": "Working",
        "origin": "Germany", "size": "Large", "life_expectancy_years": "7-10",
        "temperament": "Friendly, patient and dependable",
    },
    {
        "id": "doberman-pinscher", "name": "Doberman Pinscher", "group": "Working",
        "origin": "Germany", "size": "Large", "life_expectancy_years": "10-12",
        "temperament": "Loyal, fearless and alert",
    },
    {
        "id": "cane-corso", "name": "Cane Corso", "group": "Working",
        "origin": "Italy", "size": "Large", "life_expectancy_years": "9-12",
        "temperament": "Affectionate, majestic and intelligent",
    },
    {
        "id": "miniature-schnauzer", "name": "Miniature Schnauzer", "group": "Terrier",
        "origin": "Germany", "size": "Small", "life_expectancy_years": "12-15",
        "temperament": "Friendly, smart and obedient",
    },
    {
        "id": "shih-tzu", "name": "Shih Tzu", "group": "Toy",
        "origin": "China", "size": "Small", "life_expectancy_years": "10-18",
        "temperament": "Affectionate, playful and outgoing",
    },
    {
        "id": "boston-terrier", "name": "Boston Terrier", "group": "Non-Sporting",
        "origin": "United States", "size": "Small", "life_expectancy_years": "11-13",
        "temperament": "Friendly, bright and amusing",
    },
    {
        "id": "bernese-mountain-dog", "name": "Bernese Mountain Dog", "group": "Working",
        "origin": "Switzerland", "size": "Large", "life_expectancy_years": "7-10",
        "temperament": "Good-natured, calm and strong",
    },
    {
        "id": "pomeranian", "name": "Pomeranian", "group": "Toy",
        "origin": "Germany", "size": "Small", "life_expectancy_years": "12-16",
        "temperament": "Inquisitive, bold and lively",
    },
    {
        "id": "havanese", "name": "Havanese", "group": "Toy",
        "origin": "Cuba", "size": "Small", "life_expectancy_years": "14-16",
        "temperament": "Intelligent, outgoing and funny",
    },
    {
        "id": "shetland-sheepdog", "name": "Shetland Sheepdog", "group": "Herding",
        "origin": "United Kingdom", "size": "Small", "life_expectancy_years": "12-14",
        "temperament": "Playful, energetic and bright",
    },
    {
        "id": "border-collie", "name": "Border Collie", "group": "Herding",
        "origin": "United Kingdom", "size": "Medium", "life_expectancy_years": "12-15",
        "temperament": "Energetic, smart and work-oriented",
    },
    {
        "id": "brittany", "name": "Brittany", "group": "Sporting",
        "origin": "France", "size": "Medium", "life_expectancy_years": "12-14",
        "temperament": "Bright, fun-loving and upbeat",
    },
    {
        "id": "english-springer-spaniel", "name": "English Springer Spaniel", "group": "Sporting",
        "origin": "United Kingdom", "size": "Medium", "life_expectancy_years": "12-14",
        "temperament": "Friendly, playful and obedient",
    },
    {
        "id": "cocker-spaniel", "name": "Cocker Spaniel", "group": "Sporting",
        "origin": "United States", "size": "Medium", "life_expectancy_years": "10-14",
        "temperament": "Gentle, smart and happy",
    },
    {
        "id": "mastiff", "name": "Mastiff", "group": "Working",
        "origin": "United Kingdom", "size": "Large", "life_expectancy_years": "6-10",
        "temperament": "Courageous, dignified and good-natured",
    },
    {
        "id": "chihuahua", "name": "Chihuahua", "group": "Toy",
        "origin": "Mexico", "size": "Small", "life_expectancy_years": "14-16",
        "temperament": "Charming, graceful and sassy",
    },
    {
        "id": "vizsla", "name": "Vizsla", "group": "Sporting",
        "origin": "Hungary", "size": "Medium", "life_expectancy_years": "12-14",
        "temperament": "Affectionate, energetic and gentle",
    },
    {
        "id": "weimaraner", "name": "Weimaraner", "group": "Sporting",
        "origin": "Germany", "size": "Large", "life_expectancy_years": "10-13",
        "temperament": "Friendly, fearless and obedient",
    },
    {
        "id": "collie", "name": "Collie", "group": "Herding",
        "origin": "United Kingdom", "size": "Large", "life_expectancy_years": "12-14",
        "temperament": "Devoted, graceful and proud",
    },
    {
        "id": "newfoundland", "name": "Newfoundland", "group": "Working",
        "origin": "Canada", "size": "Large", "life_expectancy_years": "9-10",
        "temperament": "Sweet, patient and devoted",
    },
    {
        "id": "basset-hound", "name": "Basset Hound", "group": "Hound",
        "origin": "France", "size": "Medium", "life_expectancy_years": "12-13",
        "temperament": "Charming, patient and low-key",
    },
    {
        "id": "bloodhound", "name": "Bloodhound", "group": "Hound",
        "origin": "Belgium", "size": "Large", "life_expectancy_years": "10-12",
        "temperament": "Friendly, independent and inquisitive",
    },
    {
        "id": "whippet", "name": "Whippet", "group": "Hound",
        "origin": "United Kingdom", "size": "Medium", "life_expectancy_years": "12-15",
        "temperament": "Affectionate, playful and calm",
    },
    {
        "id": "rhodesian-ridgeback", "name": "Rhodesian Ridgeback", "group": "Hound",
        "origin": "Zimbabwe", "size": "Large", "life_expectancy_years": "10-12",
        "temperament": "Affectionate, dignified and even-tempered",
    },
    {
        "id": "west-highland-white-terrier", "name": "West Highland White Terrier", "group": "Terrier",
        "origin": "United Kingdom", "size": "Small", "life_expectancy_years": "13-15",
        "temperament": "Loyal, happy and entertaining",
    },
    {
        "id": "scottish-terrier", "name": "Scottish Terrier", "group": "Terrier",
        "origin": "United Kingdom", "size": "Small", "life_expectancy_years": "12-15",
        "temperament": "Confident, independent and spirited",
    },
    {
        "id": "airedale-terrier", "name": "Airedale Terrier", "group": "Terrier",
        "origin": "United Kingdom", "size": "Large", "life_expectancy_years": "11-14",
        "temperament": "Friendly, clever and courageous",
    },
    {
        "id": "bull-terrier", "name": "Bull Terrier", "group": "Terrier",
        "origin": "United Kingdom", "size": "Medium", "life_expectancy_years": "12-13",
        "temperament": "Playful, charming and mischievous",
    },
    {
        "id": "akita", "name": "Akita", "group": "Working",
        "origin": "Japan", "size": "Large", "life_expectancy_years": "10-13",
        "temperament": "Courageous, dignified and loyal",
    },
    {
        "id": "shiba-inu", "name": "Shiba Inu", "group": "Non-Sporting",
        "origin": "Japan", "size": "Small", "life_expectancy_years": "13-16",
        "temperament": "Alert, active and attentive",
    },
    {
        "id": "samoyed", "name": "Samoyed", "group": "Working",
        "origin": "Russia", "size": "Medium", "life_expectancy_years": "12-14",
        "temperament": "Adaptable, friendly and gentle",
    },
    {
        "id": "alaskan-malamute", "name": "Alaskan Malamute", "group": "Working",
        "origin": "United States", "size": "Large", "life_expectancy_years": "10-14",
        "temperament": "Affectionate, loyal and playful",
    },
    {
        "id": "maltese", "name": "Maltese", "group": "Toy",
        "origin": "Malta", "size": "Small", "life_expectancy_years": "12-15",
        "temperament": "Gentle, playful and charming",
    },
    {
        "id": "papillon", "name": "Papillon", "group": "Toy",
        "origin": "France", "size": "Small", "life_expectancy_years": "14-16",
        "temperament": "Friendly, alert and happy",
    },
    {
        "id": "great-pyrenees", "name": "Great Pyrenees", "group": "Working",
        "origin": "France", "size": "Large", "life_expectancy_years": "10-12",
        "temperament": "Smart, patient and calm",
    },
]
