import pytest
from datetime import datetime
from app.models.user_action import User_Action
from app.services import user_action_service

"""This module defines unit tests for user action-related functionalities in the app."""

@pytest.mark.asyncio
@pytest.mark.order(1)
async def test_create_user_action():
    """Test the functionality of creating a new user action.

    Creates a new user action object and verifies that it is successfully created in the database.
    """
    new_user_action = User_Action(id=0, user_id=0, type='expense', amount=100, datetime=datetime.now())
    result = await user_action_service.Create_user_action(new_user_action)
    assert result.id is not None
    assert result.user_id == new_user_action.user_id
    assert result.type == new_user_action.type
    assert result.amount == new_user_action.amount
    assert result.datetime == new_user_action.datetime

@pytest.mark.asyncio
@pytest.mark.order(2)
async def test_get_user_action_by_user_id():
    """Tests the retrieval of a user action by user ID."""
    user_id = 0
    user_action_id = 0
    result = await user_action_service.get_user_action_by_user_id(user_id, user_action_id)
    assert result.id == user_action_id
    assert result.user_id == user_id

@pytest.mark.asyncio
@pytest.mark.order(3)
async def test_update_user_action():
    """Tests the update of a user action."""
    user_action = User_Action(id=0, user_id=0, type='revenue', amount=200, datetime=datetime.now())
    result = await user_action_service.update_user_action(user_action)
    assert result == user_action

@pytest.mark.asyncio
@pytest.mark.order(4)
async def test_delete_user_action():
    """Tests the deletion of a user action."""
    user_action_id = 0
    result = await user_action_service.delete_user_action(user_action_id)
    assert result is None


