"""Notable natural satellites (moons) of the Solar System."""

META = {
    "name": "moons",
    "title": "Moons",
    "description": "Notable natural satellites of the Solar System with parent planet and discovery details.",
    "emoji": "🌙",
}

# (id, name, planet, radius_km, discovered_year, discovered_by)
_ROWS = [
    ("moon", "Moon", "Earth", 1737.4, None, None),
    ("phobos", "Phobos", "Mars", 11.267, 1877, "Asaph Hall"),
    ("deimos", "Deimos", "Mars", 6.2, 1877, "Asaph Hall"),
    ("io", "Io", "Jupiter", 1821.6, 1610, "Galileo Galilei"),
    ("europa", "Europa", "Jupiter", 1560.8, 1610, "Galileo Galilei"),
    ("ganymede", "Ganymede", "Jupiter", 2634.1, 1610, "Galileo Galilei"),
    ("callisto", "Callisto", "Jupiter", 2410.3, 1610, "Galileo Galilei"),
    ("amalthea", "Amalthea", "Jupiter", 83.5, 1892, "Edward Emerson Barnard"),
    ("himalia", "Himalia", "Jupiter", 69.8, 1904, "Charles Dillon Perrine"),
    ("titan", "Titan", "Saturn", 2574.7, 1655, "Christiaan Huygens"),
    ("rhea", "Rhea", "Saturn", 763.8, 1672, "Giovanni Domenico Cassini"),
    ("iapetus", "Iapetus", "Saturn", 734.5, 1671, "Giovanni Domenico Cassini"),
    ("dione", "Dione", "Saturn", 561.4, 1684, "Giovanni Domenico Cassini"),
    ("tethys", "Tethys", "Saturn", 531.1, 1684, "Giovanni Domenico Cassini"),
    ("enceladus", "Enceladus", "Saturn", 252.1, 1789, "William Herschel"),
    ("mimas", "Mimas", "Saturn", 198.2, 1789, "William Herschel"),
    ("hyperion", "Hyperion", "Saturn", 135.0, 1848, "William Cranch Bond"),
    ("phoebe", "Phoebe", "Saturn", 106.5, 1899, "William Henry Pickering"),
    ("titania", "Titania", "Uranus", 788.4, 1787, "William Herschel"),
    ("oberon", "Oberon", "Uranus", 761.4, 1787, "William Herschel"),
    ("umbriel", "Umbriel", "Uranus", 584.7, 1851, "William Lassell"),
    ("ariel", "Ariel", "Uranus", 578.9, 1851, "William Lassell"),
    ("miranda", "Miranda", "Uranus", 235.8, 1948, "Gerard Kuiper"),
    ("triton", "Triton", "Neptune", 1353.4, 1846, "William Lassell"),
    ("nereid", "Nereid", "Neptune", 170.0, 1949, "Gerard Kuiper"),
    ("proteus", "Proteus", "Neptune", 210.0, 1989, "Voyager 2"),
    ("charon", "Charon", "Pluto", 606.0, 1978, "James Christy"),
    ("nix", "Nix", "Pluto", 24.5, 2005, "Hubble Space Telescope team"),
    ("hydra", "Hydra", "Pluto", 30.5, 2005, "Hubble Space Telescope team"),
    ("dysnomia", "Dysnomia", "Eris", 350.0, 2005, "Michael E. Brown"),
]

ITEMS = [
    {
        "id": _id,
        "name": name,
        "planet": planet,
        "radius_km": radius,
        "discovered_year": year,
        "discovered_by": by,
    }
    for (_id, name, planet, radius, year, by) in _ROWS
]
