from pydantic import BaseModel
from typing import Optional

class TaskCreate(BaseModel):
    title:str
    status:bool

class TaskUpdate(BaseModel):
    title:Optional[str]=None
    status:Optional[bool]=None

class TaskResponse(BaseModel):
    id:int
    title:str
    status:bool


    