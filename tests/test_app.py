import pytest
from src.app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "ok"


def test_add(client):
    response = client.get("/add?a=2&b=3")
    assert response.status_code == 200
    assert response.json["result"] == 5.0


def test_subtract(client):
    response = client.get("/subtract?a=10&b=3")
    assert response.status_code == 200
    assert response.json["result"] == 7.0


def test_multiply(client):
    response = client.get("/multiply?a=4&b=5")
    assert response.status_code == 200
    assert response.json["result"] == 20.0


def test_divide(client):
    response = client.get("/divide?a=10&b=2")
    assert response.status_code == 200
    assert response.json["result"] == 5.0


def test_divide_by_zero(client):
    response = client.get("/divide?a=5&b=0")
    assert response.status_code == 400
    assert "error" in response.json