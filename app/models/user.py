from pydantic import BaseModel, constr


class User(BaseModel):
    id: int
    name: constr(pattern=r"^[a-zA-Z0-9_]+$")
    password: str

