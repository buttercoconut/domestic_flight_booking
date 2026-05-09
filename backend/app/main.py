from fastapi import FastAPI
from .routes import flight, booking, payment

app = FastAPI(title="Domestic Flight Booking API")

app.include_router(flight.router)
app.include_router(booking.router)
app.include_router(payment.router)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Domestic Flight Booking API"}
