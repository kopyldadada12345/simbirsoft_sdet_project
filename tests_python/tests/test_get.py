
from src.models import Entity


def test_get_entity(api_client, created_entity: Entity):
    response = api_client.get(created_entity.id)
    assert response.status_code == 200

    entity = Entity(**response.json())
    assert entity == created_entity