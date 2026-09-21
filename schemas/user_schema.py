geo_schema = {
    "type": "object",
    "properties": {
        "lat": {"type": "string"},
        "lng": {"type": "string"}
    },
    "required": ["lat", "lng"],
    "additionalProperties": False
}


address_schema = {
    "type": "object",
    "properties": {
        "street": {"type": "string"},
        "suite": {"type": "string"},
        "city": {"type": "string"},
        "zipcode": {"type": "string"},
        "geo": geo_schema
    },
    "required": [
        "street",
        "suite",
        "city",
        "zipcode",
        "geo"
    ],
    "additionalProperties": False
}


company_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "catchPhrase": {"type": "string"},
        "bs": {"type": "string"}
    },
    "required": [
        "name",
        "catchPhrase",
        "bs"
    ],
    "additionalProperties": False
}


user_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "username": {"type": "string"},
        "email": {"type": "string"},
        "address": address_schema,
        "phone": {"type": "string"},
        "website": {"type": "string"},
        "company": company_schema
    },
    "required": [
        "id",
        "name",
        "username",
        "email",
        "address",
        "phone",
        "website",
        "company"
    ],
    "additionalProperties": False
}


users_schema = {
    "type": "array",
    "items": user_schema
}