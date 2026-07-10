"""Named CSS/web colors with hex and RGB values."""

META = {
    "name": "colors",
    "title": "Colors",
    "description": "Named web colors with hex, RGB and HSL values.",
    "emoji": "\U0001F3A8",
}

# (id, name, hex) -- full set of CSS/X11 named colors
_RAW = [
    ("aliceblue", "Alice Blue", "#F0F8FF"),
    ("antiquewhite", "Antique White", "#FAEBD7"),
    ("aqua", "Aqua", "#00FFFF"),
    ("aquamarine", "Aquamarine", "#7FFFD4"),
    ("azure", "Azure", "#F0FFFF"),
    ("beige", "Beige", "#F5F5DC"),
    ("bisque", "Bisque", "#FFE4C4"),
    ("black", "Black", "#000000"),
    ("blanchedalmond", "Blanched Almond", "#FFEBCD"),
    ("blue", "Blue", "#0000FF"),
    ("blueviolet", "Blue Violet", "#8A2BE2"),
    ("brown", "Brown", "#A52A2A"),
    ("burlywood", "Burly Wood", "#DEB887"),
    ("cadetblue", "Cadet Blue", "#5F9EA0"),
    ("chartreuse", "Chartreuse", "#7FFF00"),
    ("chocolate", "Chocolate", "#D2691E"),
    ("coral", "Coral", "#FF7F50"),
    ("cornflowerblue", "Cornflower Blue", "#6495ED"),
    ("cornsilk", "Cornsilk", "#FFF8DC"),
    ("crimson", "Crimson", "#DC143C"),
    ("cyan", "Cyan", "#00FFFF"),
    ("darkblue", "Dark Blue", "#00008B"),
    ("darkcyan", "Dark Cyan", "#008B8B"),
    ("darkgoldenrod", "Dark Goldenrod", "#B8860B"),
    ("darkgray", "Dark Gray", "#A9A9A9"),
    ("darkgreen", "Dark Green", "#006400"),
    ("darkkhaki", "Dark Khaki", "#BDB76B"),
    ("darkmagenta", "Dark Magenta", "#8B008B"),
    ("darkolivegreen", "Dark Olive Green", "#556B2F"),
    ("darkorange", "Dark Orange", "#FF8C00"),
    ("darkorchid", "Dark Orchid", "#9932CC"),
    ("darkred", "Dark Red", "#8B0000"),
    ("darksalmon", "Dark Salmon", "#E9967A"),
    ("darkseagreen", "Dark Sea Green", "#8FBC8F"),
    ("darkslateblue", "Dark Slate Blue", "#483D8B"),
    ("darkslategray", "Dark Slate Gray", "#2F4F4F"),
    ("darkturquoise", "Dark Turquoise", "#00CED1"),
    ("darkviolet", "Dark Violet", "#9400D3"),
    ("deeppink", "Deep Pink", "#FF1493"),
    ("deepskyblue", "Deep Sky Blue", "#00BFFF"),
    ("dimgray", "Dim Gray", "#696969"),
    ("dodgerblue", "Dodger Blue", "#1E90FF"),
    ("firebrick", "Fire Brick", "#B22222"),
    ("floralwhite", "Floral White", "#FFFAF0"),
    ("forestgreen", "Forest Green", "#228B22"),
    ("fuchsia", "Fuchsia", "#FF00FF"),
    ("gainsboro", "Gainsboro", "#DCDCDC"),
    ("ghostwhite", "Ghost White", "#F8F8FF"),
    ("gold", "Gold", "#FFD700"),
    ("goldenrod", "Goldenrod", "#DAA520"),
    ("gray", "Gray", "#808080"),
    ("green", "Green", "#008000"),
    ("greenyellow", "Green Yellow", "#ADFF2F"),
    ("honeydew", "Honeydew", "#F0FFF0"),
    ("hotpink", "Hot Pink", "#FF69B4"),
    ("indianred", "Indian Red", "#CD5C5C"),
    ("indigo", "Indigo", "#4B0082"),
    ("ivory", "Ivory", "#FFFFF0"),
    ("khaki", "Khaki", "#F0E68C"),
    ("lavender", "Lavender", "#E6E6FA"),
    ("lavenderblush", "Lavender Blush", "#FFF0F5"),
    ("lawngreen", "Lawn Green", "#7CFC00"),
    ("lemonchiffon", "Lemon Chiffon", "#FFFACD"),
    ("lightblue", "Light Blue", "#ADD8E6"),
    ("lightcoral", "Light Coral", "#F08080"),
    ("lightcyan", "Light Cyan", "#E0FFFF"),
    ("lightgoldenrodyellow", "Light Goldenrod Yellow", "#FAFAD2"),
    ("lightgray", "Light Gray", "#D3D3D3"),
    ("lightgreen", "Light Green", "#90EE90"),
    ("lightpink", "Light Pink", "#FFB6C1"),
    ("lightsalmon", "Light Salmon", "#FFA07A"),
    ("lightseagreen", "Light Sea Green", "#20B2AA"),
    ("lightskyblue", "Light Sky Blue", "#87CEFA"),
    ("lightslategray", "Light Slate Gray", "#778899"),
    ("lightsteelblue", "Light Steel Blue", "#B0C4DE"),
    ("lightyellow", "Light Yellow", "#FFFFE0"),
    ("lime", "Lime", "#00FF00"),
    ("limegreen", "Lime Green", "#32CD32"),
    ("linen", "Linen", "#FAF0E6"),
    ("magenta", "Magenta", "#FF00FF"),
    ("maroon", "Maroon", "#800000"),
    ("mediumaquamarine", "Medium Aquamarine", "#66CDAA"),
    ("mediumblue", "Medium Blue", "#0000CD"),
    ("mediumorchid", "Medium Orchid", "#BA55D3"),
    ("mediumpurple", "Medium Purple", "#9370DB"),
    ("mediumseagreen", "Medium Sea Green", "#3CB371"),
    ("mediumslateblue", "Medium Slate Blue", "#7B68EE"),
    ("mediumspringgreen", "Medium Spring Green", "#00FA9A"),
    ("mediumturquoise", "Medium Turquoise", "#48D1CC"),
    ("mediumvioletred", "Medium Violet Red", "#C71585"),
    ("midnightblue", "Midnight Blue", "#191970"),
    ("mintcream", "Mint Cream", "#F5FFFA"),
    ("mistyrose", "Misty Rose", "#FFE4E1"),
    ("moccasin", "Moccasin", "#FFE4B5"),
    ("navajowhite", "Navajo White", "#FFDEAD"),
    ("navy", "Navy", "#000080"),
    ("oldlace", "Old Lace", "#FDF5E6"),
    ("olive", "Olive", "#808000"),
    ("olivedrab", "Olive Drab", "#6B8E23"),
    ("orange", "Orange", "#FFA500"),
    ("orangered", "Orange Red", "#FF4500"),
    ("orchid", "Orchid", "#DA70D6"),
    ("palegoldenrod", "Pale Goldenrod", "#EEE8AA"),
    ("palegreen", "Pale Green", "#98FB98"),
    ("paleturquoise", "Pale Turquoise", "#AFEEEE"),
    ("palevioletred", "Pale Violet Red", "#DB7093"),
    ("papayawhip", "Papaya Whip", "#FFEFD5"),
    ("peachpuff", "Peach Puff", "#FFDAB9"),
    ("peru", "Peru", "#CD853F"),
    ("pink", "Pink", "#FFC0CB"),
    ("plum", "Plum", "#DDA0DD"),
    ("powderblue", "Powder Blue", "#B0E0E6"),
    ("purple", "Purple", "#800080"),
    ("rebeccapurple", "Rebecca Purple", "#663399"),
    ("red", "Red", "#FF0000"),
    ("rosybrown", "Rosy Brown", "#BC8F8F"),
    ("royalblue", "Royal Blue", "#4169E1"),
    ("saddlebrown", "Saddle Brown", "#8B4513"),
    ("salmon", "Salmon", "#FA8072"),
    ("sandybrown", "Sandy Brown", "#F4A460"),
    ("seagreen", "Sea Green", "#2E8B57"),
    ("seashell", "Seashell", "#FFF5EE"),
    ("sienna", "Sienna", "#A0522D"),
    ("silver", "Silver", "#C0C0C0"),
    ("skyblue", "Sky Blue", "#87CEEB"),
    ("slateblue", "Slate Blue", "#6A5ACD"),
    ("slategray", "Slate Gray", "#708090"),
    ("snow", "Snow", "#FFFAFA"),
    ("springgreen", "Spring Green", "#00FF7F"),
    ("steelblue", "Steel Blue", "#4682B4"),
    ("tan", "Tan", "#D2B48C"),
    ("teal", "Teal", "#008080"),
    ("thistle", "Thistle", "#D8BFD8"),
    ("tomato", "Tomato", "#FF6347"),
    ("turquoise", "Turquoise", "#40E0D0"),
    ("violet", "Violet", "#EE82EE"),
    ("wheat", "Wheat", "#F5DEB3"),
    ("white", "White", "#FFFFFF"),
    ("whitesmoke", "White Smoke", "#F5F5F5"),
    ("yellow", "Yellow", "#FFFF00"),
    ("yellowgreen", "Yellow Green", "#9ACD32"),
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
