from bson import ObjectId
from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from bson import ObjectId

from app.services import user_CRUD
from app.models.user import User

user_router = APIRouter()

@user_router.post('/login')
async def login(user: User):
    try:
        user_found = await user_CRUD.login(user)
        if user_found:
            print(f"message: {user_found.name} login successful")
            return user_found
        else:
            raise HTTPException(status_code=401, detail="Invalid credentials")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred during login: {e}")

@user_router.post('/signup')
async def sign_up(user: User):
    try:
        new_user = await user_CRUD.sign_up(user)
        print(new_user)
        print (f"message: {user.name} Sign-up successful")
        return new_user
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred during sign-up: {e}")

@user_router.put('/update')
async def update_user(user: User):
    try:
        await user_CRUD.update_user(user)
        print(f"message: {user.name} Update successful")
        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred during update: {e}")
