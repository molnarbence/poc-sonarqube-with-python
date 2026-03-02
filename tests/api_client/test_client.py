from app.api_client.client import get_stuff


def test_get_stuff() -> None:
    result = get_stuff()

    assert result == {"stuff": "some stuff"}
