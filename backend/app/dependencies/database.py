# Database dependency placeholder
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

DATABASE_URL = "postgresql://user:password@localhost:5432/domestic_flight"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency for FastAPI
async def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
