from pydantic import BaseModel
from datetime import datetime

class Flight(BaseModel):
    flight_number: str
    departure_airport: str
    arrival_airport: str
    departure_time: datetime
    price: float

class User(BaseModel):
    id: int
    username: str
    email: str
    hashed_password: str

class Seat(BaseModel):
    seat_number: str
    is_available: bool

class Booking(BaseModel):
    id: int
    user_id: int
    flight_id: int
    seat_number: str
    booking_time: datetime

class Payment(BaseModel):
    id: int
    booking_id: int
    amount: float
    status: str
    paid_at: datetime | None = None
