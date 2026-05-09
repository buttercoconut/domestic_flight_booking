from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ..dependencies.database import get_db
from ..models import models as db_models
from ..models import models as schemas

router = APIRouter(prefix="/flights", tags=["flights"])

@router.get("/search", response_model=schemas.FlightListResponse)
def search_flights(query: schemas.FlightSearchQuery, db: Session = Depends(get_db)):
    # Simplified: return all flights matching departure/arrival and date
    flights = db.query(db_models.Flight).filter(
        db_models.Flight.departure_airport == query.departure_airport,
        db_models.Flight.arrival_airport == query.arrival_airport,
        db_models.Flight.departure_time.cast(db_models.Flight.departure_time.type).date() == query.date.date()
    ).all()
    results = []
    for f in flights:
        results.append(schemas.FlightSearchResult(flight=f, seats_available=f.seats_available))
    return schemas.FlightListResponse(flights=results)

@router.post("/reserve", response_model=schemas.Booking)
def reserve_flight(booking: schemas.BookingCreate, db: Session = Depends(get_db)):
    # Core logic: reserve seat and create booking
    flight = db.query(db_models.Flight).filter(db_models.Flight.id == booking.flight_id).first()
    if not flight:
        raise HTTPException(status_code=404, detail="Flight not found")
    if flight.seats_available <= 0:
        raise HTTPException(status_code=400, detail="No seats available")
    # Decrement seat count
    flight.seats_available -= 1
    db.add(flight)
    new_booking = db_models.Booking(
        user_id=booking.user_id,
        flight_id=booking.flight_id,
        seat_number=booking.seat_number,
        passenger_name=booking.passenger_name,
        passenger_email=booking.passenger_email,
        status="PENDING",
    )
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    return new_booking
