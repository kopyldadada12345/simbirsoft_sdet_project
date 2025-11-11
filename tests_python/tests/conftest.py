
import pytest
from src.client import ApiClient
from src.models import EntityRequest, Entity
import json


@pytest.fixture(scope="session")
def base_url() -> str:
    return "http://localhost:8080"


@pytest.fixture(scope="session")
def api_client(base_url: str) -> ApiClient:
    return ApiClient(base_url)


@pytest.fixture(scope="function")
def entity_payload() -> dict:
    request_model = EntityRequest(
        title="Заголовок сущности",
        verified=True,
        important_numbers=[42, 87, 15],
        addition={
            "additional_info": "Дополнительные сведения",
            "additional_number": 123,
        },
    )
    return json.loads(request_model.model_dump_json())


@pytest.fixture(scope="function")
def created_entity(api_client: ApiClient, entity_payload: dict) -> Entity:
    create_resp = api_client.create(entity_payload)
    create_resp.raise_for_status()

    entity_id = int(create_resp.text.strip())
    get_resp = api_client.get(entity_id)
    get_resp.raise_for_status()

    entity = Entity(**get_resp.json())
    yield entity

    api_client.delete(entity_id)