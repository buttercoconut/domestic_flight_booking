# models/booking.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from . import Base

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    flight_id = Column(Integer, ForeignKey("flights.id"), nullable=False)
    seat_number = Column(String, nullable=False)
    booking_time = Column(DateTime, nullable=False)
    total_price = Column(Float, nullable=False)
    status = Column(String, default="confirmed")

    user = relationship("User", backref="bookings")
    flight = relationship("Flight", backref="bookings")

# Pydantic schemas
from pydantic import BaseModel
from datetime import datetime

class BookingBase(BaseModel):
    flight_id: int
    seat_number: str

class BookingCreate(BookingBase):
    pass

class BookingRead(BookingBase):
    id: int
    user_id: int
    booking_time: datetime
    total_price: float
    status: str

    class Config:
        orm_mode = True
