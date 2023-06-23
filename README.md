# Using FastAPI with Async SQLAlchemy 2.0 <!-- omit from toc -->

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
  - [Local Postgres server using Docker](#local-postgres-server-using-docker)
  - [Use SQLite instead of PostgreSQL](#use-sqlite-instead-of-postgresql)
- [License](#license)

## Introduction

I've been using [FastAPI](https://fastapi.tiangolo.com/) and
[SQLAlchemy](https://www.sqlalchemy.org/) combined with
[encode/databases](https://www.encode.io/databases/) for a while now.

The `databases` package is a great wrapper around `SQLAlchemy` that allows you
to use async/await with SQLAlchemy.

However, this does not seem be be actively maintained anymore. So I decided to
give the new [Async
SQLAlchemy](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html) a try
instead.

This repository contains a very simple example how to use FastAPI with Async
SQLAlchemy 2.0.

## Installation

Clone the repository and install the dependencies. This project uses
[Poetry](https://python-poetry.org/) for dependency management which should be
installed on your system first.

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

> You can also run the server by just executing the `main.py` file:
>
> ```console
> python main.py
> ```

Then open your browser at [http://localhost:8000](http://localhost:8000).

There is only one endpoint available: `/users`. It returns a list of all users
for a `GET` request and creates a new user for a `POST` request.

### Local Postgres server using Docker

This example uses [PostgreSQL](https://www.postgresql.org/) as the database. If
you dont have a local PostgreSQL database running, you can start one with
[Docker](https://www.docker.com) using the following command:

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

For testing purposes, you can also use SQLite instead of PostgreSQL. To do so,
open the [dp.py](db.py) file and comment out the PostgreSQL database in the
`DATABASE_URL` environment variable and uncomment the SQLite database.

```python
# DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost/postgres"
DATABASE_URL = "sqlite+aiosqlite:///./test.db"
```

## License

This project is licensed under the terms of the MIT license.

```pre
MIT License

Copyright (c) 2023 Grant Ramsay

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

```
