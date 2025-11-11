

from src.models import Entity


def test_delete_entity(api_client, entity_payload):
    create_resp = api_client.create(entity_payload)
    create_resp.raise_for_status()
    entity_id = int(create_resp.text.strip())

    delete_resp = api_client.delete(entity_id)
    assert delete_resp.status_code == 204

    get_resp = api_client.get(entity_id)
    assert get_resp.status_code in (404, 500, 400)