
# new
from src.models import EntitiesResponse
from src.models import Entity
def test_get_all_entities(api_client, created_entity: Entity):
    response = api_client.get_all()
    assert response.status_code == 200

    entities_resp = EntitiesResponse(**response.json())
    assert any(entity.id == created_entity.id for entity in entities_resp.entity)