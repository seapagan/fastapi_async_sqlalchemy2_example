"""Set up some schemas for the database."""

from pydantic import BaseModel


class UserResponseModel(BaseModel):
    """Response model for the User model."""

    name: str
    email: str
