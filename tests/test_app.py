import json

from app import handler


def test_returns_200():
    assert handler({}, None)["statusCode"] == 200


def test_has_products():
    body = json.loads(handler({}, None)["body"])
    assert len(body["products"]) >= 3
