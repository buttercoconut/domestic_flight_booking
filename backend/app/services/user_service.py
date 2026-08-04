# services/user_service.py
from sqlalchemy.orm import Session
from ..models.user import User, UserCreate, UserRead
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Create user

def create_user(db: Session, user: UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
        is_active=True,
        is_admin=False
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Get user by username

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

# Verify password

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)
