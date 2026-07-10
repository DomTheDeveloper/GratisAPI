"""The main cloud types recognized in meteorology."""

META = {
    "name": "cloud-types",
    "title": "Cloud Types",
    "description": "The principal cloud genera classified by altitude and appearance.",
    "emoji": "☁️",
}

# id, name, abbreviation, altitude_level, description
_RAW = [
    ("cirrus", "Cirrus", "Ci", "High",
     "Thin, wispy strands of ice crystals often called mare's tails."),
    ("cirrocumulus", "Cirrocumulus", "Cc", "High",
     "Small white patches or ripples of cloud, forming a mackerel sky."),
    ("cirrostratus", "Cirrostratus", "Cs", "High",
     "Transparent, whitish veil that can produce a halo around the sun or moon."),
    ("altocumulus", "Altocumulus", "Ac", "Middle",
     "White or grey layers of rounded masses, often in groups or waves."),
    ("altostratus", "Altostratus", "As", "Middle",
     "Grey or blue-grey sheet covering the sky, through which the sun appears dimly."),
    ("nimbostratus", "Nimbostratus", "Ns", "Middle",
     "Thick, dark, featureless layer producing continuous rain or snow."),
    ("stratus", "Stratus", "St", "Low",
     "Uniform grey layer resembling fog that does not reach the ground; may drizzle."),
    ("stratocumulus", "Stratocumulus", "Sc", "Low",
     "Low, lumpy layer of grey or white rounded masses with gaps of clear sky."),
    ("cumulus", "Cumulus", "Cu", "Low",
     "Detached, puffy fair-weather clouds with flat bases and cauliflower tops."),
    ("cumulonimbus", "Cumulonimbus", "Cb", "Vertical",
     "Towering thunderstorm cloud producing heavy rain, lightning, and hail."),
    ("lenticular", "Lenticular", "Ac len", "Middle",
     "Smooth, lens- or saucer-shaped clouds that form over hills and mountains."),
    ("mammatus", "Mammatus", "Cb mam", "Vertical",
     "Pouch-like bulges hanging beneath a cloud base, often after severe storms."),
    ("contrail", "Contrail", "Ci con", "High",
     "Line-shaped ice clouds formed from aircraft engine exhaust at high altitude."),
]

ITEMS = [
    {
        "id": r[0],
        "name": r[1],
        "abbreviation": r[2],
        "altitude_level": r[3],
        "description": r[4],
    }
    for r in _RAW
]
