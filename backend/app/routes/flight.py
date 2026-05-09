from fastapi import APIRouter, Depends, HTTPException, status
from ..dependencies.database import get_db
from ..models.flight import Flight
from sqlalchemy.orm import Session

router = APIRouter(prefix="/flights", tags=["flights"])

@router.get("/search", response_model=list[Flight])
async def search_flights(departure: str, arrival: str, date: str, db: Session = Depends(get_db)):
    # Placeholder: Query database for flights
    return []
