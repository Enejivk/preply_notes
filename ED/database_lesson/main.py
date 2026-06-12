from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from pydantic import BaseModel, EmailStr
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional

# ──────────────────────────────────────────────
# CONFIG
# ──────────────────────────────────────────────

SECRET_KEY = "your-super-secret-key-change-this-in-production"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_DAYS = 7

# ──────────────────────────────────────────────
# DATABASE SETUP
# ──────────────────────────────────────────────

DATABASE_URL = "sqlite:///./app.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ──────────────────────────────────────────────
# DATABASE MODELS
# ──────────────────────────────────────────────

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)


class TokenBlacklist(Base):
    __tablename__ = "token_blacklist"

    id = Column(Integer, primary_key=True, index=True)
    token = Column(String, unique=True, index=True)
    blacklisted_at = Column(DateTime, default=datetime.utcnow)


# ──────────────────────────────────────────────
# PYDANTIC SCHEMAS
# ──────────────────────────────────────────────

class UserRegister(BaseModel):
    name: str
    email: str
    password: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool
    is_verified: bool
    created_at: datetime

    class Config:
        from_attributes = True


class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class RefreshTokenRequest(BaseModel):
    refresh_token: str


class ChangePasswordRequest(BaseModel):
    current_password: str
    new_password: str


class UpdateProfileRequest(BaseModel):
    name: str
    email: str


# ──────────────────────────────────────────────
# PASSWORD HASHING
# ──────────────────────────────────────────────

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)


# ──────────────────────────────────────────────
# JWT TOKENS
# ──────────────────────────────────────────────

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def create_access_token(data: dict) -> str:
    payload = data.copy()
    payload["exp"] = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    payload["type"] = "access"
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def create_refresh_token(data: dict) -> str:
    payload = data.copy()
    payload["exp"] = datetime.utcnow() + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    payload["type"] = "refresh"
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def decode_token(token: str) -> dict:
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )


# ──────────────────────────────────────────────
# CURRENT USER DEPENDENCY
# ──────────────────────────────────────────────

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    payload = decode_token(token)

    if payload.get("type") != "access":
        raise HTTPException(status_code=401, detail="Invalid token type")

    # Check if token is blacklisted (logged out)
    blacklisted = db.query(TokenBlacklist).filter(TokenBlacklist.token == token).first()
    if blacklisted:
        raise HTTPException(status_code=401, detail="Token has been revoked. Please log in again.")

    user = db.query(User).filter(User.email == payload.get("sub")).first()
    if user is None:
        raise HTTPException(status_code=401, detail="User not found")
    if not user.is_active:
        raise HTTPException(status_code=403, detail="Account is deactivated")

    return user


# ──────────────────────────────────────────────
# APP
# ──────────────────────────────────────────────

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI Auth System")


# ──────────────────────────────────────────────
# AUTH ROUTES
# ──────────────────────────────────────────────

@app.post("/auth/register", response_model=UserResponse, status_code=201, tags=["Auth"])
def register(user: UserRegister, db: Session = Depends(get_db)):
    """Register a new user account."""
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = User(
        name=user.name,
        email=user.email,
        hashed_password=hash_password(user.password),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.post("/auth/login", response_model=TokenResponse, tags=["Auth"])
def login(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """Login with email + password. Returns access & refresh tokens."""
    user = db.query(User).filter(User.email == form.username).first()
    if not user or not verify_password(form.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Incorrect email or password")
    if not user.is_active:
        raise HTTPException(status_code=403, detail="Account is deactivated")

    return TokenResponse(
        access_token=create_access_token({"sub": user.email}),
        refresh_token=create_refresh_token({"sub": user.email}),
    )


@app.post("/auth/refresh", response_model=TokenResponse, tags=["Auth"])
def refresh_token(body: RefreshTokenRequest, db: Session = Depends(get_db)):
    """Use a refresh token to get a new access token."""
    payload = decode_token(body.refresh_token)

    if payload.get("type") != "refresh":
        raise HTTPException(status_code=401, detail="Invalid token type")

    user = db.query(User).filter(User.email == payload.get("sub")).first()
    if not user or not user.is_active:
        raise HTTPException(status_code=401, detail="User not found or inactive")

    return TokenResponse(
        access_token=create_access_token({"sub": user.email}),
        refresh_token=create_refresh_token({"sub": user.email}),
    )


@app.post("/auth/logout", tags=["Auth"])
def logout(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """Logout by blacklisting the current access token."""
    db.add(TokenBlacklist(token=token))
    db.commit()
    return {"message": "Successfully logged out"}


# ──────────────────────────────────────────────
# USER ROUTES (Protected)
# ──────────────────────────────────────────────

@app.get("/users/me", response_model=UserResponse, tags=["Users"])
def get_me(current_user: User = Depends(get_current_user)):
    """Get the currently logged-in user's profile."""
    return current_user


@app.put("/users/me", response_model=UserResponse, tags=["Users"])
def update_profile(
    body: UpdateProfileRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Update name and email of the logged-in user."""
    if body.email != current_user.email:
        if db.query(User).filter(User.email == body.email).first():
            raise HTTPException(status_code=400, detail="Email already taken")

    current_user.name = body.name
    current_user.email = body.email
    db.commit()
    db.refresh(current_user)
    return current_user


@app.put("/users/me/password", tags=["Users"])
def change_password(
    body: ChangePasswordRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Change the logged-in user's password."""
    if not verify_password(body.current_password, current_user.hashed_password):
        raise HTTPException(status_code=400, detail="Current password is incorrect")

    current_user.hashed_password = hash_password(body.new_password)
    db.commit()
    return {"message": "Password updated successfully"}


@app.delete("/users/me", tags=["Users"])
def deactivate_account(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Deactivate (soft-delete) the logged-in user's account."""
    current_user.is_active = False
    db.commit()
    return {"message": "Account deactivated successfully"}


# ──────────────────────────────────────────────
# ADMIN ROUTES (Protected)
# ──────────────────────────────────────────────

@app.get("/users/", response_model=list[UserResponse], tags=["Admin"])
def list_users(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),  # must be logged in
):
    """List all users (requires authentication)."""
    return db.query(User).offset(skip).limit(limit).all()


@app.get("/users/{user_id}", response_model=UserResponse, tags=["Admin"])
def get_user(
    user_id: int,
    db: Session = Depends(get_db),
    _: User = Depends(get_current_user),
):
    """Get a specific user by ID."""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
