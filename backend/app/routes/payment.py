from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..dependencies.database import get_db
from ..models.payment import PaymentRequest, PaymentResponse
from ..services.payment_service import process_payment

router = APIRouter(prefix="/payments", tags=["payments"])

@router.post("/process", response_model=PaymentResponse)
async def payment_endpoint(request: PaymentRequest, db: Session = Depends(get_db)):
    try:
        payment = process_payment(db, request)
        return payment
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
