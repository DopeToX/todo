from fastapi import FastAPI, HTTPException, Depends, Security
from fastapi.security import APIKeyHeader

from crud import *
from auth import check_token, create_token
from models import Task

app = FastAPI()

# --- AUTH (Swagger-friendly) ---
api_key_header = APIKeyHeader(name="Authorization")


def auth(token: str = Security(api_key_header)):
    if not token:
        raise HTTPException(status_code=401, detail="No token")

    if not check_token(token):
        raise HTTPException(status_code=401, detail="Invalid token")

    return True


# --- LOGIN ---
@app.post("/login")
def login():
    return {"token": create_token(1)}


# --- TASKS ---
@app.get("/tasks")
def all_tasks(ok: bool = Depends(auth)):
    return get_all_tasks()


@app.get("/tasks/incomplete")
def incomplete(ok: bool = Depends(auth)):
    return get_incomplete_tasks()


@app.post("/tasks")
def create(task: Task, ok: bool = Depends(auth)):
    add_task(task.title)
    return {"msg": "added"}


@app.put("/tasks/{task_id}")
def update(task_id: int, ok: bool = Depends(auth)):
    update_task(task_id)
    return {"msg": "updated"}


@app.delete("/tasks/{task_id}")
def delete(task_id: int, ok: bool = Depends(auth)):
    delete_task(task_id)
    return {"msg": "deleted"}