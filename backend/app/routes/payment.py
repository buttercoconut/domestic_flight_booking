from fastapi import APIRouter, Depends, HTTPException, status
from ..dependencies.database import get_db
from ..models.payment import Payment
from sqlalchemy.orm import Session

router = APIRouter(prefix="/payments", tags=["payments"])

@router.post("/process", response_model=Payment)
async def process_payment(payment: Payment, db: Session = Depends(get_db)):
    # Placeholder: Process payment logic
    return payment
