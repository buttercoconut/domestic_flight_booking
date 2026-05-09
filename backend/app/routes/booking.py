from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..dependencies.database import get_db
from ..models.flight import Flight, BookingRequest, BookingResponse
from ..services.booking_service import reserve_flight

router = APIRouter(prefix="/bookings", tags=["bookings"])

@router.post("/reserve", response_model=BookingResponse)
async def reserve_booking(request: BookingRequest, db: Session = Depends(get_db)):
    try:
        booking = reserve_flight(db, request)
        return booking
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/list", response_model=List[BookingResponse])
async def list_bookings(user_id: int, db: Session = Depends(get_db)):
    # placeholder: return empty list
    return []
