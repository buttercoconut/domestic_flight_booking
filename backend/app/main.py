from fastapi import FastAPI
from .routes import flights

app = FastAPI(title="Domestic Flight Booking API")

app.include_router(flights.router, prefix="/flights", tags=["flights"])

# Future routers: bookings, payments, users
