from fastapi import APIRouter, Depends, HTTPException
from typing import List
from ..models.models import Flight, BookingRequest, BookingResponse
from ..services.booking_service import reserve_flight

router = APIRouter()

# Mock flight data
FLIGHTS = [
    Flight(
        flight_number="KE123",
        departure_airport="ICN",
        arrival_airport="GMP",
        departure_time="2024-07-01T08:00:00Z",
        price=120000.0,
    ),
    Flight(
        flight_number="KE456",
        departure_airport="ICN",
        arrival_airport="GMP",
        departure_time="2024-07-01T12:00:00Z",
        price=110000.0,
    ),
]

@router.get("/search", response_model=List[Flight])
def search_flights(departure: str, arrival: str, date: str):
    # Simple filter logic
    return [f for f in FLIGHTS if f.departure_airport == departure and f.arrival_airport == arrival]

@router.post("/reserve", response_model=BookingResponse)
def reserve(request: BookingRequest):
    try:
        return reserve_flight(request)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
