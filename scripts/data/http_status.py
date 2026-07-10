"""HTTP status codes."""

META = {
    "name": "http-status",
    "title": "HTTP Status Codes",
    "description": "HTTP response status codes with their standard reason phrase and category.",
    "emoji": "\U0001F4E1",
}

_RAW = [
    (100, "Continue", "Informational"),
    (101, "Switching Protocols", "Informational"),
    (200, "OK", "Success"),
    (201, "Created", "Success"),
    (202, "Accepted", "Success"),
    (204, "No Content", "Success"),
    (206, "Partial Content", "Success"),
    (301, "Moved Permanently", "Redirection"),
    (302, "Found", "Redirection"),
    (304, "Not Modified", "Redirection"),
    (307, "Temporary Redirect", "Redirection"),
    (308, "Permanent Redirect", "Redirection"),
    (400, "Bad Request", "Client Error"),
    (401, "Unauthorized", "Client Error"),
    (403, "Forbidden", "Client Error"),
    (404, "Not Found", "Client Error"),
    (405, "Method Not Allowed", "Client Error"),
    (409, "Conflict", "Client Error"),
    (410, "Gone", "Client Error"),
    (418, "I'm a teapot", "Client Error"),
    (422, "Unprocessable Entity", "Client Error"),
    (429, "Too Many Requests", "Client Error"),
    (500, "Internal Server Error", "Server Error"),
    (501, "Not Implemented", "Server Error"),
    (502, "Bad Gateway", "Server Error"),
    (503, "Service Unavailable", "Server Error"),
    (504, "Gateway Timeout", "Server Error"),
]

ITEMS = [
    {"id": code, "code": code, "message": msg, "category": cat}
    for code, msg, cat in _RAW
]
