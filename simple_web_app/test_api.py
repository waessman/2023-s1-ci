from fastapi.testclient import TestClient

from .main import app

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
    assert response.json() == {
        "description": "This is just a dummy response. Your API is up and running!"
    }


def test_password_validation_misspelled_key_should_return_status_422():
    # given
    misspelled_key_password_dict = {"contnt": ""}
    # when
    response = client.post("/", json=misspelled_key_password_dict)
    # then
    assert response.status_code == 422


def test_password_validation_empty_str_password_should_return_status_400():
    # given
    empty_password_dict = {"content": ""}
    # when
    response = client.post("/", json=empty_password_dict)
    # then
    print(response.content)
    assert response.status_code == 400


def test_password_validation_8_chars_good_password_should_return_status_201():
    # given
    good_password_dict = {"content": "aB1@cD2#"}
    # when
    response = client.post("/", json=good_password_dict)
    # then
    print(response.content)
    assert response.status_code == 201
