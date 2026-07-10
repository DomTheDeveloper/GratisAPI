"""The Mohs scale of mineral hardness."""

META = {
    "name": "mohs-scale",
    "title": "Mohs Hardness Scale",
    "description": "Mineral hardness from 1 (talc) to 10 (diamond) with reference minerals.",
    "emoji": "\U0001F48E",
}

# id, hardness, mineral, description
_RAW = [
    (1, 1, "Talc", "Easily scratched by a fingernail."),
    (2, 2, "Gypsum", "Scratched by a fingernail."),
    (3, 3, "Calcite", "Scratched by a copper coin."),
    (4, 4, "Fluorite", "Easily scratched by a knife."),
    (5, 5, "Apatite", "Scratched by a knife with difficulty."),
    (6, 6, "Orthoclase feldspar", "Scratched by a steel file; scratches glass."),
    (7, 7, "Quartz", "Scratches glass and steel."),
    (8, 8, "Topaz", "Scratches quartz."),
    (9, 9, "Corundum", "Scratches topaz; includes ruby and sapphire."),
    (10, 10, "Diamond", "Hardest known natural material; scratches all others."),
]

ITEMS = [
    {
        "id": r[0],
        "hardness": r[1],
        "mineral": r[2],
        "description": r[3],
    }
    for r in _RAW
]
