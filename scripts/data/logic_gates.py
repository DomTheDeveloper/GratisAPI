"""Fundamental digital logic gates with symbols, truth tables, and expressions."""

META = {
    "name": "logic_gates",
    "title": "Logic Gates",
    "description": "The fundamental digital logic gates with their symbols, truth tables, and Boolean expressions.",
    "emoji": "\U0001F50C",
}

ITEMS = [
    {
        "id": "and",
        "name": "AND",
        "symbol_text": "&",
        "inputs": 2,
        "truth_table": "Output is 1 only when both inputs are 1.",
        "boolean_expression": "Y = A · B",
    },
    {
        "id": "or",
        "name": "OR",
        "symbol_text": "≥1",
        "inputs": 2,
        "truth_table": "Output is 1 when at least one input is 1.",
        "boolean_expression": "Y = A + B",
    },
    {
        "id": "not",
        "name": "NOT",
        "symbol_text": "1",
        "inputs": 1,
        "truth_table": "Output is the inverse of the input: 1 becomes 0 and 0 becomes 1.",
        "boolean_expression": "Y = ¬A",
    },
    {
        "id": "nand",
        "name": "NAND",
        "symbol_text": "&",
        "inputs": 2,
        "truth_table": "Output is 0 only when both inputs are 1; otherwise 1.",
        "boolean_expression": "Y = ¬(A · B)",
    },
    {
        "id": "nor",
        "name": "NOR",
        "symbol_text": "≥1",
        "inputs": 2,
        "truth_table": "Output is 1 only when both inputs are 0; otherwise 0.",
        "boolean_expression": "Y = ¬(A + B)",
    },
    {
        "id": "xor",
        "name": "XOR",
        "symbol_text": "=1",
        "inputs": 2,
        "truth_table": "Output is 1 when the inputs differ.",
        "boolean_expression": "Y = A ⊕ B",
    },
    {
        "id": "xnor",
        "name": "XNOR",
        "symbol_text": "=",
        "inputs": 2,
        "truth_table": "Output is 1 when the inputs are equal.",
        "boolean_expression": "Y = ¬(A ⊕ B)",
    },
    {
        "id": "buffer",
        "name": "BUFFER",
        "symbol_text": "1",
        "inputs": 1,
        "truth_table": "Output equals the input; used to strengthen or delay a signal.",
        "boolean_expression": "Y = A",
    },
]
