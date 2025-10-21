# lmrex/models/user_model.py
"""SQLModel-based user models.

Replaces previous usage of Reflex `rx.Model` with proper SQLModel classes so the
models can be persisted with the project's SQLModel / SQLAlchemy helpers.

Notes:
- `User` is a table model (SQLModel with table=True).
- `NewUser` is a simple data model used for creation flows (not persisted directly).
- `Gallery` is kept as a simple SQLModel (not a DB table by default) for reuse in the app.
- Add migrations (Alembic) for production; `SQLModel.metadata.create_all` is suitable
  for simple local development only.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Optional

from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    """Persistent user model stored in the database."""

    __tablename__ = "user"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(default="", index=False)
    email: str = Field(default="", index=True)
    password: str = Field(default="")  # store hashed password only
    token: str = Field(default="")  # store hashed token (not raw token)
    token_expires_at: Optional[datetime] = Field(default=None, nullable=True)

    @classmethod
    def from_dict(cls, data: dict) -> "User":
        """Create a User instance from a dictionary-like payload."""
        return cls(
            id=data.get("id"),
            name=data.get("name", "") or "",
            email=data.get("email", "") or "",
            password=data.get("password", "") or "",
            token=data.get("token", "") or "",
            token_expires_at=data.get("token_expires_at"),
        )


class NewUser(SQLModel):
    """Lightweight model used when creating a new user (no DB id)."""

    name: str = ""
    email: str = ""
    password: str = ""


class Gallery(SQLModel):
    """Simple gallery representation; not necessarily a DB table in this form."""

    title: str = ""
    media: List[str] = Field(default_factory=list)
    creator: str = ""
