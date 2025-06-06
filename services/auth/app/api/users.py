from fastapi import APIRouter, HTTPException
from ..models import User
from ..schemas import UserCreate
from ..crud import create_user

router = APIRouter()

@router.post("/users/", response_model=User )
def register_user(user: UserCreate):
    db_user = create_user(user)
    if not db_user:
        raise HTTPException(status_code=400, detail="User  already exists")
    return db_user
