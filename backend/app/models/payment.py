from pydantic import BaseModel

class PaymentRequest(BaseModel):
    booking_id: int
    amount: float
    payment_method: str

class PaymentResponse(BaseModel):
    payment_id: int
    status: str
    transaction_id: str
    created_at: str
