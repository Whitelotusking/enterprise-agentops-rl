from fastapi.testclient import TestClient

from app.main import app


def test_health_contract() -> None:
    response = TestClient(app).get("/health")
    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "service": "enterprise-agentops-rl",
        "phase": "bootstrap",
    }


def test_openapi_is_available() -> None:
    response = TestClient(app).get("/openapi.json")
    assert response.status_code == 200
    assert "/health" in response.json()["paths"]
