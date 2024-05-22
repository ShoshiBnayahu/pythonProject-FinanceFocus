from _datetime import datetime
from pydantic import BaseModel,field_validator

class User_Action(BaseModel):
     id:int
     user_id:int
     type:str
     amount:int
     datetime:datetime

     @field_validator('type')
     def check_type(self, type):
         """Validates that the type is either 'revenue' or 'expense'"""
         if type not in ['revenue','expense']:
            raise ValueError('error,type must to be revenue or expense')
         return type
     @field_validator('amount','user_id')
     def check_positiveNumber(self, num):
        # Ensures that the amount and user_id are positive numbers
        if num < 0:
            raise ValueError('error, negative number! ')
        return num