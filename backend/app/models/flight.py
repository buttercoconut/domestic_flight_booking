# models/flight.py
from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean
from . import Base

class Flight(Base):
    __tablename__ = "flights"

    id = Column(Integer, primary_key=True, index=True)
    flight_number = Column(String, unique=True, index=True, nullable=False)
    origin = Column(String, nullable=False)
    destination = Column(String, nullable=False)
    departure_time = Column(DateTime, nullable=False)
    arrival_time = Column(DateTime, nullable=False)
    total_seats = Column(Integer, nullable=False)
    available_seats = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    is_active = Column(Boolean, default=True)

# Pydantic schemas
from pydantic import BaseModel
from datetime import datetime

class FlightBase(BaseModel):
    flight_number: str
    origin: str
    destination: str
    departure_time: datetime
    arrival_time: datetime
    total_seats: int
    price: float

class FlightCreate(FlightBase):
    available_seats: int

class FlightRead(FlightBase):
    id: int
    available_seats: int
    is_active: bool

    class Config:
        orm_mode = True
