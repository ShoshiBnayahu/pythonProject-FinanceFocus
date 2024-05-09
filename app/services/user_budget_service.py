from datetime  import datetime
from pymongo import DESCENDING

from app.models.user_budget import User_budget
from app.services.db_service import users_budget




async def create(new_user_budget:User_budget):
    user_budget_id = await set_id()
    now=datetime.now()
    users_budget.insert_one({
        "id": user_budget_id,
        "user_id": new_user_budget.user_id,
        "expenses": new_user_budget.expenses,
        "revenues": new_user_budget.revenues,
        "datetime":now

    })
    print("create user_budget successful.")
    new_user_budget=users_budget.find_one({"id":user_budget_id})
    return new_user_budget


async def set_id():
   max_id_document = users_budget.find_one({}, sort=[("id", DESCENDING)])
   if max_id_document:
    return(max_id_document["id"]+1)
   else:
    return 0
