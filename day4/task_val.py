from pydantic import BaseModel,ValidationError

class TaskModel(BaseModel):
    title:str
    priority:str="low"
    completed:bool="False"

task1=TaskModel(title="Python")
print(task1.model_dump())

try:
    task2=TaskModel(title=123)
except ValidationError as e:
    print(e)