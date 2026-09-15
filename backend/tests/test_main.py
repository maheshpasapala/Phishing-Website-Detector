import pytest
from main import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200


def test_register_endpoint_exists(client):
    response = client.post("/api/v1/register", json={})
    assert response.status_code != 404


def test_login_endpoint_exists(client):
    response = client.post("/api/v1/login", json={})
    assert response.status_code != 404


def test_auth_endpoint_exists(client):
    response = client.get("/api/v1/auth")
    assert response.status_code != 404


def test_urls_endpoint_exists(client):
    response = client.get("/api/v1/urls")
    assert response.status_code != 404