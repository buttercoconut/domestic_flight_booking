import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_search_flights():
    response = client.get("/flights/search", params={"departure": "ICN", "arrival": "GMP", "date": "2024-07-01"})
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


def test_reserve_flight():
    payload = {
        "user_id": 1,
        "flight_number": "KE123",
        "seat_number": "1A",
        "passenger_name": "John Doe",
        "passenger_email": "john@example.com",
    }
    response = client.post("/flights/reserve", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "confirmed"
    assert data["flight"]["flight_number"] == "KE123"
