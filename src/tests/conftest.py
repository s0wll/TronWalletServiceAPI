from typing import AsyncGenerator

from httpx import ASGITransport, AsyncClient
import pytest

from src.main import app
from src.database import async_session_maker
from src.database import Base, engine
from src.utils.db_manager import DBManager
from src.config import settings


@pytest.fixture(scope="session", autouse=True)
def check_test_mode() -> None:
    assert settings.MODE == "TEST"
    assert settings.DB_NAME == "TronWalletServiceAPI-test"


@pytest.fixture(scope="function")
async def db() -> AsyncGenerator[DBManager]:
    async with DBManager(session_factory=async_session_maker) as db:
        yield db


@pytest.fixture(scope="session", autouse=True)
async def setup_database(check_test_mode) -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


@pytest.fixture(scope="session")
async def ac() -> AsyncGenerator[AsyncClient]:  # Асинхронный клиент для тестирования
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        yield ac