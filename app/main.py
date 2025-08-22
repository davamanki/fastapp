from fastapi import FastAPI
import uvicorn
from contextlib import asynccontextmanager
from app.database import create_table, delete_table
from app.router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_table()
    print("База очищена")
    await create_table()
    print("База готова к работе")
    yield
    print("Выключение")


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)