# Using this example

## Installation

Clone [this repository][repo]{:target="_blank"} and install the
dependencies. This project uses [Poetry][poetry]{:target="_blank"} for
dependency management which should be installed on your system first.

Install the dependencies:

```console
poetry install
```

Then switch to the virtual environment:

```console
poetry shell
```

## Usage

Run the server using `Uvicorn`:

```console
uvicorn main:app --reload
```

!!! note
    You can also run the server by just executing the `main.py` file:

    ```console
    python main.py
    ```

    or using the included `POE` alias:

    ```console
    poe serve
    ```

Then open your browser at
[http://localhost:8000](http://localhost:8000){:target="_blank"}.

There is only one endpoint available: `/users`. It returns a list of all users
for a `GET` request and creates a new user for a `POST` request.

### Local Postgres server using Docker

This example uses [PostgreSQL][postgres]{:target="_blank"} as the database. If
you dont have a local PostgreSQL database running, you can start one with
[Docker][docker]{:target="_blank"} using the following command:

```console
docker run \
  --rm   \
  --name  postgres \
  -p 5432:5432 \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=postgres \
  -d postgres
```

This will run a PostgreSQL database in a Docker container in the background.
When you are finished and want to stop the database, run:

```console
docker stop postgres
```

If needed, you can connect to the database managment by :

```console
docker exec -it postgres psql -U postgres
```

This will allow you to edit or delete the database or records.

### Use SQLite instead of PostgreSQL

For testing purposes, you can also use [SQLite][sqlite]{:target="_blank"}
instead of PostgreSQL. To do so, open the `db.py` file and comment out the
PostgreSQL database in the `DATABASE_URL` environment variable and uncomment the
SQLite database.

```python
# DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost/postgres"
DATABASE_URL = "sqlite+aiosqlite:///./test.db"
```

[poetry]: https://python-poetry.org/
[postgres]:https://www.postgresql.org/
[docker]:https://www.docker.com/
[sqlite]:https://www.sqlite.org/
[repo]:https://github.com/seapagan/fastapi_async_sqlalchemy2_example
