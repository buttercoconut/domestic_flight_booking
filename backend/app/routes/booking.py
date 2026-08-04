# routes/booking.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..dependencies.database import get_db
from ..services.booking_service import reserve_flight, get_user_bookings
from ..models.booking import BookingCreate, BookingRead

router = APIRouter(prefix="/bookings", tags=["bookings"])

@router.post("/", response_model=BookingRead, status_code=status.HTTP_201_CREATED)
def create_booking(booking: BookingCreate, user_id: int, db: Session = Depends(get_db)):
    try:
        return reserve_flight(db, user_id, booking.flight_id, booking.seat_number)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/user/{user_id}", response_model=list[BookingRead])
def read_user_bookings(user_id: int, db: Session = Depends(get_db)):
    return get_user_bookings(db, user_id)
