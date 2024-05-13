from _datetime import datetime
from pymongo import DESCENDING
from app.models.user_action import User_Action
from app.services.db_service import users_action

async def create_user_action(new_user_action:User_Action):
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
    new_values = {"$set": {"type": user_action.type,
                            "amount": user_action.amount,
                            "datetime":user_action.datetime}}
    users_action.update_one(filter, new_values)
    return user_action

   # מחיקה לא צריכה להיות לפי params
async def delete_user_action(user_action: User_Action):
    existing_user_action = users_action.delete_one({"id": user_action.id})
    return existing_user_action


async def set_id():
    max_id_document = users_action.find_one({}, sort=[("id", DESCENDING)])
    if max_id_document:
     return(max_id_document["id"]+1)
    else:
     return 0
    ##צריך להוסיף שליפת נתונים