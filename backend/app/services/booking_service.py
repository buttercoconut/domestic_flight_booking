# services/booking_service.py
from sqlalchemy.orm import Session
from ..models.booking import Booking, BookingCreate, BookingRead
from ..models.flight import Flight
from datetime import datetime

# Reserve a flight seat

def reserve_flight(db: Session, user_id: int, flight_id: int, seat_number: str):
    # Check flight exists and has available seats
    flight = db.query(Flight).filter(Flight.id == flight_id, Flight.is_active == True).first()
    if not flight:
        raise ValueError("Flight not found or inactive")
    if flight.available_seats <= 0:
        raise ValueError("No seats available")
    # Check seat number is not already taken
    existing = db.query(Booking).filter(Booking.flight_id == flight_id, Booking.seat_number == seat_number).first()
    if existing:
        raise ValueError("Seat already booked")
    # Create booking
    booking = Booking(
        user_id=user_id,
        flight_id=flight_id,
        seat_number=seat_number,
        booking_time=datetime.utcnow(),
        total_price=flight.price,
        status="confirmed"
    )
    db.add(booking)
    # Decrement available seats
    flight.available_seats -= 1
    db.commit()
    db.refresh(booking)
    return booking

# Get bookings for a user

def get_user_bookings(db: Session, user_id: int, skip: int = 0, limit: int = 10):
    return db.query(Booking).filter(Booking.user_id == user_id).offset(skip).limit(limit).all()
