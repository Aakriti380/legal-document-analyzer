from fastapi import APIRouter  #to organise routes
from fastapi import HTTPException

from models.user import(
    
    UserRegister,
    UserLogin
    )

from config.database import(
    users_collection
)

from utils.password import (
    hash_password,
    verify_password
)

from utils.jwt_handler import (
    create_access_token
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/register")
def register(user:UserRegister):
    existing_user =users_collection.find_one(
        {"eamil":user.email}
    )
    
    if existing_user:
        raise HTTPException(
            
             status_code=400,
            detail="User already exists"
            
        )
    
    hashed_password=hash_password(
        user.password
    )
    
    users_collection.insert_one({
        "name": user.name,
        "email": user.email,
        "password": hashed_password
    })
    
    return {
        "message": "User registered successfully"
    }

@router.post("/login")
def login(user: UserLogin):

    existing_user = users_collection.find_one(
        {"email": user.email}
    )

    if not existing_user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    if not verify_password(
        user.password,
        existing_user["password"]
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid password"
        )

    token = create_access_token({
        "user_id": str(existing_user["_id"]),
        "email": existing_user["email"]
    })

    return {
        "access_token": token
    }
