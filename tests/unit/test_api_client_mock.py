from unittest.mock import patch, MagicMock
from api_client import ApiClient, DEFAULT_TIMEOUT

BASE = "https://example.org"

@patch("api_client.requests.get")
def test_get_mocked_ok(mock_get):
    # Configurar respuesta falsa
    fake_resp = MagicMock()
    fake_resp.status_code = 200
    fake_resp.headers = {"content-type": "application/json; charset=utf-8"}
    fake_resp.json.return_value = [{"id": 1, "title": "mocked"}]
    mock_get.return_value = fake_resp

    client = ApiClient(BASE)
    resp = client.get("/posts")

    # Validaciones
    assert resp.status_code == 200
    assert "application/json" in resp.headers["content-type"].lower()
    assert resp.json()[0]["title"] == "mocked"

    mock_get.assert_called_once()

    # ✅ Recuperamos los argumentos pasados a la función
    called_args, called_kwargs = mock_get.call_args
    # El primer argumento posicional es la URL
    assert called_args[0] == f"{BASE}/posts"
    assert called_kwargs.get("params") is None
    assert called_kwargs.get("timeout") == DEFAULT_TIMEOUT


@patch("api_client.requests.post")
def test_post_mocked_ok(mock_post):
    fake_resp = MagicMock()
    fake_resp.status_code = 201
    fake_resp.headers = {"content-type": "application/json"}
    fake_resp.json.return_value = {"id": 101, "title": "foo"}
    mock_post.return_value = fake_resp

    client = ApiClient(BASE)
    resp = client.post("/posts", json={"title": "foo"})

    assert resp.status_code == 201
    assert resp.json()["id"] == 101
    mock_post.assert_called_once()

    # Revisar argumentos pasados
    called_args, called_kwargs = mock_post.call_args
    assert called_args[0] == f"{BASE}/posts"
    assert called_kwargs["json"]["title"] == "foo"
    assert called_kwargs.get("timeout") == DEFAULT_TIMEOUT
