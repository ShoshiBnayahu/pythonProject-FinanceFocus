from fastapi import APIRouter, HTTPException
from app.services import user_action_service
from app.models.user_action import User_Action

user_action_router = APIRouter()
@user_action_router.post('/create')
async def create_user_action(user_action: User_Action):
    try:
        new_user_action = await user_action_service.create_user_action(user_action)
        print (f"message: user-action id:{new_user_action.id} create successful")
        return new_user_action
    except Exception as e:
        print(f"An error occurred during create user action: {e}")
        raise e

