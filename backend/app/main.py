# main.py
from fastapi import FastAPI
from .routes import flight, booking, payment, user
from .dependencies.database import engine, Base

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Domestic Flight Booking API")

app.include_router(user.router)
app.include_router(flight.router)
app.include_router(booking.router)
app.include_router(payment.router)

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Domestic Flight Booking API"}
