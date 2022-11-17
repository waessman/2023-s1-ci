from fastapi.testclient import TestClient
from main import app

# given
client = TestClient(app)


def test_read_main_status():
    # when
    response = client.get("/")
    # then
    assert response.status_code == 200
