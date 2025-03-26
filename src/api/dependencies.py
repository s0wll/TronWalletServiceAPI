from typing import Annotated, AsyncGenerator

from fastapi import Depends, Query
from pydantic import BaseModel

from src.utils.db_manager import DBManager
from src.database import async_session_maker


class PaginationParams(BaseModel):
    page: Annotated[int | None, Query(1, ge=1)]
    per_page: Annotated[
        int | None, Query(None, ge=1, lt=30,)
    ]


PaginationDep = Annotated[PaginationParams, Depends()]


async def get_db() -> AsyncGenerator[DBManager, None]:
    async with DBManager(session_factory=async_session_maker) as db:
        yield db


DBDep = Annotated[DBManager, Depends(get_db)]