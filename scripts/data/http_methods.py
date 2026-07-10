"""HTTP request methods."""

META = {
    "name": "http-methods",
    "title": "HTTP Request Methods",
    "description": "The HTTP request methods and their safety, idempotency, and caching semantics.",
    "emoji": "\U0001F517",
}

# id, method, safe, idempotent, cacheable, has_request_body, description
_RAW = [
    ("get", "GET", True, True, True, False,
     "Requests a representation of the specified resource without modifying it."),
    ("post", "POST", False, False, False, True,
     "Submits an entity to the specified resource, often causing a change in state."),
    ("put", "PUT", False, True, False, True,
     "Replaces all current representations of the target resource with the request payload."),
    ("delete", "DELETE", False, True, False, False,
     "Deletes the specified resource."),
    ("patch", "PATCH", False, False, False, True,
     "Applies partial modifications to a resource."),
    ("head", "HEAD", True, True, True, False,
     "Identical to GET but returns only the headers without the response body."),
    ("options", "OPTIONS", True, True, False, False,
     "Describes the communication options available for the target resource."),
    ("trace", "TRACE", True, True, False, False,
     "Performs a message loop-back test along the path to the target resource."),
    ("connect", "CONNECT", False, False, False, False,
     "Establishes a tunnel to the server identified by the target resource."),
]

ITEMS = [
    {
        "id": _id,
        "method": method,
        "description": desc,
        "safe": safe,
        "idempotent": idempotent,
        "cacheable": cacheable,
        "has_request_body": has_body,
    }
    for _id, method, safe, idempotent, cacheable, has_body, desc in _RAW
]
