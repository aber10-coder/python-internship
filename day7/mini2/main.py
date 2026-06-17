from fastapi import FastAPI
from schemas import TaskCreate,TaskResponse
from db import init_db, create_task,get_all_tasks

app = FastAPI()


@app.on_event("startup")
def startup():
    init_db()


@app.post("/tasks")
def add_task(task: TaskCreate):
    return create_task(task.title)

@app.get("/tasks",response_model=list[TaskResponse])
def get_tasks():
    return get_all_tasks()