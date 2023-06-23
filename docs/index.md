# Async SQLAlchemy 2 with FastAPI

## Introduction

I've been using [FastAPI][fastapi]{:target="_blank"} and
[SQLAlchemy][sqla]{:target="_blank"} combined with
[encode/databases][databases]{:target="_blank"} for a while now.

The `databases` package is a great wrapper around `SQLAlchemy` that allows you
to use async/await with SQLAlchemy.

However, this does not seem be be actively maintained anymore. So I decided to
give the new [Async SQLAlchemy][async-sqla]{:target="_blank"} a try instead.

This repository contains a very simple example how to use FastAPI with Async
SQLAlchemy 2.0, in `ORM` mode. I'll probably add an example for `Core` mode
also.

[fastapi]:https://fastapi.tiangolo.com/
[sqla]: https://www.sqlalchemy.org/
[databases]:https://www.encode.io/databases/
[async-sqla]:https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html
