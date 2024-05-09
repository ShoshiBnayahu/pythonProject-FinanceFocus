from pydantic import BaseModel
class User_budget(BaseModel):
     user_id:str
     expenses:int
     revenues:int
