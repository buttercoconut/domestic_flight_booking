# services/flight_service.py
from sqlalchemy.orm import Session
from ..models.flight import Flight, FlightCreate, FlightRead
from datetime import datetime

# CRUD operations for flights

def get_flights(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Flight).offset(skip).limit(limit).all()

def get_flight(db: Session, flight_id: int):
    return db.query(Flight).filter(Flight.id == flight_id).first()

def create_flight(db: Session, flight: FlightCreate):
    db_flight = Flight(**flight.dict())
    db_flight.available_seats = flight.total_seats
    db.add(db_flight)
    db.commit()
    db.refresh(db_flight)
    return db_flight

# Search flights by origin, destination, date
def search_flights(db: Session, origin: str, destination: str, date: datetime):
    return db.query(Flight).filter(
        Flight.origin == origin,
        Flight.destination == destination,
        Flight.departure_time.between(date, date.replace(hour=23, minute=59, second=59)),
        Flight.is_active == True
    ).all()
