from fastapi import APIRouter
from pydantic import constr
from app.services import visual_service
from utils.decorators import logger

visual_router = APIRouter()
"""This module defines API routes for generating visualizations of user actions."""
@visual_router.get('/get/{user_id}/{year}')
@logger
async def get_user_graph(user_id: int, year: int):
    """Generates and shows a graph of monthly sums for a user in a given year."""
    month, monthly_sums = await visual_service.get_user_monthly_sums(user_id, year)
    visual_service.create_plot(month, monthly_sums)
    return "User graph shown"

@visual_router.get('/get/{user_id}/action_type/{action_type}')
@logger
async def get_user_monthly_by_type(user_id: int, action_type: constr(pattern="revenue|expense")):
    """Generates and shows a graph of monthly revenues or expenses for a user."""
    months, monthly_revenues = await visual_service.get_user_monthly_by_type(user_id, action_type)
    visual_service.create_plot(months, monthly_revenues)
    return "User graph shown"