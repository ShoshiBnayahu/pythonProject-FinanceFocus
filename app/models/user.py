from pydantic import BaseModel, constr

class User(BaseModel):
    id: int
    name: constr(pattern=r"^[a-zA-Z0-9_]+$")  # Ensures the name only contains alphanumeric characters and underscores
    password: constr(min_length=4, max_length=8)  # Ensures the password length is between 4 and 8 characters