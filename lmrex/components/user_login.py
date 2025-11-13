# ./lmrex/components/login_logic.py
import reflex as rx

from lmrex.state.auth_state import AuthState  # Import your existing state logic


def user_login() -> rx.Component:
    return rx.vstack(
        rx.heading("Login"),
        rx.input(
            placeholder="Username",
            on_change=AuthState.set_username,
            value=AuthState.username,
        ),
        rx.input(
            placeholder="Password",
            type="password",
            on_change=AuthState.set_password,
            value=AuthState.password,
        ),
        rx.button("Login", on_click=AuthState.handle_login_success),
        spacing="4",
    )
