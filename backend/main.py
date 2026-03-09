from fastapi import FastAPI, HTTPException

app = FastAPI()

users = []
otp_store = {}


@app.get("/")
def root():
    return {"message": "DevOps Platform API running"}


@app.post("/signup")
def signup(name: str, email: str, password: str):

    for user in users:
        if user["email"] == email:
            raise HTTPException(status_code=400, detail="User already exists")

    users.append({
        "name": name,
        "email": email,
        "password": password
    })

    return {"message": "User created successfully"}


@app.post("/login")
def login(email: str, password: str):

    for user in users:
        if user["email"] == email and user["password"] == password:
            return {"message": "Login successful"}

    raise HTTPException(status_code=401, detail="Invalid credentials")

@app.post("/login-otp")
def login_otp(phone: str):

    otp = "123456"

    otp_store[phone] = otp

    return {
        "message": "OTP generated",
        "otp": otp
    }    

@app.post("/verify-otp")
def verify_otp(phone: str, otp: str):

    if phone in otp_store and otp_store[phone] == otp:
        return {"message": "OTP login successful"}

    raise HTTPException(status_code=400, detail="Invalid OTP")


@app.get("/stats")
def stats():

    return {
        "total_users": len(users)
    }
    