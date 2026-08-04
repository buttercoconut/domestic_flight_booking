# tests/test_booking.py
import pytest
from fastapi.testclient import TestClient
from ..app.main import app

client = TestClient(app)

# Dummy user and flight creation for tests
@pytest.fixture(scope="module")
def setup_data():
    # Create user
    user_resp = client.post("/users/", json={"username": "testuser", "email": "test@example.com", "password": "testpass"})
    assert user_resp.status_code == 201
    user_id = user_resp.json()["id"]
    # Create flight
    flight_resp = client.post("/flights/", json={
        "flight_number": "AB123",
        "origin": "CityA",
        "destination": "CityB",
        "departure_time": "2025-12-01T10:00:00",
        "arrival_time": "2025-12-01T12:00:00",
        "total_seats": 100,
        "price": 150.0
    })
    assert flight_resp.status_code == 201
    flight_id = flight_resp.json()["id"]
    return {"user_id": user_id, "flight_id": flight_id}

def test_reserve_flight(setup_data):
    data = setup_data
    resp = client.post("/bookings/", json={"flight_id": data["flight_id"], "seat_number": "12A"})
    assert resp.status_code == 201
    booking = resp.json()
    assert booking["seat_number"] == "12A"
    assert booking["total_price"] == 150.0

