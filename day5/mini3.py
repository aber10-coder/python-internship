from fastapi import FastAPI, HTTPException
app = FastAPI()
tasks = []
@app.post("/tasks")
def add_task(task: dict):
    task["id"] = len(tasks) + 1
    tasks.append(task)
    return task

@app.get("/tasks")
def get_tasks():
    return tasks

@app.delete("/tasks/{id}")
def delete_task(id: int):
    for task in tasks:
        if task["id"] == id:
            tasks.remove(task)
            return {"message": "Task deleted"}
    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )