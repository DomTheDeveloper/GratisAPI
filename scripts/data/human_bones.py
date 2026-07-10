"""Notable bones of the human skeleton with region and bone type."""

META = {
    "name": "human_bones",
    "title": "Human Bones",
    "description": "Notable bones of the human skeleton grouped by body region and bone type.",
    "emoji": "\U0001F9B4",
}

ITEMS = [
    # --- Skull ---
    {"id": "frontal-bone", "name": "Frontal bone", "latin_name": "Os frontale", "region": "Skull", "type": "Flat"},
    {"id": "parietal-bone", "name": "Parietal bone", "latin_name": "Os parietale", "region": "Skull", "type": "Flat"},
    {"id": "temporal-bone", "name": "Temporal bone", "latin_name": "Os temporale", "region": "Skull", "type": "Irregular"},
    {"id": "occipital-bone", "name": "Occipital bone", "latin_name": "Os occipitale", "region": "Skull", "type": "Flat"},
    {"id": "sphenoid-bone", "name": "Sphenoid bone", "latin_name": "Os sphenoidale", "region": "Skull", "type": "Irregular"},
    {"id": "ethmoid-bone", "name": "Ethmoid bone", "latin_name": "Os ethmoidale", "region": "Skull", "type": "Irregular"},
    {"id": "mandible", "name": "Mandible", "latin_name": "Mandibula", "region": "Skull", "type": "Irregular"},
    {"id": "maxilla", "name": "Maxilla", "latin_name": "Maxilla", "region": "Skull", "type": "Irregular"},
    {"id": "zygomatic-bone", "name": "Zygomatic bone", "latin_name": "Os zygomaticum", "region": "Skull", "type": "Irregular"},
    {"id": "nasal-bone", "name": "Nasal bone", "latin_name": "Os nasale", "region": "Skull", "type": "Flat"},
    {"id": "vomer", "name": "Vomer", "latin_name": "Vomer", "region": "Skull", "type": "Flat"},

    # --- Spine ---
    {"id": "atlas", "name": "Atlas (C1)", "latin_name": "Atlas", "region": "Spine", "type": "Irregular"},
    {"id": "axis", "name": "Axis (C2)", "latin_name": "Axis", "region": "Spine", "type": "Irregular"},
    {"id": "sacrum", "name": "Sacrum", "latin_name": "Os sacrum", "region": "Spine", "type": "Irregular"},
    {"id": "coccyx", "name": "Coccyx", "latin_name": "Os coccygis", "region": "Spine", "type": "Irregular"},

    # --- Thorax ---
    {"id": "sternum", "name": "Sternum", "latin_name": "Sternum", "region": "Thorax", "type": "Flat"},
    {"id": "rib", "name": "Rib", "latin_name": "Costa", "region": "Thorax", "type": "Flat"},
    {"id": "hyoid-bone", "name": "Hyoid bone", "latin_name": "Os hyoideum", "region": "Thorax", "type": "Irregular"},

    # --- Arm ---
    {"id": "clavicle", "name": "Clavicle", "latin_name": "Clavicula", "region": "Arm", "type": "Long"},
    {"id": "scapula", "name": "Scapula", "latin_name": "Scapula", "region": "Arm", "type": "Flat"},
    {"id": "humerus", "name": "Humerus", "latin_name": "Humerus", "region": "Arm", "type": "Long"},
    {"id": "radius", "name": "Radius", "latin_name": "Radius", "region": "Arm", "type": "Long"},
    {"id": "ulna", "name": "Ulna", "latin_name": "Ulna", "region": "Arm", "type": "Long"},

    # --- Hand ---
    {"id": "scaphoid", "name": "Scaphoid", "latin_name": "Os scaphoideum", "region": "Hand", "type": "Short"},
    {"id": "lunate", "name": "Lunate", "latin_name": "Os lunatum", "region": "Hand", "type": "Short"},
    {"id": "metacarpal", "name": "Metacarpal", "latin_name": "Os metacarpale", "region": "Hand", "type": "Long"},
    {"id": "phalanx-hand", "name": "Phalanx (finger)", "latin_name": "Phalanx", "region": "Hand", "type": "Long"},

    # --- Pelvis ---
    {"id": "ilium", "name": "Ilium", "latin_name": "Os ilium", "region": "Pelvis", "type": "Flat"},
    {"id": "ischium", "name": "Ischium", "latin_name": "Os ischii", "region": "Pelvis", "type": "Irregular"},
    {"id": "pubis", "name": "Pubis", "latin_name": "Os pubis", "region": "Pelvis", "type": "Irregular"},

    # --- Leg ---
    {"id": "femur", "name": "Femur", "latin_name": "Femur", "region": "Leg", "type": "Long"},
    {"id": "patella", "name": "Patella", "latin_name": "Patella", "region": "Leg", "type": "Sesamoid"},
    {"id": "tibia", "name": "Tibia", "latin_name": "Tibia", "region": "Leg", "type": "Long"},
    {"id": "fibula", "name": "Fibula", "latin_name": "Fibula", "region": "Leg", "type": "Long"},

    # --- Foot ---
    {"id": "calcaneus", "name": "Calcaneus", "latin_name": "Calcaneus", "region": "Foot", "type": "Short"},
    {"id": "talus", "name": "Talus", "latin_name": "Talus", "region": "Foot", "type": "Short"},
    {"id": "metatarsal", "name": "Metatarsal", "latin_name": "Os metatarsale", "region": "Foot", "type": "Long"},
    {"id": "phalanx-foot", "name": "Phalanx (toe)", "latin_name": "Phalanx", "region": "Foot", "type": "Long"},
]
