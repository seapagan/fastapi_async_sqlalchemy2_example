# Introduction

This section will attempt to explain the code in this repository. It is not
meant to be a tutorial on how to use FastAPI or SQLAlchemy, but rather an
explanation of how to get the two to work together **Asynchronously**.

## Caveats

This is a very simple example of a REST API. It is not meant to be used in
production, it is meant to be a simple example of how to use FastAPI and
SQLAlchemy together **Asynchronously**. As such there are some things that you
would
not do in a production environment, such as:

- Using SQLite as the database
- Manual database migrations, instead of using a tool like Alembic
- No validation of the data being sent to the API
- No check for duplicate email addresses
- The code layout is not optimal. The relevant files are all in the root
  directory, instead of being in a `src` directory or similar, and the routes
  would be better in a separate file.

The above is not an exhaustive list!

## Relevant Files

- `main.py` - The main file that runs the program and contains the routes
- `db.py` - This file contains the database connection and functions
- `models.py` - This file contains the database models
- `schema.py` - This defines the Pydantic schemas for the models, used for
  validation and serialization.
