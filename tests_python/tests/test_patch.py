
from src.models import Entity


def test_patch_entity(api_client, created_entity: Entity):
    payload = {
        "title": created_entity.title,
        "verified": False,
        "important_numbers": created_entity.important_numbers + [999],
        "addition": {
            "additional_info": "Обновлённые сведения",
            "additional_number": 321,
        },
    }

    response = api_client.patch(created_entity.id, payload)
    assert response.status_code in (200, 204)

    if response.status_code == 200:
        updated = Entity(**response.json())
    else:
        get_resp = api_client.get(created_entity.id)
        get_resp.raise_for_status()
        updated = Entity(**get_resp.json())

    assert updated.id == created_entity.id
    assert updated.verified is False
    assert updated.addition.additional_info == "Обновлённые сведения"