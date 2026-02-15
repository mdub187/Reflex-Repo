# models/user_model.py

from datetime import datetime
from typing import Optional

import reflex as rx
from sqlmodel import Field, SQLModel


class Admin(rx.Model, table=True, extend_existing=True):
    """Admin user model - DO NOT use hardcoded credentials in production"""
    name: str = ""
    email: str = ""
    password_hash: str = ""  # Store hashed passwords only


class NewUser(rx.Model, extend_existing=True):
    """New user registration model"""
    name: str = ""
    email: str = ""
    password: str = ""  # Will be hashed before storage


class UserGallery(rx.Model, extend_existing=True):
    """User gallery items"""
    title: str = ""
    media: str = ""
    creator: str = ""


# class LocalUser(SQLModel, table=True, extend_existing=True):
#     """Model for local users."""
#     id: Optional[int] = Field(default=None, primary_key=True)
#     username: str
#     password_hash: str
#     enabled: bool = True


# class LocalAuthSession(SQLModel, table=True, extend_existing=True):
#     """Model for local authentication sessions."""
#     id: Optional[int] = Field(default=None, primary_key=True)
#     user_id: int = Field(foreign_key="localuser.id")
#     session_id: str
#     expiration: datetime
