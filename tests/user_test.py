import asyncio
import pytest
from app.models.user import User
from app.services import user_service

"""This module defines unit tests for user-related functionalities in the app."""

@pytest.mark.parametrize("user,expected_id, expected_name, expected_password", [
    (User(id=3, name='u', password='12345'), 3, 'u', '12345'),
    (User(id=0, name='shoshi', password='1234'), 0, 'shoshi', '1234'),
])
@pytest.mark.asyncio
async def test_login(user, expected_id, expected_name, expected_password):

    """Tests the login functionality.
    Uses parameters of a specific user and the expected output of user details.
    Checks that the output of the login function matches the expected user details.
    """
    result = await user_service.login(user)
    assert result.id == expected_id
    assert result.name == expected_name
    assert result.password == expected_password

@pytest.mark.asyncio
async def test_sign_up():

    """Tests the sign-up functionality for a new user.
    Creates a new user and checks that the user was successfully registered and received a unique identifier.
    """
    new_user = User(id=9, name='michalile', password='123456')
    result = await user_service.sign_up(new_user)
    assert result == new_user
    assert result.id is not None

@pytest.mark.asyncio
async def test_update_user_detail():

    """Checks the functionality of updating user details.
    Creates a user with new details and verifies that the details were successfully updated.
    """
    updated_user = User(id=6, name='shoshana', password='1234')
    result = await user_service.update_user_detail(updated_user)
    assert result == updated_user


@pytest.mark.asyncio
async def test_get_user_by_id():
    """Checks the functionality of retrieving a user by ID.
       Verifies that the user found by the given ID matches the expected user.
    """
    user = User(id=6, name='shoshana', password='1234')
    result = await user_service.get_user_by_id(6)
    assert result == user