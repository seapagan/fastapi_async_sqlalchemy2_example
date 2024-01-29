"""Define Models used in this example."""
from db import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class User(Base):
    """Create a test table."""

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    email: Mapped[str] = mapped_column(String(120), unique=True, index=True)

    def __repr__(self) -> str:
        """Define the model representation."""
        return f'User({self.id}, "{self.name}")'
