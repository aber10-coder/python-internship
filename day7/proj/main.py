from fastapi import FastAPI, HTTPException

from schemas import (
    TaskCreate,
    TaskUpdate,
    TaskResponse
)

from database import (
    init_db,
    db_create_task,
    db_get_all_tasks,
    db_get_task,
    db_update_task,
    db_delete_task
)

app = FastAPI()


@app.on_event("startup")
def startup():
    init_db()


@app.post("/tasks", response_model=TaskResponse)
def create_task(task: TaskCreate):
    return db_create_task(task)


@app.get("/tasks", response_model=list[TaskResponse])
def get_tasks(status: str | None = None):
    return db_get_all_tasks(status)


@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):
    task = db_get_task(task_id)

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task


@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task: TaskUpdate):
    updated_task = db_update_task(task_id, task)

    if updated_task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return updated_task


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    deleted = db_delete_task(task_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return {"message": "Task deleted successfully"}