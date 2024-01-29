"""An example of using FastAPI with Async SQLAlchemy 2."""
from collections.abc import AsyncGenerator, Sequence
from contextlib import asynccontextmanager
from typing import Any

import uvicorn
from db import get_db, init_models
from fastapi import Depends, FastAPI
from models import User
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[Any, None]:  # noqa: ARG001
    """Run tasks before and after the server starts."""
    await init_models()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root() -> dict[str, str]:
    """Root endpoint."""
    return {"message": "Test API for FastAPI and Async SQLAlchemy ."}


@app.post("/users/")
async def create_user(
    name: str, email: str, session: AsyncSession = Depends(get_db)
) -> User:
    """Add a user."""
    user = User(name=name, email=email)
    session.add(user)
    return user


@app.get("/users/")
async def get_users(session: AsyncSession = Depends(get_db)) -> Sequence[User]:
    """Get all users."""
    result = await session.execute(select(User))
    return result.scalars().all()


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
