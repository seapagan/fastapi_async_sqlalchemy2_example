"""An example of using FastAPI with Async SQLAlchemy 2."""
import subprocess
from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI
from sqlalchemy import select

from db import Base, async_session, engine
from models import User


async def init_models():
    """Create tables if they don't already exist.

    In a real-life example we would use Alembic to manage migrations.
    """
    async with engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Run tasks before and after the server starts."""
    await init_models()
    yield


app = FastAPI(lifespan=lifespan)


async def get_db():
    """Get a database session.

    To be used for dependency injection.
    """
    async with async_session() as session:
        async with session.begin():
            yield session


@app.get("/")
async def root():
    """Root endpoint."""
    return {"message": "Test API for FastAPI and Async SQLAlchemy ."}


@app.post("/users/")
async def create_user(name: str, email: str, session=Depends(get_db)):
    """Add a user."""
    user = User(name=name, email=email)
    session.add(user)
    return user


@app.get("/users/")
async def get_users(session=Depends(get_db)):
    """Get all users."""
    result = await session.execute(select(User))
    users = result.scalars().all()
    return users


if __name__ == "__main__":
    subprocess.call(["uvicorn", "main:app", "--reload"])
