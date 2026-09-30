import json

VERSION = "v1"

PRODUCTS = [
    {"productId": "p1", "name": "Laptop Stand", "price": 1499},
    {"productId": "p2", "name": "USB-C Hub", "price": 2499},
    {"productId": "p3", "name": "Mechanical Keyboard", "price": 3999},
]


def handler(event, context):
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"version": VERSION, "products": PRODUCTS}),
    }
