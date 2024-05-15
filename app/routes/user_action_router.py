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

@user_action_router.delete('/delete/{user_action_id}')
async def delete_user_action(user_action_id: int):
    try:
        await user_action_service.delete_user_action(user_action_id)
        print (f"message: user-action id:{user_action_id} deleted successfully")
        return f"message: user-action id:{user_action_id} deleted successfully"
    except Exception as e:
        print(f"An error occurred during delete user action: {e}")
        raise e

@user_action_router.put('/update')
async def update_user__action_detail(user_action: User_Action):
    try:
        user_action=await user_action_service.update_user_action(user_action)
        print(f"message: user_action id:  {user_action.id} Update successful")
        return user_action
    except Exception as e:
        print(f"An error occurred during update user detail: {e}")
        raise e