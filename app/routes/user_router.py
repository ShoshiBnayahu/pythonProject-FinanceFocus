from fastapi import APIRouter, HTTPException
from app.services import user_service
from app.models.user import User
from pydantic import ValidationError

user_router = APIRouter()

@user_router.post('/login')
async def login(user: User):
    try:
        user_found = await user_service.login(user)
        if user_found:
            print(f" message: user id: {user_found.id} login successful")
            return user_found
        else:
            raise HTTPException(status_code=401, detail="Invalid credentials")
    except Exception as e:
        print(f"An error occurred during login: {e}")
        raise e


@user_router.post('/signup')
async def sign_up(user: User):
    try:
        new_user = await user_service.sign_up(user)
        print (f"message: user id: {user.id} Sign-up successful")
        return new_user
    except Exception as e:
        print(f"An error occurred during sign-up: {e}")
        raise e

@user_router.put('/update')
async def update_user_detail(user: User):
    try:
        user=await user_service.update_user_detail(user)
        print(f"message: user id:  {user.id} Update successful")
        return user
    except Exception as e:
        print(f"An error occurred during update user detail: {e}")
        raise e
