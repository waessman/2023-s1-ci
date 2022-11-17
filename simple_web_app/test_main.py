from fastapi.testclient import TestClient
from main import app

# given
client = TestClient(app)


def test_read_main_status():
    # when
    response = client.get("/")
    # then
    assert response.status_code == 200


def test_read_main_response():
    # when
    response = client.get("/")
    # then
    assert response.json() == {"description": "Please submit a post with a password for validation on validate_password view"}
