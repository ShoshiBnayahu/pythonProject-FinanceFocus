from fastapi import APIRouter, HTTPException
from app.services import user_service
from app.models.user import User
from utils.decorators import logger

user_router = APIRouter()
@user_router.post('/login')
@logger
async def login(user: User):
    user_found = await user_service.login(user)
    print(f"details: user id: {user_found.id} login successfully")
    return user_found

@user_router.post('/signup')
@logger
async def sign_up(user: User):
    new_user = await user_service.sign_up(user)
    print (f"details: user id: {user.id} Sign-up successfully")
    return new_user

@user_router.put('/update')
@logger
async def update_user_detail(user: User):
    user=await user_service.update_user_detail(user)
    print(f"details: user id:  {user.id} Update successfully")
    return user

@user_router.get('/get')
@logger
async def get_users():
    users_list= await user_service.get_users();
    return users_list

@user_router.get('/get/{user_id}')
@logger
async def get_user_by_id(user_id: int):
    user_found = await user_service.get_user_by_id(user_id)
    print(f"details: get user id: {user_found.id}  successfully")
    return user_found








