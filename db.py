from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost/postgres"

engine = create_async_engine(DATABASE_URL, echo=False)
Base = declarative_base()


async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False  # type: ignore
)
