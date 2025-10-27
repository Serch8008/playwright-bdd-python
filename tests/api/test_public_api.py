import json
from api_client import ApiClient

BASE = "https://jsonplaceholder.typicode.com"

def test_get_posts_ok():
    client = ApiClient(BASE)
    resp = client.get("/posts")
    # status code
    assert resp.status_code == 200
    # headers básicos
    assert "content-type" in resp.headers
    assert "application/json" in resp.headers["content-type"].lower()
    # json válido
    data = resp.json()
    assert isinstance(data, list)
    assert len(data) > 0
    # campos mínimos
    first = data[0]
    for key in ("userId", "id", "title", "body"):
        assert key in first

def test_post_create_ok():
    client = ApiClient(BASE)
    payload = {"title": "foo", "body": "bar", "userId": 1}
    resp = client.post("/posts", json=payload)
    assert resp.status_code in (200, 201)  # jsonplaceholder devuelve 201
    data = resp.json()
    # eco de la data + id generado
    assert data["title"] == "foo"
    assert "id" in data
