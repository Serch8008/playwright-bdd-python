import requests
from typing import Any, Dict, Optional

DEFAULT_TIMEOUT = 10  # segundos

class ApiClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")

    def get(self, path: str, params: Optional[Dict[str, Any]] = None) -> requests.Response:
        url = f"{self.base_url}/{path.lstrip('/')}"
        return requests.get(url, params=params, timeout=DEFAULT_TIMEOUT)

    def post(self, path: str, json: Optional[Dict[str, Any]] = None) -> requests.Response:
        url = f"{self.base_url}/{path.lstrip('/')}"
        return requests.post(url, json=json, timeout=DEFAULT_TIMEOUT)
