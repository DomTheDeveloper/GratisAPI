"""ABO / Rh blood types and their compatibility."""

META = {
    "name": "blood-types",
    "title": "Blood Types",
    "description": "The eight ABO/Rh blood groups with donor and recipient compatibility.",
    "emoji": "\U0001FA78",
}

# id, group, can_donate_to (list), can_receive_from (list), approx global %
_RAW = [
    ("o-negative", "O-", ["O-", "O+", "A-", "A+", "B-", "B+", "AB-", "AB+"], ["O-"], 4.0),
    ("o-positive", "O+", ["O+", "A+", "B+", "AB+"], ["O-", "O+"], 36.0),
    ("a-negative", "A-", ["A-", "A+", "AB-", "AB+"], ["O-", "A-"], 6.0),
    ("a-positive", "A+", ["A+", "AB+"], ["O-", "O+", "A-", "A+"], 28.0),
    ("b-negative", "B-", ["B-", "B+", "AB-", "AB+"], ["O-", "B-"], 2.0),
    ("b-positive", "B+", ["B+", "AB+"], ["O-", "O+", "B-", "B+"], 8.0),
    ("ab-negative", "AB-", ["AB-", "AB+"], ["O-", "A-", "B-", "AB-"], 1.0),
    ("ab-positive", "AB+", ["AB+"], ["O-", "O+", "A-", "A+", "B-", "B+", "AB-", "AB+"], 5.0),
]

ITEMS = [
    {
        "id": cid,
        "group": group,
        "can_donate_to": donate,
        "can_receive_from": receive,
        "is_universal_donor": group == "O-",
        "is_universal_recipient": group == "AB+",
        "approx_global_percent": pct,
    }
    for cid, group, donate, receive, pct in _RAW
]
