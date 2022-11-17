from fastapi.testclient import TestClient
from main import app

# given
client = TestClient(app)


def test_read_main_should_return_status_200():
    # when
    response = client.get("/")
    # then
    assert response.status_code == 200


def test_read_main_response():
    # when
    response = client.get("/")
    # then
    assert response.json() == {"description": "Please submit a post with a password for validation on validate_password view"}


def test_password_validation_misspelled_key_password_should_return_status_422():
    # given
    misspelled_key_password_dict = {"passwrd": ""}
    # when
    response = client.post("/", data=misspelled_key_password_dict)
    # then
    assert response.status_code == 422
