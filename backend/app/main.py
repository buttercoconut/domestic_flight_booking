from fastapi import FastAPI
from .routes import booking as booking_router
from .routes import payment as payment_router

app = FastAPI(title="Domestic Flight Booking API")

app.include_router(booking_router.router)
app.include_router(payment_router.router)

# Health check
@app.get("/health")
async def health_check():
    return {"status": "ok"}
