# Simple example how to use FastAPI with Async SQLAlchemy 2.0

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

```bash
poetry install
```

Then switch to the virtual environment:

```bash
poetry shell
```

## Usage

Run the server using `Uvicorn`:

```bash
uvicorn main:app --reload
```

Then open your browser at [http://localhost:8000](http://localhost:8000).

There is only one endpoint available: `/users`. It returns a list of all users
for a `GET` request and creates a new user for a `POST` request.

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
