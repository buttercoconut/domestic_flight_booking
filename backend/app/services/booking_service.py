from datetime import datetime
from ..models.flight import Flight, BookingRequest, BookingResponse
from sqlalchemy.orm import Session

# In-memory storage for demo purposes
_flights = {
    1: Flight(
        flight_number="SK123",
        departure_airport="ICN",
        arrival_airport="GMP",
        departure_time=datetime(2024, 10, 1, 9, 0),
        price=150.0,
    ),
}
_booking_counter = 1


def reserve_flight(db: Session, request: BookingRequest) -> BookingResponse:
    # Simulate flight lookup
    flight = _flights.get(request.flight_id)
    if not flight:
        raise ValueError("Flight not found")
    # Simulate seat reservation logic
    booking_id = _booking_counter
    _booking_counter += 1
    response = BookingResponse(
        booking_id=booking_id,
        status="confirmed",
        flight=flight,
        seat_number=request.seat_number,
        passenger_name=request.passenger_name,
        passenger_id=request.passenger_id,
        created_at=datetime.utcnow(),
    )
    return response
