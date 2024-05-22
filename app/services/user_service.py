from pymongo import DESCENDING
from fastapi import HTTPException

from app.models.user import User
from app.services.db_service import users

async def login(user: User):
    """
        Authenticate a user.
        This function checks if the provided user credentials exist in the database.
        If they do, the user details are returned. Otherwise, an HTTP 404 error is raised.
        """
    existing_user = users.find_one({"name": user.name, "password": user.password})
    if not existing_user:
        raise HTTPException(status_code=404, detail="invalid credentials")
    return User(**existing_user)


async def sign_up(new_user:User):
    """
       Register a new user.
       This function assigns a unique ID to a new user and inserts their details into the database.
       """
    new_user.id = await set_id()
    users.insert_one({
        "id": new_user.id,
        "name": new_user.name,
        "password": new_user.password
    })
    return new_user

async def update_user_detail(updated_user:User):
    """
        Update user details.
        This function updates the name and password of an existing user in the database.
        If the user does not exist, an HTTP 404 error is raised.
        """
    filter = {"id": updated_user.id}
    new_values = {"$set": {"name": updated_user.name, "password": updated_user.password}}
    result=users.update_one(filter,new_values)
    if result.raw_result.get('n') == 0:
        raise HTTPException(status_code=404, detail="invalid user")
    return updated_user

async def get_users():
    """
        Retrieve all users.
        This function retrieves all user records from the database.
        """
    users_list=users.find()
    users_list = [ User(**user) for user in list(users_list)]
    return users_list

async def get_user_by_id(user_id:int):
    """
        Retrieve a user by ID.
        This function retrieves a user record from the database based on the provided user ID.
        If the user does not exist, an HTTP 404 error is raised.
        """
    existing_user = users.find_one({"id": user_id})
    if not existing_user:
        raise HTTPException(status_code=404, detail="Invalid user_id ")
    return User(**existing_user)

async def set_id():
    """
        Generate a new unique user ID.
        This function finds the highest current user ID in the database and increments it by one.
        """
    max_id_document = users.find_one({}, sort=[("id", DESCENDING)])
    if max_id_document:
     return(max_id_document["id"]+1)
    else:
     return 0