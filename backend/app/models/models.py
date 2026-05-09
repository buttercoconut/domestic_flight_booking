from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional

class Flight(BaseModel):
    flight_number: str = Field(..., description="항공편 번호")
    departure_airport: str = Field(..., description="출발 공항 코드")
    arrival_airport: str = Field(..., description="도착 공항 코드")
    departure_time: datetime = Field(..., description="출발 시각")
    price: float = Field(..., description="기본 가격")
    seats_available: int = Field(..., description="남은 좌석 수")

class Seat(BaseModel):
    seat_number: str
    is_booked: bool = False

class BookingCreate(BaseModel):
    user_id: int
    flight_id: int
    seat_number: str
    passenger_name: str
    passenger_email: str

class Booking(BaseModel):
    id: int
    user_id: int
    flight_id: int
    seat_number: str
    passenger_name: str
    passenger_email: str
    status: str
    created_at: datetime

class PaymentCreate(BaseModel):
    booking_id: int
    amount: float
    method: str

class Payment(BaseModel):
    id: int
    booking_id: int
    amount: float
    method: str
    status: str
    processed_at: datetime

class User(BaseModel):
    id: int
    email: str
    hashed_password: str
    full_name: Optional[str] = None
    is_active: bool = True
    created_at: datetime

class UserCreate(BaseModel):
    email: str
    password: str
    full_name: Optional[str] = None

class UserLogin(BaseModel):
    email: str
    password: str

class UserOut(BaseModel):
    id: int
    email: str
    full_name: Optional[str] = None
    is_active: bool
    created_at: datetime

class FlightSearchQuery(BaseModel):
    departure_airport: str
    arrival_airport: str
    date: datetime

class FlightSearchResult(BaseModel):
    flight: Flight
    seats_available: int

class FlightListResponse(BaseModel):
    flights: List[FlightSearchResult]

# Additional models can be added as needed
