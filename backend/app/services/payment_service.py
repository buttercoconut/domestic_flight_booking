# services/payment_service.py
from sqlalchemy.orm import Session
from ..models.payment import Payment, PaymentCreate, PaymentRead
from datetime import datetime

# Process payment (placeholder)

def process_payment(db: Session, payment: PaymentCreate):
    # In real scenario, integrate with payment gateway
    payment_record = Payment(
        booking_id=payment.booking_id,
        amount=payment.amount,
        payment_time=datetime.utcnow(),
        payment_method=payment.payment_method,
        status="completed"
    )
    db.add(payment_record)
    db.commit()
    db.refresh(payment_record)
    return payment_record
