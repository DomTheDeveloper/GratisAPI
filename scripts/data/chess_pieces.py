META = {
    "name": "chess-pieces",
    "title": "Chess Pieces",
    "description": "The six chess pieces with their Unicode symbols, relative point value, and movement rules.",
    "emoji": "♟️",
}

ITEMS = [
    {"id": "king", "name": "King", "symbol_white": "♔", "symbol_black": "♚", "value": None, "movement": "One square in any direction"},
    {"id": "queen", "name": "Queen", "symbol_white": "♕", "symbol_black": "♛", "value": 9, "movement": "Any number of squares horizontally, vertically, or diagonally"},
    {"id": "rook", "name": "Rook", "symbol_white": "♖", "symbol_black": "♜", "value": 5, "movement": "Any number of squares horizontally or vertically"},
    {"id": "bishop", "name": "Bishop", "symbol_white": "♗", "symbol_black": "♝", "value": 3, "movement": "Any number of squares diagonally"},
    {"id": "knight", "name": "Knight", "symbol_white": "♘", "symbol_black": "♞", "value": 3, "movement": "In an L-shape; may jump over other pieces"},
    {"id": "pawn", "name": "Pawn", "symbol_white": "♙", "symbol_black": "♟", "value": 1, "movement": "Forward one square (two on first move); captures diagonally"},
]
