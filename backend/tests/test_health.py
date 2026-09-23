from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_healthz():
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_readyz():
    response = client.get("/readyz")
    assert response.status_code == 200


def test_create_and_get_case():
    create_response = client.post(
        "/api/v1/cases", json={"company_name": "Acme Corp", "owner_id": "user-1"}
    )
    assert create_response.status_code == 201
    case_id = create_response.json()["id"]

    get_response = client.get(f"/api/v1/cases/{case_id}")
    assert get_response.status_code == 200
    assert get_response.json()["company_name"] == "Acme Corp"
