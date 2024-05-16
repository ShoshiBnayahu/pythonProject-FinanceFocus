import json

from fastapi import APIRouter, HTTPException
from app.services import user_service
from app.models.user import User

user_router = APIRouter()

@user_router.post('/login')
async def login(user: User):
    try:
        user_found = await user_service.login(user)
        print(f" message: user id: {user_found.id} login successful")
        return user_found
    except Exception as e:
        print(f"An error occurred during login: {e}")
        raise e


@user_router.post('/signup')
async def sign_up(user: User):
    try:
        new_user = await user_service.sign_up(user)
        print (f"message: user id: {user.id} Sign-up successful")
        print(new_user)
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

@user_router.get('/get')
async def get_users():
    try:
       users_list= await user_service.get_users();
       print(f"message: get all users successfully")
       return users_list
    except Exception as e:
       print(f"An error occurred during get  users: {e}")
       raise e
@user_router.get('/get/{user_id}')
async def get_user_by_id(user_id: int):
    try:
        user_found = await user_service.get_user_by_id(user_id)
        print(f" message: get user id: {user_found.id}  successfully")
        return user_found
    except Exception as e:
        print(f"An error occurred during get user by id: {e}")
        raise e