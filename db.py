"""Set up the database connection and session.""" ""
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base

DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost/postgres"
# DATABASE_URL = "sqlite+aiosqlite:///./test.db"
# Note that (as far as I can tell from the docs and searching) there is no need
# to add 'check_same_thread=False' to the sqlite connection string, as
# SQLAlchemy version 1.4+ will automatically add it for you when using SQLite.

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
