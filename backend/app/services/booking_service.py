from ..models.models import BookingRequest, BookingResponse, Flight, Seat
import uuid

# In-memory booking store
BOOKINGS = {}

# Simple seat map for each flight
SEAT_MAP = {
    "KE123": {f"{row}{seat}": True for row in range(1, 6) for seat in "ABCDEF"},
    "KE456": {f"{row}{seat}": True for row in range(1, 6) for seat in "ABCDEF"},
}

def reserve_flight(request: BookingRequest) -> BookingResponse:
    flight = next((f for f in request.__class__.__mro__[0].__annotations__ if f.flight_number == request.flight_number), None)
    if not flight:
        raise ValueError("Flight not found")
    seat_key = request.seat_number
    if not SEAT_MAP.get(request.flight_number, {}).get(seat_key, False):
        raise ValueError("Seat not available")
    # Mark seat as booked
    SEAT_MAP[request.flight_number][seat_key] = False
    booking_id = uuid.uuid4().int >> 64
    booking = BookingResponse(
        booking_id=booking_id,
        status="confirmed",
        flight=flight,
        seat=Seat(seat_number=seat_key, is_available=False),
    )
    BOOKINGS[booking_id] = booking
    return booking
