"""Named CSS/web colors with hex and RGB values."""

META = {
    "name": "colors",
    "title": "Colors",
    "description": "Named web colors with hex, RGB and HSL values.",
    "emoji": "\U0001F3A8",
}

# (id, name, hex)
_RAW = [
    ("black", "Black", "#000000"),
    ("white", "White", "#FFFFFF"),
    ("red", "Red", "#FF0000"),
    ("lime", "Lime", "#00FF00"),
    ("blue", "Blue", "#0000FF"),
    ("yellow", "Yellow", "#FFFF00"),
    ("cyan", "Cyan", "#00FFFF"),
    ("magenta", "Magenta", "#FF00FF"),
    ("silver", "Silver", "#C0C0C0"),
    ("gray", "Gray", "#808080"),
    ("maroon", "Maroon", "#800000"),
    ("olive", "Olive", "#808000"),
    ("green", "Green", "#008000"),
    ("purple", "Purple", "#800080"),
    ("teal", "Teal", "#008080"),
    ("navy", "Navy", "#000080"),
    ("orange", "Orange", "#FFA500"),
    ("gold", "Gold", "#FFD700"),
    ("pink", "Pink", "#FFC0CB"),
    ("crimson", "Crimson", "#DC143C"),
    ("indigo", "Indigo", "#4B0082"),
    ("violet", "Violet", "#EE82EE"),
    ("turquoise", "Turquoise", "#40E0D0"),
    ("salmon", "Salmon", "#FA8072"),
    ("coral", "Coral", "#FF7F50"),
    ("tomato", "Tomato", "#FF6347"),
    ("chocolate", "Chocolate", "#D2691E"),
    ("brown", "Brown", "#A52A2A"),
    ("tan", "Tan", "#D2B48C"),
    ("beige", "Beige", "#F5F5DC"),
    ("ivory", "Ivory", "#FFFFF0"),
    ("khaki", "Khaki", "#F0E68C"),
    ("lavender", "Lavender", "#E6E6FA"),
    ("plum", "Plum", "#DDA0DD"),
    ("orchid", "Orchid", "#DA70D6"),
    ("skyblue", "Sky Blue", "#87CEEB"),
    ("royalblue", "Royal Blue", "#4169E1"),
    ("steelblue", "Steel Blue", "#4682B4"),
    ("forestgreen", "Forest Green", "#228B22"),
    ("seagreen", "Sea Green", "#2E8B57"),
]


def _hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def _rgb_to_hsl(r, g, b):
    r, g, b = r / 255, g / 255, b / 255
    mx, mn = max(r, g, b), min(r, g, b)
    l = (mx + mn) / 2
    if mx == mn:
        h = s = 0.0
    else:
        d = mx - mn
        s = d / (2 - mx - mn) if l > 0.5 else d / (mx + mn)
        if mx == r:
            h = (g - b) / d + (6 if g < b else 0)
        elif mx == g:
            h = (b - r) / d + 2
        else:
            h = (r - g) / d + 4
        h /= 6
    return round(h * 360), round(s * 100), round(l * 100)


ITEMS = []
for cid, name, hexval in _RAW:
    r, g, b = _hex_to_rgb(hexval)
    hh, ss, ll = _rgb_to_hsl(r, g, b)
    ITEMS.append({
        "id": cid,
        "name": name,
        "hex": hexval,
        "rgb": {"r": r, "g": g, "b": b},
        "rgb_string": f"rgb({r}, {g}, {b})",
        "hsl": {"h": hh, "s": ss, "l": ll},
        "hsl_string": f"hsl({hh}, {ss}%, {ll}%)",
    })
