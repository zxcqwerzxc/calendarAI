import uvicorn
from fastapi import FastAPI
from fastapi.routing import APIRouter

from src.api.handlers.tasks_handlers import task_router
from src.api.handlers.users_handlers import user_router

app = FastAPI(title='ic-investigative-work')

main_api_router = APIRouter(prefix='/api/v1')

main_api_router.include_router(task_router, prefix='/task', tags=['Задачи'])
main_api_router.include_router(user_router, prefix='/user', tags=['Пользователи'])
app.include_router(main_api_router)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0")

