from datetime import datetime
from ..models.payment import PaymentRequest, PaymentResponse
from sqlalchemy.orm import Session

_payment_counter = 1


def process_payment(db: Session, request: PaymentRequest) -> PaymentResponse:
    global _payment_counter
    payment_id = _payment_counter
    _payment_counter += 1
    response = PaymentResponse(
        payment_id=payment_id,
        status="completed",
        transaction_id=f"TXN{payment_id:06d}",
        created_at=datetime.utcnow(),
    )
    return response
