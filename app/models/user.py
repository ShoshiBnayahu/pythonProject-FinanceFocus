from pydantic import BaseModel, constr

class User(BaseModel):
    id: int
    name: constr(pattern=r"^[a-zA-Z0-9_]+$")
    password: constr(min_length=4, max_length=8)

