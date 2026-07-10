"""The human senses, including the classic five and additional senses."""

META = {
    "name": "human_senses",
    "title": "Human Senses",
    "description": "The human senses, including the classic five plus balance, proprioception, and more.",
    "emoji": "\U0001F441",
}

ITEMS = [
    {"id": "sight", "name": "Sight (vision)", "organ": "Eyes", "description": "Detection of light, color, and motion to perceive the visual world.", "type": "Classic"},
    {"id": "hearing", "name": "Hearing (audition)", "organ": "Ears", "description": "Detection of sound waves as vibrations in the air.", "type": "Classic"},
    {"id": "smell", "name": "Smell (olfaction)", "organ": "Nose", "description": "Detection of airborne chemical molecules to perceive odors.", "type": "Classic"},
    {"id": "taste", "name": "Taste (gustation)", "organ": "Tongue", "description": "Detection of dissolved chemicals to perceive sweet, sour, salty, bitter, and umami.", "type": "Classic"},
    {"id": "touch", "name": "Touch (tactition)", "organ": "Skin", "description": "Detection of pressure, vibration, and texture through the skin.", "type": "Classic"},
    {"id": "balance", "name": "Balance (equilibrioception)", "organ": "Vestibular system of the inner ear", "description": "Sense of body orientation, acceleration, and equilibrium.", "type": "Other"},
    {"id": "proprioception", "name": "Proprioception", "organ": "Muscles and joints", "description": "Awareness of the position and movement of the body's parts.", "type": "Other"},
    {"id": "temperature", "name": "Temperature (thermoception)", "organ": "Skin", "description": "Detection of heat and cold through thermoreceptors.", "type": "Other"},
    {"id": "pain", "name": "Pain (nociception)", "organ": "Nociceptors throughout the body", "description": "Detection of harmful or damaging stimuli to protect the body.", "type": "Other"},
]
