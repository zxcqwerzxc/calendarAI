import uvicorn
from fastapi import FastAPI
from fastapi.routing import APIRouter
from starlette.middleware.cors import CORSMiddleware

from src.api.handlers.chats_handlers import chat_router
from src.api.handlers.tasks_handlers import task_router
from src.api.handlers.users_handlers import user_router

from src.api.handlers.params_handlers import params_router

app = FastAPI(title='Calendar')
origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
main_api_router = APIRouter(prefix='/api/v1')

main_api_router.include_router(task_router, prefix='/task', tags=['Задачи'])
main_api_router.include_router(user_router, prefix='/user', tags=['Пользователи'])

main_api_router.include_router(params_router, prefix='/params', tags=['Параметры'])
main_api_router.include_router(chat_router, prefix='/chat', tags=['Чат'])
app.include_router(main_api_router)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0")

