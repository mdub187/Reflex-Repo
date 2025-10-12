# models/user_model.py

import reflex as rx

class User1(rx.Model, table=True, extend_existing=True):
    """The user model."""

    name: str = ""
    email: str = ""
    password: str = ""

class NewUser(rx.Model, extend_existing=True):
    name: str = ""
    email: str = ""
    passsword: str = ""

class Gallery(rx.Model, extend_existing=True):
    title: str = ""
    media: str = ""
    creator: str = ""
