"""
State for the login form used by the login modal.

This state holds the username/password inputs, provides simple client-side
validation helpers, and exposes a `submit` event which delegates to the
auth state to perform login + redirect in the demo app.
"""
from __future__ import annotations

import reflex as rx
from lmrex.state.auth_state import AuthState


class LoginState(rx.State):
    """Login form state (username/password + validation)."""

    username: str = ""
    password: str = ""

    @rx.event
    def set_username(self, value: str):
        """Update the username field."""
        # Defensive: ensure a string is stored
        self.username = value or ""

    @rx.event
    def set_password(self, value: str):
        """Update the password field."""
        # Defensive: ensure a string is stored
        self.password = value or ""

    @rx.var
    def is_valid(self) -> bool:
        """Return True when the form is valid and ready for submit."""
        return bool(self.username.strip()) and len(self.password) >= 6

    @rx.var
    def username_missing(self) -> bool:
        """Helper var: True when username is empty (useful for inline messages)."""
        return not bool(self.username.strip())

    @rx.var
    def password_short(self) -> bool:
        """Helper var: True when password is too short (< 6 chars)."""
        return len(self.password) < 6

    @rx.event
    def submit(self):
        """
        Submit the login form.

        For this demo, we synthesize a token from username/password and call
        the `AuthState.handle_login_and_redirect` event to both sign the user
        in and redirect them to /account.
        """
        # Simple guard - don't submit if invalid
        if not self.is_valid:
            return None

        token = f"{self.username.strip()}:{self.password}"
        # This returns a redirect event that Reflex will use to navigate.
        # Suppress the static type checker complaint about EventNamespace being
        # non-callable when referenced on the class.
        return AuthState.handle_login_and_redirect(token)  # type: ignore[call-arg]