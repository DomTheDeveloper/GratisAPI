"""NATO phonetic alphabet: 26 code words with pronunciation and Morse code."""

META = {
    "name": "nato_alphabet",
    "title": "NATO Phonetic Alphabet",
    "description": "The 26 NATO phonetic alphabet code words with pronunciation and Morse code.",
    "emoji": "\U0001F4E1",
}

# letter, code_word, pronunciation, morse
_RAW = [
    ("A", "Alfa", "AL-fah", ".-"),
    ("B", "Bravo", "BRAH-voh", "-..."),
    ("C", "Charlie", "CHAR-lee", "-.-."),
    ("D", "Delta", "DELL-tah", "-.."),
    ("E", "Echo", "ECK-oh", "."),
    ("F", "Foxtrot", "FOKS-trot", "..-."),
    ("G", "Golf", "GOLF", "--."),
    ("H", "Hotel", "hoh-TELL", "...."),
    ("I", "India", "IN-dee-ah", ".."),
    ("J", "Juliett", "JEW-lee-ett", ".---"),
    ("K", "Kilo", "KEY-loh", "-.-"),
    ("L", "Lima", "LEE-mah", ".-.."),
    ("M", "Mike", "MIKE", "--"),
    ("N", "November", "no-VEM-ber", "-."),
    ("O", "Oscar", "OSS-cah", "---"),
    ("P", "Papa", "pah-PAH", ".--."),
    ("Q", "Quebec", "keh-BECK", "--.-"),
    ("R", "Romeo", "ROW-me-oh", ".-."),
    ("S", "Sierra", "see-AIR-rah", "..."),
    ("T", "Tango", "TANG-go", "-"),
    ("U", "Uniform", "YOU-nee-form", "..-"),
    ("V", "Victor", "VIK-tah", "...-"),
    ("W", "Whiskey", "WISS-key", ".--"),
    ("X", "X-ray", "ECKS-ray", "-..-"),
    ("Y", "Yankee", "YANG-key", "-.--"),
    ("Z", "Zulu", "ZOO-loo", "--.."),
]

ITEMS = [
    {"id": letter.lower(), "letter": letter, "code_word": word,
     "pronunciation": pron, "morse": morse}
    for letter, word, pron, morse in _RAW
]
