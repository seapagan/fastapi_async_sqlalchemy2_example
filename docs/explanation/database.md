# The Database file (db.py)

The database setup is fairly straightforward, we will go through it line by
line.

## Imports

```python linenums="1"
"""Set up the database connection and session.""" ""
from collections.abc import AsyncGenerator
from typing import Any

from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase
```

Lines 1 to 11 are the imports. The only thing to note here is that we are using
the `AsyncGenerator` type hint for the `get_db` function. This is because we are
using the `yield` keyword in the function, which makes it a generator. The
`AsyncGenerator` type hint is a special type hint that is used for asynchronous
generators.

## Database Connection String

```python linenums="13"
DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost/postgres"
# DATABASE_URL = "sqlite+aiosqlite:///./test.db"
```

We set a variable to be used later which contains the database URL. We are using
PostgreSQL, but you can use any database that SQLAlchemy supports. The commented
out line is for SQLite, which is a good choice for testing. You can comment out
the PostgreSQL line (**13**)and uncomment the SQLite line (**14**)to use SQLite
instead.

This is a basic connection string, in reality you would want to use environment
variables to store the user/password and database name.

## The Base Class

```python linenums="20"
class Base(DeclarativeBase):
    """Base class for SQLAlchemy models.

    All other models should inherit from this class.
    """

    metadata = MetaData(
        naming_convention={
            "ix": "ix_%(column_0_label)s",
            "uq": "uq_%(table_name)s_%(column_0_name)s",
            "ck": "ck_%(table_name)s_%(constraint_name)s",
            "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
            "pk": "pk_%(table_name)s",
        }
    )
```

This takes the `DeclarativeBase` class from SQLAlchemy and adds a `metadata`
attribute to it. This is used to define the naming convention for the database
tables. **This is not required**, but it is a good idea to set this up for
consistency.

We will use this class as the base class for all of our future models.

## The database engine and session

```python linenums="37"
async_engine = create_async_engine(DATABASE_URL, echo=False)
```

Here on line 37 we create the database engine. The `create_async_engine`
function takes the database URL and returns an engine, the connection to the
database. The `echo` parameter is set to `False` to prevent SQLAlchemy from
outputting all of the SQL commands it is running. Note that it uses the
`DATABASE_URL` variable we set earlier.

```python linenums="38"
async_session = async_sessionmaker(async_engine, expire_on_commit=False)
```

Next, we create the session. The `async_sessionmaker` function takes the engine
and returns a session. The `expire_on_commit` parameter is set to `False` to
prevent SQLAlchemy from expiring objects on commit. This is required for
`asyncpg` to work properly.

We will NOT use this session directly, instead we will use the `get_db` function
below to get and release a session.

## The `get_db()` function

```python linenums="41"
async def get_db() -> AsyncGenerator[AsyncSession, Any]:
    """Get a database session.

    To be used for dependency injection.
    """
    async with async_session() as session, session.begin():
        yield session
```

This function is used to get a database session as a generator function. This
function is used for dependency injection, which is a fancy way of saying that
we will use it to pass the database session to other functions. Since we have
used the `with` statement, the session will be automatically closed (and data
comitted) when the function returns, usually after the related route is
complete.

!!! note
    Note that in line **46** we are using a combined `with` statement. This
    is a shortcut for using two nested `with` statements, one for the
    `async_session` and one for the `session.begin()`.

## The `init_models()` function

This function is used to create the database tables. It is called by the
`lifespan()` function at startup.

!!! note
    This function is only used in our demo, in a real application you would
    use a migration tool like
    [Alembic](https://alembic.sqlalchemy.org/en/latest/){:target="_blank"}
    instead.

```python linenums="50"
async def init_models() -> None:
    """Create tables if they don't already exist.

    In a real-life example we would use Alembic to manage migrations.
    """
    async with async_engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)  # noqa: ERA001
        await conn.run_sync(Base.metadata.create_all)
```

This function shows how to run a `syncronous` function in an `async` context
using the `async_engine` object directly instead of the `async_session` object.
On line **57** we use the `run_sync` method to run the `create_all` method of
the `Base.metadata` object (a syncronous function). This will create all of the
tables defined in the models.

Next, we will look at the models themselves and the Schemas used to validate
them within FastAPI.
