"""Define Models used in this example."""
from sqlalchemy import Column, Integer, String

from db import Base


class User(Base):
    """Create a test table."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
