# models/seat.py
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Seat(Base):
    __tablename__ = "seats"

    id = Column(Integer, primary_key=True, index=True)
    flight_id = Column(Integer, ForeignKey("flights.id"), nullable=False)
    seat_number = Column(String, nullable=False)
    is_available = Column(Boolean, default=True)

    flight = relationship("Flight", backref="seats")

# Pydantic schemas
from pydantic import BaseModel

class SeatBase(BaseModel):
    flight_id: int
    seat_number: str
    is_available: bool

class SeatCreate(SeatBase):
    pass

class SeatRead(SeatBase):
    id: int

    class Config:
        orm_mode = True
