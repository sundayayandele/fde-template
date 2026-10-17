import pytest
from fastapi.testclient import TestClient

from app.main import app, greet

client = TestClient(app)


def test_live():
    assert client.get("/health/live").json() == {"status": "ok"}


def test_ready_reports_version():
    body = client.get("/health/ready").json()
    assert body["status"] == "ready"
    assert "version" in body


def test_metrics_exposed():
    client.get("/health/live")
    r = client.get("/metrics/")
    assert r.status_code == 200
    assert "http_requests_total" in r.text


def test_hello_validation():
    assert client.post("/api/v1/hello", json={"name": ""}).status_code == 422


@pytest.mark.exercise
def test_greet():
    assert greet("  Ada ") == "Hello, Ada! Welcome to the FDE series."


@pytest.mark.exercise
def test_hello_endpoint():
    r = client.post("/api/v1/hello", json={"name": "Ada"})
    assert r.status_code == 200
    assert r.json()["message"].startswith("Hello, Ada")
