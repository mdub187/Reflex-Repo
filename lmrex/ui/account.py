import reflex as rx
from lmrex.state.state import AuthState
from lmrex.models.user_model import User
from ..template import template


def account() -> rx.Component:
    return rx.vstack(
        template(child=rx.text("Account"), args={}, key="account"),
        rx.cond(
            AuthState.authenticated_user,
            rx.text("Hello, ", AuthState.auth_token),
            rx.link("Log in", href="/login"),
        ),
    )
