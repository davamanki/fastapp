from typing import Annotated, Any, Coroutine

from fastapi import APIRouter, Depends

from app.repository import TaskRepository
from app.schemas import TaskAdd, Task, TaskId

router = APIRouter(
prefix="/tasks",
    tags=["Задачи"]
)

@router.post('')
async def add_task(task: Annotated[TaskAdd, Depends()]) -> dict[str, bool | int]:
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task_id}

@router.get("")
async def get_tasks() -> list[Task]:
    tasks = await TaskRepository.find_all()
    return tasks