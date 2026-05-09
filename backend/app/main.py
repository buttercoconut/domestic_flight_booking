from fastapi import Depends, FastAPI
from .routes import flights as flights_router
from .dependencies import database

app = FastAPI(title="Domestic Flight Booking API")

app.include_router(flights_router)

# Health check
@app.get("/health")
def health():
    return {"status": "ok"}
