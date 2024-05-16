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
async def update_user_action_detail(user_action: User_Action):
    try:
        user_action=await user_action_service.update_user_action(user_action)
        print(f"message: user_action id:  {user_action.id} Update successful")
        return user_action
    except Exception as e:
        print(f"An error occurred during update user detail: {e}")
        raise e


@user_action_router.get('/get/{user_id}')
async def get_user_actions_by_user_id(user_id:int):
    try:
       user_actions_list= await user_action_service.get_user_actions_by_user_id(user_id)
       print(f"message: get all user actions of user id: {user_id } successfully")
       return user_actions_list
    except Exception as e:
       print(f"An error occurred during get user actions by user id: {e}")
       raise e

@user_action_router.get('/get/{user_id}/{user_action_id}')
async def get_user_action_by_user_id(user_id:int,user_action_id:int):
    try:
       user_action= await user_action_service.get_user_action_by_user_id(user_id,user_action_id)
       print(f"message: get  user action id: {user_action_id} of user id: {user_id } successfully")
       return user_action
    except Exception as e:
       print(f"An error occurred during get user action by user id: {e}")
       raise e

@user_action_router.get('/get')
async def get_users_actions():
    try:
       users_actions_list= await user_action_service.get_users_actions();
       print(f"message: get all users actions successfully")
       return users_actions_list
    except Exception as e:
       print(f"An error occurred during get  users actions: {e}")
       raise e

 # add getters by date/month?