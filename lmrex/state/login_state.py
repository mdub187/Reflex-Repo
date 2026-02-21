import reflex as rx
from lmrex.state.auth_state import AuthState


class LoginState(rx.State):
    """Minimal login state that provides a boolean for conditional rendering"""

    @rx.var
    def is_logged_in(self) -> bool:
        rx.button(rx.link("Account", "/account")),
        """Return True if user is logged in, False otherwise"""
        # return AuthState.is_logged_in
