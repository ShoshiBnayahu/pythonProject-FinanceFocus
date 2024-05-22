from fastapi import APIRouter
from app.services import user_service
from app.models.user import User
from utils.decorators import logger

user_router = APIRouter()
"""This module defines API routes for user management."""
@user_router.post('/login')
@logger
async def login(user: User):
    """Authenticates a user with their credentials."""
    user_found = await user_service.login(user)
    return user_found


@user_router.post('/signup')
@logger
async def sign_up(user: User):
    """Registers a new user."""
    new_user = await user_service.sign_up(user)
    return new_user


@user_router.put('/update')
@logger
async def update_user_detail(user: User):
    """Updates user details."""
    user = await user_service.update_user_detail(user)
    return user


@user_router.get('/get')
@logger
async def get_users():
     """Retrieves a list of all users."""
     users_list= await user_service.get_users();
     return users_list


@user_router.get('/get/{user_id}')
@logger
async def get_user_by_id(user_id: int):
    """Retrieves a specific user by their ID."""
    user_found = await user_service.get_user_by_id(user_id)
    return user_found