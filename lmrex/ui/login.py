# lmrex/ui/login.py

from ..components.footer import footer
from ..imports import rx
from ..state.auth_state import AuthState


def user_login() -> rx.Component:
    """Login page with simulated login buttons and proper redirects."""

    # Helper functions
    def login_and_redirect(token: str):
        AuthState.handle_login_success(token)
        return rx.redirect("/protected/secret")  # Redirect after successful login

    def logout_and_redirect():
        # AuthState._auth_token()
        return rx.redirect("/")  # Redirect to home after logout

    return rx.box(
        rx.vstack(
            rx.heading("Login / Demo", size="6"),
            rx.text(
                "This page simulates a login flow for local development. "
                "Click a button below to store a demo token and set the authenticated user state."
            ),
            rx.hstack(
                rx.button(
                    "Simulate login",
                    on_click=lambda: AuthState.handle_login_success("demo-token"),
                ),
                rx.button(
                    "Simulate admin token",
                    on_click=lambda: login_and_redirect("demo-admin-token"),
                    style={"background_color": "#2563eb", "color": "white"},
                ),
                rx.button(
                    "Logout",
                    on_click=logout_and_redirect,
                    style={"background_color": "#ef4444", "color": "white"},
                ),
                spacing="4",
            ),
            rx.text(
                "After a successful login you'll be redirected to the protected secret page."
            ),
            spacing="6",
            justify="center",
            align="center",
            min_height="60vh",
        ),
        footer(),
        style={"padding": "18px"},
    )


def login() -> rx.Component:
    """Alias for compatibility with modules that expect a `login` function"""
    return user_login()
