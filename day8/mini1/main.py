from fastapi import FastAPI, HTTPException

from schemas import UserCreate,UserResponse

from db import init_db,create_user


app = FastAPI()


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