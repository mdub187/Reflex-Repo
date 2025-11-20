# lmrex/state/auth_state.py
# Reflex_pylot/lmrex/state/auth_state.py

import typing as t

import reflex as rx

from lmrex.middleware import auth_logic
from lmrex.routes import routes
from lmrex.ui.account import account_ui
from ..middleware.auth_logic import ProtectedState


class AuthState(rx.State):
    """
    Demo authentication state using serializable built-in types.

    Notes:
    - `authenticated_user` is stored as a plain dict (or None) to satisfy Reflex's
      requirement that state vars be serializable. Avoid storing custom classes
      or dataclass instances directly on State.
    - This is intentionally simple and client-only for local development/demo pages.
    - For production, replace with proper authentication flows (server-validated tokens,
      secure storage, refresh tokens, etc.).
    """

    # Stored auth token (demo only)
    auth_token: t.Optional[str] = None

    # The currently authenticated user (or None). Use a serializable dict.
    authenticated_user: t.Optional[dict] = None

    @rx.var
    def is_authenticated(self) -> bool:
        """Check if user is authenticated"""
        """Convenience var for checking authentication in UI code."""
        return self.authenticated_user is not None

    @rx.var
    def get_roles(self) -> t.List[str]:
        """Get user roles"""
        return (
            list(self.authenticated_user.get("roles", []))
            if self.authenticated_user
            else []
        )

    @staticmethod
    def _user_from_token(token: str) -> dict:
        """Mock user lookup from token - replace with real auth logic"""
        """
        Create a demo serializable user dict from a token string.

        Rules (demo):
        - If token contains 'admin' -> admin user
        - Otherwise -> demo user
        """
        if "admin" in (token or "").lower():
            return {
                "email": "admin@example.local",
                "name": "Admin",
                "roles": ["admin"],
            }
        return {"email": "demo@example.local", "name": "Demo User", "roles": ["user"]}

    @rx.event
    def handle_login_success(self, username: str, password: str):
        """Handle successful login with username and password"""
        # TODO: Replace with real authentication logic
        token = f"{username}:{password}"
        self._auth_token = token
        self.authenticated_user = self._user_from_token(token)
        print(f"[AuthState] Login success for {self.authenticated_user['name']}")
        # Redirect to protected page after successful login
        # return rx.redirect(token)
        # rx.redirect(token)
        rx.redirect("/protected/account/" + self.authenticated_user["email"])

    @rx.event
    def clear_auth_token(self) -> None:
        """Clear stored token and authenticated user (logout)."""
        print("[AuthState] Clearing auth token and authenticated user")
        self._auth_token = None
        self.authenticated_user = None
        auth_logic()

    @rx.event
    def do_logout(self):
        """Logout handler"""
        return self.clear_auth_token()

    @rx.event
    def set_user_email(self, email: str) -> None:
        """Utility to update the authenticated user's email (if present)."""
        if self.authenticated_user is not None:
            print(f"[AuthState] Updating authenticated user email to: {email}")
            # Mutate the dict in-place (still serializable)
            self.authenticated_user["email"] = email
        else:
            print("[AuthState] No authenticated user to update")


class State(rx.State):
    logged_in: bool = False
