from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from database import engine, SessionLocal, Base
from user_model import User
from feature_model import FeatureFlag


app = FastAPI()

# CORS middleware (allows frontend to call backend)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# create database tables

Base.metadata.create_all(bind=engine)

users = []
otp_store = {}


@app.get("/")
def root():
    return {"message": "DevOps Platform API running"}


# -----------------------------
# SIGNUP
# -----------------------------

@app.post("/signup")
def signup(name: str, email: str, password: str):

    db = SessionLocal()

    existing = db.query(User).filter(User.email == email).first()

    if existing:
        raise HTTPException(status_code=400, detail="User already exists")

    user = User(
        name=name,
        email=email,
        password=password
    )

    db.add(user)
    db.commit()

    return {"message": "User created successfully"}


# -----------------------------
# LOGIN
# -----------------------------

@app.post("/login")
def login(email: str, password: str):

    db = SessionLocal()

    user = db.query(User).filter(User.email == email).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user.password != password:
        raise HTTPException(status_code=401, detail="Invalid password")

    return {"message": "Login successful"}


# -----------------------------
# OTP VERIFY
# -----------------------------

@app.post("/verify-otp")
def verify_otp(phone: str, otp: str):

    if phone in otp_store and otp_store[phone] == otp:
        return {"message": "OTP login successful"}

    raise HTTPException(status_code=400, detail="Invalid OTP")


# -----------------------------
# STATS
# -----------------------------

@app.get("/stats")
def stats():

    db = SessionLocal()

    total = db.query(User).count()

    return {
        "total_users": total
    }


# -----------------------------
# FEATURE FLAG TOGGLE
# -----------------------------

@app.post("/toggle-feature")
def toggle_feature():

    db = SessionLocal()

    feature = db.query(FeatureFlag).filter(
        FeatureFlag.feature_name == "new_dashboard"
    ).first()

    if not feature:

        feature = FeatureFlag(
            feature_name="new_dashboard",
            enabled=True
        )

        db.add(feature)

    else:

        feature.enabled = not feature.enabled

    db.commit()

    return {
        "feature": feature.feature_name,
        "enabled": feature.enabled
    }


# -----------------------------
# FEATURE STATUS
# -----------------------------

@app.get("/feature-status")
def feature_status():

    db = SessionLocal()

    feature = db.query(FeatureFlag).filter(
        FeatureFlag.feature_name == "new_dashboard"
    ).first()

    if not feature:
        return {"enabled": False}

    return {"enabled": feature.enabled}


from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from database import engine, SessionLocal, Base
from user_model import User
from feature_model import FeatureFlag


app = FastAPI()

# CORS middleware (allows frontend to call backend)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# create database tables

Base.metadata.create_all(bind=engine)

users = []
otp_store = {}


@app.get("/")
def root():
    return {"message": "DevOps Platform API running"}


# -----------------------------
# SIGNUP
# -----------------------------

@app.post("/signup")
def signup(name: str, email: str, password: str):

    db = SessionLocal()

    existing = db.query(User).filter(User.email == email).first()

    if existing:
        raise HTTPException(status_code=400, detail="User already exists")

    user = User(
        name=name,
        email=email,
        password=password
    )

    db.add(user)
    db.commit()

    return {"message": "User created successfully"}


# -----------------------------
# LOGIN
# -----------------------------

@app.post("/login")
def login(email: str, password: str):

    db = SessionLocal()

    user = db.query(User).filter(User.email == email).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user.password != password:
        raise HTTPException(status_code=401, detail="Invalid password")

    return {"message": "Login successful"}


# -----------------------------
# OTP VERIFY
# -----------------------------

@app.post("/verify-otp")
def verify_otp(phone: str, otp: str):

    if phone in otp_store and otp_store[phone] == otp:
        return {"message": "OTP login successful"}

    raise HTTPException(status_code=400, detail="Invalid OTP")


# -----------------------------
# STATS
# -----------------------------

@app.get("/stats")
def stats():

    db = SessionLocal()

    total = db.query(User).count()

    return {
        "total_users": total
    }


# -----------------------------
# FEATURE FLAG TOGGLE
# -----------------------------

@app.post("/toggle-feature")
def toggle_feature():

    db = SessionLocal()

    feature = db.query(FeatureFlag).filter(
        FeatureFlag.feature_name == "new_dashboard"
    ).first()

    if not feature:

        feature = FeatureFlag(
            feature_name="new_dashboard",
            enabled=True
        )

        db.add(feature)

    else:

        feature.enabled = not feature.enabled

    db.commit()

    return {
        "feature": feature.feature_name,
        "enabled": feature.enabled
    }


# -----------------------------
# FEATURE STATUS
# -----------------------------

@app.get("/feature-status")
def feature_status():

    db = SessionLocal()

    feature = db.query(FeatureFlag).filter(
        FeatureFlag.feature_name == "new_dashboard"
    ).first()

    if not feature:
        return {"enabled": False}

    return {"enabled": feature.enabled}