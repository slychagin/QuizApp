import requests

from typing import Annotated, List, Type

from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.base_config import current_user
from src.auth.models import User
from src.database import get_async_session
from src.questions.models import Question

router = APIRouter(
    prefix="/questions",
    tags=["Questions"]
)

JSERVICE_URL = "https://jservice.io/api/random"


async def get_data_from_api(number: int) -> List[dict]:
    """Get questions by entered number from jservice.io API"""
    response = requests.get(JSERVICE_URL, params={"count": number})
    response.raise_for_status()
    questions_data = response.json()
    return questions_data


async def get_question_ids_from_db(session: AsyncSession = Depends(get_async_session)) -> List[int]:
    """Get all question id's from database"""
    stmt = select(Question)
    result = await session.execute(stmt)
    question_ids = [item.question_id for item in result.scalars()]
    return question_ids


async def get_last_saved_question(session: AsyncSession = Depends(get_async_session)) -> Type[Question]:
    """Get last saved question from db"""
    stmt = select(Question).order_by(Question.id.desc()).limit(1)
    result = await session.execute(stmt)
    last_question = result.scalar()
    return last_question


@router.post("/")
async def add_questions(
        questions_num: Annotated[int, Query(
                ge=1,
                le=100,
                description="Enter the number of questions you want to upload to the database"
            )],
        session: AsyncSession = Depends(get_async_session)
):
    """
    Save quiz questions in the database.
    In order to allow this post request only for registered users,
    you need to add the following to the arguments of this function:
        user: User = Depends(current_user)
    """
    try:
        # Get previous question
        previous_question = await get_last_saved_question(session)

        # Get questions by number from jservice.io API
        data = await get_data_from_api(questions_num)

        # Get all question id's from db
        ids = await get_question_ids_from_db(session)

        # Repeating question counter
        i = 0

        # Save unique questions in the database.
        # If question exists in db than increase repeating question counter.
        for item in data:
            if int(item["id"]) not in ids:
                stmt = insert(Question).values(
                    question_id=int(item["id"]),
                    question=str(item["question"]),
                    answer=str(item["answer"]),
                    created_at=str(item["created_at"].split("T")[0]),
                    air_date=str(item["airdate"].split("T")[0])
                )
                await session.execute(stmt)
            else:
                i += 1
        if i > 0:
            # Execute the function recursively until the counter is reset to zero
            await add_questions(questions_num=i, session=session)

        await session.commit()

        return {
            "Previous question": {
                "id": previous_question.question_id,
                "question": previous_question.question,
                "answer": previous_question.answer
            }
        } if previous_question else {}
    except Exception:
        raise HTTPException(status_code=500, detail={
            'status': 'error',
            'data': None,
            'details': None
        })
