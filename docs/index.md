# Async SQLAlchemy 2 with FastAPI

## Introduction

This repository contains a very simple example how to use FastAPI with Async
SQLAlchemy 2.0, in `ORM` mode. I'll probably add an example for `Core` mode
also. No effort has been made to make this a production ready application, it's
just a simple demo since at the time of writing there were few clear examples of
how to do this.

Last update 29th January 2024, and tested to work with the following versions:

- Python 3.9+
- FastAPI 0.109.0
- SQLAlchemy  2.0.25

## Why use Raw SQLAlchemy?

I was using [FastAPI][fastapi]{:target="_blank"} and
[SQLAlchemy][sqla]{:target="_blank"} combined with
[encode/databases][databases]{:target="_blank"} for a while. This worked fine
originally but I felt I needed a bit more control over the database session
management.

!!! info
    The [databases][databases]{:target="_blank"} package is a great wrapper
    around `SQLAlchemy` that allows you to use async/await for database
    operations. It also has a nice way of managing the database session, which
    is why I used it originally.

However, this did not seem be be actively maintained at the time, so I decided
to give the newer [Async SQLAlchemy][async-sqla]{:target="_blank"} a try
instead.

This repository is the result of my exprimentation while converting my
[FastAPI-template][fastapi-template]{:target="_blank"} project to use `Async
SQLAlchemy` instead of `databases`.

[fastapi]: https://fastapi.tiangolo.com/
[sqla]: https://www.sqlalchemy.org/
[databases]: https://www.encode.io/databases/
[async-sqla]: https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html
[fastapi-template]: https://github.com/seapagan/fastapi-template
