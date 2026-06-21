from fastapi import APIRouter, HTTPException, Depends
from schemas import TaskCreate, TaskUpdate, TaskResponse
from auth import get_current_user
from db import get_connection
from typing import List

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.post("/", response_model=TaskResponse)
def create_task(task: TaskCreate, current_user: str = Depends(get_current_user)):
    conn = get_connection()
    c = conn.cursor()

    c.execute(
        "INSERT INTO tasks (title, description, done, owner_email) VALUES (?, ?, 0, ?)",
        (task.title, task.description, current_user)
    )
    task_id = c.lastrowid
    conn.commit()

    c.execute("SELECT * FROM tasks WHERE id=?", (task_id,))
    row = c.fetchone()
    conn.close()
    return dict(row)


@router.get("/", response_model=List[TaskResponse])
def get_tasks(current_user: str = Depends(get_current_user)):
    conn = get_connection()
    c = conn.cursor()

    c.execute("SELECT * FROM tasks WHERE owner_email=?", (current_user,))
    rows = c.fetchall()
    conn.close()
    return [dict(row) for row in rows]


@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, current_user: str = Depends(get_current_user)):
    conn = get_connection()
    c = conn.cursor()

    c.execute("SELECT * FROM tasks WHERE id=? AND owner_email=?", (task_id, current_user))
    row = c.fetchone()
    conn.close()

    if not row:
        raise HTTPException(status_code=404, detail="Task not found")
    return dict(row)


@router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task: TaskUpdate, current_user: str = Depends(get_current_user)):
    conn = get_connection()
    c = conn.cursor()

    c.execute("SELECT * FROM tasks WHERE id=? AND owner_email=?", (task_id, current_user))
    existing = c.fetchone()

    if not existing:
        conn.close()
        raise HTTPException(status_code=404, detail="Task not found")

    updated_title = task.title if task.title is not None else existing["title"]
    updated_desc = task.description if task.description is not None else existing["description"]
    updated_done = task.done if task.done is not None else existing["done"]

    c.execute(
        "UPDATE tasks SET title=?, description=?, done=? WHERE id=?",
        (updated_title, updated_desc, updated_done, task_id)
    )
    conn.commit()

    c.execute("SELECT * FROM tasks WHERE id=?", (task_id,))
    row = c.fetchone()
    conn.close()
    return dict(row)


@router.delete("/{task_id}")
def delete_task(task_id: int, current_user: str = Depends(get_current_user)):
    conn = get_connection()
    c = conn.cursor()

    c.execute("SELECT * FROM tasks WHERE id=? AND owner_email=?", (task_id, current_user))
    if not c.fetchone():
        conn.close()
        raise HTTPException(status_code=404, detail="Task not found")

    c.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    conn.close()
    return {"message": "Task deleted"}