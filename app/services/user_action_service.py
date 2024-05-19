from _datetime import datetime
from pymongo import DESCENDING
from app.models.user_action import User_Action
from app.services.db_service import users_action
from app.services import user_service
from fastapi import HTTPException

async def create_user_action(new_user_action:User_Action):
    await user_service.get_user_by_id(new_user_action.user_id)
    new_user_action.id=await set_id()
    users_action.insert_one({
            "id": new_user_action.id,
            "user_id": new_user_action.user_id,
            "type": new_user_action.type,
            "amount": new_user_action.amount,
            "datetime":datetime.now()
        })
    return new_user_action


    # עדכון: אילו שדות?
async def update_user_action(user_action: User_Action):
    filter = {"id": user_action.id}
    new_values = {"$set": { "type": user_action.type,
                            "amount": user_action.amount,
                            "datetime":user_action.datetime}}
    result=users_action.update_one(filter, new_values)
    if result.raw_result.get('n') == 0:
        raise HTTPException(status_code=404, detail="Invalid user_action_id ")
    return user_action

async def delete_user_action(user_action_id:int):
    result=users_action.delete_one({"id": user_action_id})
    if result.raw_result.get('n')==0:
        raise HTTPException(status_code=404, detail="Invalid user_action_id ")

async def get_user_action_by_user_id(user_id:int,user_action_id:id):
    await user_service.get_user_by_id(user_id)
    user_action = users_action.find_one({"id": user_action_id})
    user_action=User_Action(**user_action)
    if not user_action or user_action.user_id!=user_id:
        raise HTTPException(status_code=404, detail="Invalid user_action_id ")
    return user_action

async def get_user_actions_by_user_id(user_id:int):
    await user_service.get_user_by_id(user_id)
    user_actions_list = users_action.find({"user_id": user_id})
    user_actions_list=[User_Action(**user_action) for user_action in list(user_actions_list)]
    return user_actions_list

async def get_users_actions():
    users_actions_list=users_action.find()
    users_actions_list = [ User_Action(**user_action) for user_action in list(users_actions_list)]
    return users_actions_list

async def get_user_actions_by_month(user_id: int, year: int, month: int):
    await user_service.get_user_by_id(user_id)
    start_date = datetime(year, month, 1, 0, 0, 0)
    if month == 12:
        end_date = datetime(year + 1, 1, 1, 0, 0, 0)
    else:
        end_date = datetime(year, month + 1, 1, 0, 0, 0)
    user_actions_list = users_action.find({
        "user_id": user_id,
        "datetime": {
            "$gte": start_date,
            "$lte": end_date
        }
    })
    user_filtered_actions = [User_Action(**user_action) for user_action in user_actions_list]
    return user_filtered_actions

async def get_user_actions_by_type(user_id: int, action_type: str):
    await user_service.get_user_by_id(user_id)
    user_actions_list = users_action.find({
        "user_id": user_id,
        "type": action_type
    })
    user_filtered_actions = [User_Action(**action_type) for action_type in user_actions_list]
    return user_filtered_actions

async def set_id():
    max_id_document = users_action.find_one({}, sort=[("id", DESCENDING)])
    if max_id_document:
     return(max_id_document["id"]+1)
    else:
     return 0

