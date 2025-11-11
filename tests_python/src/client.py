


import requests
from typing import Dict, Any, Optional


class ApiClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")

    def create(self, payload: Dict[str, Any]) -> requests.Response:
        return requests.post(f"{self.base_url}/api/create", json=payload)

    def get(self, entity_id: int | str) -> requests.Response:
        return requests.get(f"{self.base_url}/api/get/{entity_id}")

    def get_all(self,
                title: Optional[str] = None,
                verified: Optional[bool] = None,
                page: Optional[int] = None,
                per_page: Optional[int] = None) -> requests.Response:
        params = {}
        if title is not None:
            params["title"] = title
        if verified is not None:
            params["verified"] = str(verified).lower()
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["perPage"] = per_page
        return requests.get(f"{self.base_url}/api/getAll", params=params)

    def patch(self, entity_id: int | str, payload: Dict[str, Any]) -> requests.Response:
        return requests.patch(f"{self.base_url}/api/patch/{entity_id}", json=payload)

    def delete(self, entity_id: int | str) -> requests.Response:
        return requests.delete(f"{self.base_url}/api/delete/{entity_id}")