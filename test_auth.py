import requests

def test_auth_returns_token():
    url = "https://restful-booker.herokuapp.com/auth"
    payload = {"username": "admin", "password": "password123"}
    r = requests.post(url, json= payload, timeout=10)
    assert r.status_code == 200, f"status {r.status.code}, body {r.text}"
    assert "token" in r.json(), f"no token in {r.text}"
    print("TOKEN:", r.json()["token"])

import pytest
@pytest.mark.parametrize("payload", [
    {"username": "admin", "password": "wrong"},
    {"username": "admin"},
    {},
])
def test_auth_negative(payload):
    import requests
    r = requests.post("https://restful-booker.herokuapp.com/auth", json=payload, timeout=10)
    assert r.status_code != 200 or "token" not in r.json(), f"должен быть отказ, а пришло {r.text}"