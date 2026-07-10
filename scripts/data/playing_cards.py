META = {
    "name": "playing-cards",
    "title": "Playing Cards",
    "description": "A standard 52-card deck with rank, suit, color, value, and suit symbol.",
    "emoji": "🃏",
}

_SUITS = [
    ("Spades", "Black", "♠"),
    ("Hearts", "Red", "♥"),
    ("Diamonds", "Red", "♦"),
    ("Clubs", "Black", "♣"),
]

_RANKS = [
    ("Ace", 1),
    ("2", 2),
    ("3", 3),
    ("4", 4),
    ("5", 5),
    ("6", 6),
    ("7", 7),
    ("8", 8),
    ("9", 9),
    ("10", 10),
    ("Jack", 11),
    ("Queen", 12),
    ("King", 13),
]

ITEMS = []
for _suit, _color, _symbol in _SUITS:
    for _rank, _value in _RANKS:
        ITEMS.append({
            "id": "{}-of-{}".format(_rank.lower(), _suit.lower()),
            "rank": _rank,
            "suit": _suit,
            "color": _color,
            "value": _value,
            "symbol": _symbol,
        })
