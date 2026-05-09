from pydantic import BaseModel, Field
from datetime import datetime

class Flight(BaseModel):
    flight_number: str = Field(..., description="항공편 번호")
    departure_airport: str = Field(..., description="출발 공항 코드")
    arrival_airport: str = Field(..., description="도착 공항 코드")
    departure_time: datetime = Field(..., description="출발 시각")
    price: float = Field(..., description="항공권 가격")

class BookingRequest(BaseModel):
    user_id: int
    flight_id: int
    seat_number: str
    passenger_name: str
    passenger_id: str

class BookingResponse(BaseModel):
    booking_id: int
    status: str
    flight: Flight
    seat_number: str
    passenger_name: str
    passenger_id: str
    created_at: datetime

class PaymentRequest(BaseModel):
    booking_id: int
    amount: float
    payment_method: str

class PaymentResponse(BaseModel):
    payment_id: int
    status: str
    transaction_id: str
    created_at: datetime
