from fastapi import FastAPI
from schemas import TaskCreate
from db import init_db, create_task

app = FastAPI()


@app.on_event("startup")
def startup():
    init_db()


@app.post("/tasks")
def add_task(task: TaskCreate):
    return create_task(task.title)