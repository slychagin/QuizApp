from fastapi import (
    APIRouter,
    Request,
    Form,
    Depends
)
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import HTMLResponse, JSONResponse

from src.database import get_async_session
from src.questions.router import add_questions

router = APIRouter(
    tags=['HTML Templates']
)


templates = Jinja2Templates(directory='src/templates')


@router.get('/', response_class=HTMLResponse)
def get_index_template(request: Request):
    """Return index template"""
    return templates.TemplateResponse('index.html', {'request': request})


@router.post('/upload')
async def upload_questions(
        questions_num: int = Form(ge=1, le=100),
        session: AsyncSession = Depends(get_async_session)
):
    """Save quiz questions in the database."""
    result = await add_questions(
        questions_num=questions_num,
        session=session
    )
    return JSONResponse(content=result)
