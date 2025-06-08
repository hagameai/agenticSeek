from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

# Importing the task management functions from interaction.py
from ..interaction import TaskManager

# Create an instance of APIRouter
router = APIRouter()

class Task(BaseModel):
    id: int
    description: str
    completed: bool

class TaskCreate(BaseModel):
    description: str

@router.post("/tasks/", response_model=Task)
async def create_task(task: TaskCreate):
    """Create a new task in the task manager."""
    try:
        new_task = TaskManager.create_task(task.description)
        return new_task
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/tasks/", response_model=List[Task])
async def read_tasks():
    """Retrieve all tasks from the task manager."""
    try:
        tasks = TaskManager.get_all_tasks()
        return tasks
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, task: TaskCreate):
    """Update an existing task by ID."""
    try:
        updated_task = TaskManager.update_task(task_id, task.description)
        return updated_task
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/tasks/{task_id}", response_model=dict)
async def delete_task(task_id: int):
    """Delete a task by ID."""
    try:
        TaskManager.delete_task(task_id)
        return {"detail": "Task deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
