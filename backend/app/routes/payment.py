# routes/payment.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..dependencies.database import get_db
from ..services.payment_service import process_payment
from ..models.payment import PaymentCreate, PaymentRead

router = APIRouter(prefix="/payments", tags=["payments"])

@router.post("/", response_model=PaymentRead, status_code=status.HTTP_201_CREATED)
def create_payment(payment: PaymentCreate, db: Session = Depends(get_db)):
    try:
        return process_payment(db, payment)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
