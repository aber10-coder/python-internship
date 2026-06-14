from pydantic import BaseModel,ValidationError
from datetime import datetime
class user(BaseModel):
    username:str
    email:str

user=user(
    username="aber",
    email="aber@gmail.com"
)
print(user)