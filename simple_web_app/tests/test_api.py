from fastapi.testclient import TestClient
from simple_web_app.main import app
import json

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


def test_password_validation_misspelled_key_should_return_status_422():
    # given
    misspelled_key_password_dict = {"contnt": ""}
    # when
    response = client.post("/", data=json.dumps(misspelled_key_password_dict))
    # then
    assert response.status_code == 422


def test_password_validation_empty_str_password_should_return_status_400():
    # given
    empty_password_dict = {"content": ""}
    # when
    response = client.post("/", data=json.dumps(empty_password_dict))
    # then
    assert response.status_code == 400


def test_password_validation_8_chars_good_password_should_return_status_201():
    # given
    good_password_dict = {"content": "aB1@cD2#"}
    # when
    response = client.post("/", data=json.dumps(good_password_dict))
    # then
    assert response.status_code == 201
