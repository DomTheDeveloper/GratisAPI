"""World currencies (ISO 4217 subset)."""

META = {
    "name": "currencies",
    "title": "Currencies",
    "description": "World currencies with ISO 4217 code, symbol and minor unit.",
    "emoji": "\U0001F4B1",
}

_RAW = [
    ("USD", "United States Dollar", "$", 2),
    ("EUR", "Euro", "€", 2),
    ("JPY", "Japanese Yen", "¥", 0),
    ("GBP", "Pound Sterling", "£", 2),
    ("AUD", "Australian Dollar", "$", 2),
    ("CAD", "Canadian Dollar", "$", 2),
    ("CHF", "Swiss Franc", "Fr", 2),
    ("CNY", "Renminbi", "¥", 2),
    ("HKD", "Hong Kong Dollar", "$", 2),
    ("NZD", "New Zealand Dollar", "$", 2),
    ("SEK", "Swedish Krona", "kr", 2),
    ("KRW", "South Korean Won", "₩", 0),
    ("SGD", "Singapore Dollar", "$", 2),
    ("NOK", "Norwegian Krone", "kr", 2),
    ("MXN", "Mexican Peso", "$", 2),
    ("INR", "Indian Rupee", "₹", 2),
    ("RUB", "Russian Ruble", "₽", 2),
    ("ZAR", "South African Rand", "R", 2),
    ("BRL", "Brazilian Real", "R$", 2),
    ("TRY", "Turkish Lira", "₺", 2),
    ("AED", "UAE Dirham", "د.إ", 2),
    ("SAR", "Saudi Riyal", "﷼", 2),
    ("PLN", "Polish Zloty", "zł", 2),
    ("THB", "Thai Baht", "฿", 2),
    ("IDR", "Indonesian Rupiah", "Rp", 2),
]

ITEMS = [
    {"id": code, "code": code, "name": name, "symbol": sym, "minor_unit": minor}
    for code, name, sym, minor in _RAW
]
