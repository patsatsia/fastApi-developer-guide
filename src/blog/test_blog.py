from src.main import app
from fastapi.testclient import TestClient

test_client = TestClient(app)


def test_say_hello_success():
    response = test_client.get('/blogs/')
    assert response.status_code == 200
