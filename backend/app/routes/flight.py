# routes/flight.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime
from ..dependencies.database import get_db
from ..services.flight_service import get_flights, create_flight, search_flights
from ..models.flight import FlightCreate, FlightRead

router = APIRouter(prefix="/flights", tags=["flights"])

@router.get("/", response_model=list[FlightRead])
def read_flights(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    flights = get_flights(db, skip=skip, limit=limit)
    return flights

@router.post("/", response_model=FlightRead, status_code=status.HTTP_201_CREATED)
def add_flight(flight: FlightCreate, db: Session = Depends(get_db)):
    return create_flight(db, flight)

@router.get("/search", response_model=list[FlightRead])
def search(origin: str, destination: str, date: datetime, db: Session = Depends(get_db)):
    flights = search_flights(db, origin, destination, date)
    return flights
