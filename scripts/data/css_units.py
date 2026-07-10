"""CSS length and value units."""

META = {
    "name": "css-units",
    "title": "CSS Units",
    "description": "CSS units for length, angle, time, and viewport measurements.",
    "emoji": "\U0001F4D0",
}

# id, unit, type, description
_RAW = [
    ("px", "px", "Absolute",
     "Pixels; one device-independent pixel, the most common absolute unit."),
    ("cm", "cm", "Absolute",
     "Centimeters; a physical length unit."),
    ("mm", "mm", "Absolute",
     "Millimeters; one tenth of a centimeter."),
    ("in", "in", "Absolute",
     "Inches; equal to 96px."),
    ("pt", "pt", "Absolute",
     "Points; equal to 1/72 of an inch, common in print."),
    ("pc", "pc", "Absolute",
     "Picas; equal to 12 points or 1/6 of an inch."),
    ("em", "em", "Relative",
     "Relative to the font size of the current element."),
    ("rem", "rem", "Relative",
     "Relative to the font size of the root (html) element."),
    ("ex", "ex", "Relative",
     "Relative to the x-height of the current font."),
    ("ch", "ch", "Relative",
     "Relative to the width of the '0' glyph in the current font."),
    ("percent", "%", "Relative",
     "Relative to the parent element's corresponding value."),
    ("vw", "vw", "Viewport",
     "One percent of the viewport's width."),
    ("vh", "vh", "Viewport",
     "One percent of the viewport's height."),
    ("vmin", "vmin", "Viewport",
     "One percent of the viewport's smaller dimension."),
    ("vmax", "vmax", "Viewport",
     "One percent of the viewport's larger dimension."),
    ("deg", "deg", "Angle",
     "Degrees; a full circle is 360deg."),
    ("rad", "rad", "Angle",
     "Radians; a full circle is 2π radians."),
    ("grad", "grad", "Angle",
     "Gradians; a full circle is 400grad."),
    ("turn", "turn", "Angle",
     "Turns; one turn equals a full 360-degree circle."),
    ("s", "s", "Time",
     "Seconds; used for animation and transition durations."),
    ("ms", "ms", "Time",
     "Milliseconds; one thousandth of a second."),
]

ITEMS = [
    {
        "id": _id,
        "unit": unit,
        "type": _type,
        "description": desc,
    }
    for _id, unit, _type, desc in _RAW
]
