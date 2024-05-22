from datetime import datetime
from fastapi import HTTPException
from pymongo import DESCENDING
from app.models.user_action import User_Action
from app.services import user_service
from app.services.db_service import users_action

async def Create_user_action(new_user_action:User_Action):
    """Create a new user action.
        This function creates a new user action and inserts it into the database.
        """
    await user_service.get_user_by_id(new_user_action.user_id)
    new_user_action.id = await set_id()
    users_action.insert_one({
        "id": new_user_action.id,
        "user_id": new_user_action.user_id,
        "type": new_user_action.type,
        "amount": new_user_action.amount,
        "datetime": datetime.now()
    })
    return new_user_action
async def update_user_action(user_action: User_Action):
    """
        Update an existing user action.
        This function updates an existing user action in the database.
        """
    filter = {"id": user_action.id}
    new_values = {"$set": {"type": user_action.type,
                            "amount": user_action.amount,
                            "datetime":user_action.datetime}}
    result=users_action.update_one(filter, new_values)
    if result.raw_result.get('n') == 0:
        raise HTTPException(status_code=404, detail="invalid user action")
    return user_action

async def delete_user_action(user_action_id:int):
    """
        Delete a user action.
        This function deletes a user action from the database by its ID.
        """
    result=users_action.delete_one({"id": user_action_id})
    if result.raw_result.get('n') ==0:
        raise HTTPException(status_code=404, detail="invalid user action")

async def get_user_action_by_user_id(user_id:int,user_action_id:id):
    """
        Get a specific user action by user ID and action ID.
        This function retrieves a user action from the database by user ID and action ID.
        """
    await user_service.get_user_by_id(user_id)
    user_action = users_action.find_one({"id": user_action_id})
    user_action=User_Action(**user_action)
    if not user_action or user_action.user_id!=user_id:
        raise HTTPException(status_code=404, detail="Invalid user_action_id ")
    return user_action

async def get_user_actions_by_user_id(user_id:int):
    """
    Get all user actions for a specific user.
    This function retrieves all actions associated with a specific user ID from the database.
    """
    await user_service.get_user_by_id(user_id)
    user_actions_list = users_action.find({"user_id": user_id})
    user_actions_list=[User_Action(**user_action) for user_action in list(user_actions_list)]
    return user_actions_list

async def get_users_actions():
    """
    Get all user actions.
    This function retrieves all user actions from the database.
    """
    users_actions_list=users_action.find()
    users_actions_list = [ User_Action(**user_action) for user_action in list(users_actions_list)]
    return users_actions_list

async def get_user_actions_by_month(user_id: int, year: int, month: int):
    """
       Get user actions for a specific user by month.
       This function retrieves all user actions for a specific user and month.
       """
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
    """
       Get user actions for a specific user by type.
       This function retrieves all user actions of a specific type for a specific user.
       """
    await user_service.get_user_by_id(user_id)
    user_actions_list = users_action.find({
        "user_id": user_id,
        "type": action_type
    })
    user_filtered_actions = [User_Action(**action_type) for action_type in user_actions_list]
    return user_filtered_actions


async def get_user_actions_by_type_in_month(user_id: int, action_type: str, target_month: int):
    """
        Get user actions for a specific user by type and month.
        This function retrieves all user actions of a specific type for a specific user and month.
        """
    await user_service.get_user_by_id(user_id)
    user_actions_list = users_action.find({"user_id": user_id, "type": action_type})
    filtered_actions = []
    for action in user_actions_list:
        try:
            created_at_month = action['datetime'].month
            if created_at_month == target_month:
                filtered_actions.append(User_Action(**action))
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Error processing action: {action}, error: {e}")

    return filtered_actions


async def set_id():
    """
    Generate a new unique ID for a user action.
    This function finds the highest current ID in the database and increments it by one.
    """
    max_id_document = users_action.find_one({}, sort=[("id", DESCENDING)])
    if max_id_document:
        return max_id_document["id"] + 1
    else:
        return 0