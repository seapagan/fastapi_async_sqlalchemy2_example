"""An example of using FastAPI with Async SQLAlchemy 2."""
import subprocess
from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI
from sqlalchemy import select

from db import get_db, init_models
from models import User


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Run tasks before and after the server starts."""
    await init_models()
    yield


app = FastAPI(lifespan=lifespan)


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
