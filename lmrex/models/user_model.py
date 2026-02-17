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


# LocalUser and LocalAuthSession are provided by reflex_local_auth
# Do not redefine them here to avoid conflicts
# Import them with: from reflex_local_auth.local_auth import LocalUser, LocalAuthSession
