"""Set up some schemas for the database."""
from pydantic import BaseModel


class UserResponseModel(BaseModel):
    """Response model for the User model."""

    # id: int
    name: str
    email: str
