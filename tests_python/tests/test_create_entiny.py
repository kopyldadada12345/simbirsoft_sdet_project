

from src.models import Entity


def test_create_entity(api_client, entity_payload):
    create_resp = api_client.create(entity_payload)
    assert create_resp.status_code in (200, 201)

    entity_id = int(create_resp.text.strip())
    get_resp = api_client.get(entity_id)
    get_resp.raise_for_status()

    entity = Entity(**get_resp.json())
    assert entity.title == entity_payload["title"]
    assert entity.verified == entity_payload["verified"]
    assert entity.important_numbers == entity_payload["important_numbers"]
    assert entity.addition.additional_info == entity_payload["addition"]["additional_info"]