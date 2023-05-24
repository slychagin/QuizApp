import pytest
import requests
from httpx import AsyncClient
from sqlalchemy import select, insert

from src.auth.base_config import current_user
from src.main import app
from src.questions.models import Question
from tests.conftest import async_session_maker
from tests.data import db_data

JSERVICE_URL = "https://jservice.io/api/random"


@pytest.fixture()
async def add_questions_to_db():
    """
    This fixture insert questions to the database.
    Data is taken from data.py
    """
    async with async_session_maker() as session:
        for item in db_data:
            stmt = insert(Question).values(
                question_id=int(item["id"]),
                question=str(item["question"]),
                answer=str(item["answer"]),
                created_at=str(item["created_at"].split("T")[0]),
                air_date=str(item["airdate"].split("T")[0])
            )
            await session.execute(stmt)
        await session.commit()


async def test_get_data_from_api():
    """Test getting data from jservice.io API"""
    response = requests.get(JSERVICE_URL, params={"count": 3})
    data = response.json()

    assert response.status_code == 200
    assert len(data) == 3


async def test_get_question_ids_from_db(add_questions_to_db):
    """Test getting question id's from database"""
    async with async_session_maker() as session:
        stmt = select(Question)
        result = await session.execute(stmt)
        question_ids = [item.question_id for item in result.scalars()]

    assert len(question_ids) == 3
    for i in question_ids:
        assert type(i) == int


async def test_get_last_saved_question(add_questions_to_db):
    """Tests that the last question saved to the database matches
    the last question in the data.py file
    """
    async with async_session_maker() as session:
        stmt = select(Question).order_by(Question.id.desc()).limit(1)
        result = await session.execute(stmt)
        last_question = result.scalar()

        assert last_question.question_id == 60806


async def test_add_questions(ac: AsyncClient):
    """Test that questions was added to the database"""
    def skip_auth():
        pass
    app.dependency_overrides[current_user] = skip_auth
    response = await ac.post("/questions/", params={"questions_num": 3})

    assert response.status_code == 200
