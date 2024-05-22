# import asyncio
import pytest
from app.models.user import User
from app.services import user_service

"""This module defines unit tests for user-related functionalities in the app."""

@pytest.mark.parametrize("user", [User(id=0, name='michalile', password='123456')])
@pytest.mark.asyncio
@pytest.mark.order(2)
async def test_login(user):
    """Tests the login functionality for an existing user.
    Attempts to log in a user and checks that the user was successfully authenticated.
    """
    result = await user_service.login(user)
    print(result)
    assert result == user

@pytest.mark.asyncio
@pytest.mark.order(1)
async def test_sign_up():
    """Tests the sign-up functionality for a new user.
    Creates a new user and checks that the user was successfully registered and received a unique identifier.
    """
    new_user = User(id=0, name='michalile', password='123456')
    result = await user_service.sign_up(new_user)
    assert result.id is not None
    assert result.name == new_user.name
    assert result.password == new_user.password

@pytest.mark.asyncio
@pytest.mark.order(3)
async def test_get_user_by_id():
    """Checks the functionality of retrieving a user by ID.
       Verifies that the user found by the given ID matches the expected user.
    """
    user = User(id=0, name='michalile', password='123456')
    result = await user_service.get_user_by_id(0)
    assert result == user