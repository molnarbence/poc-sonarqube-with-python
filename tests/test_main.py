from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_main_ok() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_read_item_ok() -> None:
    response = client.get("/items/42")
    assert response.status_code == 200
    assert response.json() == {"item_id": 42}
