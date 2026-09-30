import json

VERSION = "v2"

PRODUCTS = [
    {"productId": "p1", "name": "Laptop Stand", "price": 1999},
    {"productId": "p2", "name": "USB-C Hub", "price": 3299},
    {"productId": "p3", "name": "Mechanical Keyboard", "price": 4999},
]


def handler(event, context):
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"version": VERSION, "products": PRODUCTS}),
    }
