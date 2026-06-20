
from fastapi import FastAPI, HTTPException,Header,Depends
import uuid

from schemas import UserCreate,UserResponse,UserLogin,TokenResponse

from db import init_db,create_user,get_user_by_email,pwd_context
from passlib.context import CryptContext 


app = FastAPI()
sessions={}


@app.on_event("startup")
def startup():
    init_db()


@app.post(
    "/auth/register",
    response_model=UserResponse
)
def register(user: UserCreate):

    created_user = create_user(user)

    if created_user is None:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    return created_user

@app.post("/auth/login",response_model=TokenResponse)
def login(user: UserLogin):
    db_user= get_user_by_email(user.email)
    if db_user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )
    if not pwd_context.verify(user.password,db_user["hashed_password"]):
        raise HTTPException(status_code=401,detail="Invalid credentials!")
    token=str(uuid.uuid4())
    sessions[token]=user.email
    return{
        "token":token
    }

def get_current_user(authorization:str=Header(None)):
    print("HEADER =", repr(authorization))
    if authorization is None:
        raise HTTPException(status_code=401,detail="Misiing token!")
    try:
        scheme,token=authorization.split()
        if schema !="Bearer":
            raise HTTPException(status_code=401,detail="Invalid token")
    except ValueError:
         raise HTTPException(status_code=401,detail="Invalid header")
    

    if token not in sessions:
        raise HTTPException(status_code=401,detail="Invalid token!")
    return sessions[token]
    

@app.get("/profile")
def profile(current_user=Depends(get_current_user)):
    return{
        "email":current_user
        
    }
       

