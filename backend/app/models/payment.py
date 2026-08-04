# models/payment.py
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from . import Base

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    booking_id = Column(Integer, ForeignKey("bookings.id"), nullable=False)
    amount = Column(Float, nullable=False)
    payment_time = Column(DateTime, nullable=False)
    payment_method = Column(String, nullable=False)
    status = Column(String, default="completed")

    booking = relationship("Booking", backref="payments")

# Pydantic schemas
from pydantic import BaseModel
from datetime import datetime

class PaymentBase(BaseModel):
    booking_id: int
    amount: float
    payment_method: str

class PaymentCreate(PaymentBase):
    pass

class PaymentRead(PaymentBase):
    id: int
    payment_time: datetime
    status: str

    class Config:
        orm_mode = True
