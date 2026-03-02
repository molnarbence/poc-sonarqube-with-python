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


def test_add_numbers_ok() -> None:
    response = client.post("/add?a=3&b=5")
    assert response.status_code == 200
    assert response.json() == {"result": 8}
