from fastapi import APIRouter
from pydantic import constr
from app.services import user_action_service
from app.models.user_action import User_Action
from utils.decorators import logger

user_action_router = APIRouter()
@user_action_router.post('/create')
@logger
async def create_user_action(user_action: User_Action):
    new_user_action = await user_action_service.create_user_action(user_action)
    return new_user_action

@user_action_router.delete('/delete/{user_action_id}')
@logger
async def delete_user_action(user_action_id: int):
    await user_action_service.delete_user_action(user_action_id)
    return f"message: user-action id:{user_action_id} deleted successfully"

@user_action_router.put('/update')
@logger
async def update_user_action_detail(user_action: User_Action):
    user_action=await user_action_service.update_user_action(user_action)
    return user_action

@user_action_router.get('/get/{user_id}')
@logger
async def get_user_actions_by_user_id(user_id:int):
    user_actions_list= await user_action_service.get_user_actions_by_user_id(user_id)
    return user_actions_list

@user_action_router.get('/get/{user_id}/{user_action_id}')
@logger
async def get_user_action_by_user_id(user_id:int,user_action_id:int):
    user_action= await user_action_service.get_user_action_by_user_id(user_id,user_action_id)
    return user_action

@user_action_router.get('/get')
@logger
async def get_users_actions():
    users_actions_list= await user_action_service.get_users_actions();
    return users_actions_list

#which getters I need to add?
@user_action_router.get('/get/{user_id}/{year}/{month}')
@logger
async def get_user_actions_by_month(user_id: int, year: int, month: int):
     user_filtered_actions = await user_action_service.get_user_actions_by_month(user_id, year, month)
     return user_filtered_actions

@user_action_router.get('/get/{user_id}')
@logger
async def get_user_actions_by_type(user_id: int, action_type:constr(pattern="revenue|expense")):
    user_filtered_actions = await user_action_service.get_user_actions_by_type(user_id, action_type)
    return user_filtered_actions
