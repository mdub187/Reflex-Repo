import reflex as rx

from ..components.footer import footer
from ..state.auth_state import AuthState

def login() -> rx.State:
    """Login page with simulated login buttons and proper redirects."""

    # Helper functions
    def login_and_redirect(token: str):
        # AuthState.handle_login_success
        # Redirect after successful login
        return rx.State("/protected/account")

    def logout_and_redirect():
        AuthState.clear_auth_token
        return rx.State("/")  # Redirect to home after logout

    # return rx.box(
    #     rx.vstack(
    #         rx.heading("Login / Demo", size="6"),
    #         rx.text(
    #             "This page simulates a login flow for local development. "
    #             "Click a button below to store a demo token and set the authenticated user state."
    #         ),
    #         rx.hstack(
    #             rx.button(
    #                 # "Simulate admin token",
    #                 # on_click=lambda: login_and_redirect("demo-admin-token"),
    #                 # style={"background_color": "#2563eb", "color": "white"},
    #             ),
    #             rx.button(
    #                 "Logout",
    #                 on_click=logout_and_redirect,
    #                 style={"background_color": "#ef4444", "color": "white"},
    #             ),
    #             spacing="4",
    #         ),
    #         rx.text(
    #             "After a successful login you'll be redirected to the protected secret page."
    #         ),
    #         spacing="6",
    #         justify="center",
    #         align="center",
    #         min_height="60vh",
    #     ),
    #     footer(),
    #     style={"padding": "18px"},
    # )

# def login() -> rx.Component:
#     """Alias for compatibility with modules that expect a `login` function"""
#     return rx.State()
