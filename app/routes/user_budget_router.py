from fastapi import APIRouter, HTTPException
from app.services import user_budget_service
from app.models.user_budget import User_budget

user_budget_router = APIRouter()
@user_budget_router.post('/create')
async def create_user_budget(user_budget: User_budget):
    try:
        new_user_budget = await user_budget_service.create(user_budget)
        print(new_user_budget)
        print (f"message: user-budget create successful")
        return new_user_budget
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred during create_user_budget: {e}")