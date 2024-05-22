from datetime import datetime
from pydantic import BaseModel, Field, field_validator


class User_Action(BaseModel):
    id: int
    user_id: int
    type: str
    amount: int
    datetime: datetime

    @field_validator('type')
    @classmethod
    def check_type(cls, type):
        """Validates that the type is either 'revenue' or 'expense'"""
        if type not in ['revenue', 'expense']:
            raise ValueError('error, type must be revenue or expense')
        return type

    @field_validator('amount', 'user_id')
    @classmethod
    def check_positiveNumber(cls, num):
        # Ensures that the amount and user_id are positive numbers
        if num < 0:
            raise ValueError('error, negative number!')
        return num
