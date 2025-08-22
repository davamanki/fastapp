from sqlalchemy import select

from app.database import new_session, TaskOrm
from app.schemas import TaskAdd, Task


class TaskRepository:
    @classmethod
    async def add_one(cls, data: TaskAdd) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()
            task = TaskOrm(**task_dict) # вот строчка
            session.add(task)
            await session.commit()
            return task.id


    @classmethod
    async def find_all(cls):
        async with new_session() as session:
            query = select(TaskOrm)
            result = await session.execute(query)
            task_models = result.scalars().all()
            return task_models