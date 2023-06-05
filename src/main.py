from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from src.auth.base_config import auth_backend, fastapi_users
from src.auth.schemas import UserRead, UserCreate
from src.questions.router import router as router_questions
from src.pages.router import router as router_pages

app = FastAPI(
    title="Quiz App"
)

app.mount('/static', StaticFiles(directory='src/static'), name='static')

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Authentication"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Authentication"],
)

app.include_router(router_questions)
app.include_router(router_pages)
