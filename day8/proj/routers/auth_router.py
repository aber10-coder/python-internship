from fastapi import APIRouter, HTTPException, Depends
from schemas import UserCreate, UserResponse, UserLogin, TokenResponse
from auth import create_user, login_user, get_current_user

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register", response_model=UserResponse)
def register(user: UserCreate):
    created = create_user(user)
    if created is None:
        raise HTTPException(status_code=400, detail="Email already exists")
    return created


@router.post("/login", response_model=TokenResponse)
def login(user: UserLogin):
    return login_user(user)


@router.get("/me", response_model=UserResponse)
def me(current_user: str = Depends(get_current_user)):
    from auth import get_user_by_email
    user = get_user_by_email(current_user)
    return {"id": user["id"], "email": user["email"]}