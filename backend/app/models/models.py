from pydantic import BaseModel, Field
from datetime import datetime

class Flight(BaseModel):
    flight_number: str = Field(..., example="KE123")
    departure_airport: str = Field(..., example="ICN")
    arrival_airport: str = Field(..., example="GMP")
    departure_time: datetime
    price: float

class Seat(BaseModel):
    seat_number: str
    is_available: bool

class BookingRequest(BaseModel):
    user_id: int
    flight_number: str
    seat_number: str
    passenger_name: str
    passenger_email: str

class BookingResponse(BaseModel):
    booking_id: int
    status: str
    flight: Flight
    seat: Seat
