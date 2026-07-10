"""Countries with capital, ISO codes, continent, currency and population."""

META = {
    "name": "countries",
    "title": "Countries",
    "description": "Countries of the world with capital, ISO codes, continent and currency.",
    "emoji": "\U0001F30D",
}

# id(alpha2 lower), name, alpha2, alpha3, capital, continent, currency_code, currency, pop_millions
_RAW = [
    ("us", "United States", "US", "USA", "Washington, D.C.", "North America", "USD", "US Dollar", 331),
    ("ca", "Canada", "CA", "CAN", "Ottawa", "North America", "CAD", "Canadian Dollar", 38),
    ("mx", "Mexico", "MX", "MEX", "Mexico City", "North America", "MXN", "Mexican Peso", 129),
    ("br", "Brazil", "BR", "BRA", "Brasilia", "South America", "BRL", "Brazilian Real", 214),
    ("ar", "Argentina", "AR", "ARG", "Buenos Aires", "South America", "ARS", "Argentine Peso", 46),
    ("gb", "United Kingdom", "GB", "GBR", "London", "Europe", "GBP", "Pound Sterling", 67),
    ("fr", "France", "FR", "FRA", "Paris", "Europe", "EUR", "Euro", 68),
    ("de", "Germany", "DE", "DEU", "Berlin", "Europe", "EUR", "Euro", 83),
    ("es", "Spain", "ES", "ESP", "Madrid", "Europe", "EUR", "Euro", 47),
    ("it", "Italy", "IT", "ITA", "Rome", "Europe", "EUR", "Euro", 59),
    ("nl", "Netherlands", "NL", "NLD", "Amsterdam", "Europe", "EUR", "Euro", 17),
    ("se", "Sweden", "SE", "SWE", "Stockholm", "Europe", "SEK", "Swedish Krona", 10),
    ("no", "Norway", "NO", "NOR", "Oslo", "Europe", "NOK", "Norwegian Krone", 5),
    ("ru", "Russia", "RU", "RUS", "Moscow", "Europe", "RUB", "Russian Ruble", 144),
    ("cn", "China", "CN", "CHN", "Beijing", "Asia", "CNY", "Renminbi", 1412),
    ("jp", "Japan", "JP", "JPN", "Tokyo", "Asia", "JPY", "Japanese Yen", 125),
    ("in", "India", "IN", "IND", "New Delhi", "Asia", "INR", "Indian Rupee", 1408),
    ("kr", "South Korea", "KR", "KOR", "Seoul", "Asia", "KRW", "South Korean Won", 52),
    ("id", "Indonesia", "ID", "IDN", "Jakarta", "Asia", "IDR", "Indonesian Rupiah", 274),
    ("sa", "Saudi Arabia", "SA", "SAU", "Riyadh", "Asia", "SAR", "Saudi Riyal", 35),
    ("ae", "United Arab Emirates", "AE", "ARE", "Abu Dhabi", "Asia", "AED", "UAE Dirham", 10),
    ("tr", "Turkey", "TR", "TUR", "Ankara", "Asia", "TRY", "Turkish Lira", 85),
    ("eg", "Egypt", "EG", "EGY", "Cairo", "Africa", "EGP", "Egyptian Pound", 109),
    ("za", "South Africa", "ZA", "ZAF", "Pretoria", "Africa", "ZAR", "South African Rand", 60),
    ("ng", "Nigeria", "NG", "NGA", "Abuja", "Africa", "NGN", "Nigerian Naira", 213),
    ("ke", "Kenya", "KE", "KEN", "Nairobi", "Africa", "KES", "Kenyan Shilling", 53),
    ("au", "Australia", "AU", "AUS", "Canberra", "Oceania", "AUD", "Australian Dollar", 26),
    ("nz", "New Zealand", "NZ", "NZL", "Wellington", "Oceania", "NZD", "New Zealand Dollar", 5),
]

ITEMS = []
for cid, name, a2, a3, cap, cont, ccode, cur, pop in _RAW:
    ITEMS.append({
        "id": cid,
        "name": name,
        "alpha2": a2,
        "alpha3": a3,
        "capital": cap,
        "continent": cont,
        "currency_code": ccode,
        "currency": cur,
        "population_millions": pop,
        "flag_emoji": "".join(chr(0x1F1E6 + ord(c) - ord("A")) for c in a2),
    })
