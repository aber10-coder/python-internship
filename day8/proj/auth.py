import uuid
from fastapi import  HTTPException
from passlib.context import CryptContext
from db import get_connection
from fastapi import Depends
from fastapi.security import HTTPBearer

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

sessions = {}


def create_user(user):
    conn = get_connection()
    c = conn.cursor()

    c.execute("SELECT * FROM users WHERE email=?", (user.email,))
    if c.fetchone():
        conn.close()
        return None

    hashed_password = pwd_context.hash(user.password)
    c.execute(
        "INSERT INTO users (email, hashed_password) VALUES (?, ?)",
        (user.email, hashed_password)
    )
    user_id = c.lastrowid
    conn.commit()

    c.execute("SELECT * FROM users WHERE id=?", (user_id,))
    row = c.fetchone()
    conn.close()

    return {"id": row["id"], "email": row["email"]}


def get_user_by_email(email):
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE email=?", (email,))
    row = c.fetchone()
    conn.close()
    return row


def login_user(user):
    db_user = get_user_by_email(user.email)

    if not db_user or not pwd_context.verify(user.password, db_user["hashed_password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = str(uuid.uuid4())
    sessions[token] = user.email
    return {"token": token}

bearer_scheme = HTTPBearer()
def get_current_user(credentials = Depends(bearer_scheme)):
    if authorization is None:
        raise HTTPException(status_code=401, detail="Missing token")

    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid token")

    token = authorization.split()[1]

    if token not in sessions:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    return sessions[token]