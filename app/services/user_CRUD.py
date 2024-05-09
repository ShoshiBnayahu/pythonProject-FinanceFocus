from pymongo import DESCENDING

from app.models.user import User
from app.services.db import users

async def login(user: User):
    existing_user = users.find_one({"name": user.name, "password": user.password})
    print("")
    if existing_user:
        return User(**existing_user)


async def sign_up(new_user:User):
    user_id = await set_id()
    users.insert_one({
        "id": user_id,
        "name": new_user.name,
        "password": new_user.password
    })
    print("Sign-up successful.")
    new_user=users.find_one({"id":user_id})
    return new_user

async def update_user(updated_user:User):
    filter = {"id": updated_user.id}
    new_values = {"$set": {"name": updated_user.name, "password": updated_user.password}}
    users.update_one(filter,new_values)
    print ("Update successful.")
    return updated_user
async def set_id():
   max_id_document = users.find_one({}, sort=[("id", DESCENDING)])
   if max_id_document:
    return(max_id_document["id"]+1)
   else:
    return 0
