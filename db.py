"""Set up the database connection and session.""" ""
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base

DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost/postgres"

engine = create_async_engine(DATABASE_URL, echo=False)
Base = declarative_base()
async_session = async_sessionmaker(engine, expire_on_commit=False)


async def get_db():
    """Get a database session.

    To be used for dependency injection.
    """
    async with async_session() as session:
        async with session.begin():
            yield session


async def init_models():
    """Create tables if they don't already exist.

    In a real-life example we would use Alembic to manage migrations.
    """
    async with engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
