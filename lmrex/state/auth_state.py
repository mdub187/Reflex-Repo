# Reflex_pylot/lmrex/state/auth_state.py

import typing as t

import reflex as rx


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
        """Convenience var for checking authentication in UI code."""
        return self.authenticated_user is not None

    @staticmethod
    def _user_from_token(token: str) -> dict:
        """
        Create a demo serializable user dict from a token string.

        Rules (demo):
        - If token contains 'admin' -> admin user
        - Otherwise -> demo user
        """
        if "admin" in (token or "").lower():
            return {
                "email": "admin@example.local",
                "name": "Admin User",
                "roles": ["admin"],
            }
        return {"email": "demo@example.local", "name": "Demo User", "roles": ["user"]}

    @rx.event
    def handle_login_success(self, token: str) -> None:
        """
        Handle a successful login by storing the token and setting the authenticated user.

        This is invoked by UI demo buttons to simulate successful logins.
        """
        print(f"[AuthState] Received login token: {token!r}")
        self.auth_token = token
        # Store a serializable dict representing the user
        self.authenticated_user = self._user_from_token(token)
        print(f"[AuthState] Authenticated user set: {self.authenticated_user}")
        rx.redirect("/account")

    @rx.event
    def clear_auth_token(self) -> None:
        """Clear stored token and authenticated user (logout)."""
        print("[AuthState] Clearing auth token and authenticated user")
        self.auth_token = None
        self.authenticated_user = None

    @rx.event
    def set_user_email(self, email: str) -> None:
        """Utility to update the authenticated user's email (if present)."""
        if self.authenticated_user is not None:
            print(f"[AuthState] Updating authenticated user email to: {email}")
            # Mutate the dict in-place (still serializable)
            self.authenticated_user["email"] = email
        else:
            print("[AuthState] No authenticated user to update")

    # Additional convenience helpers (demo)
    @rx.var
    def get_roles(self) -> t.List[str]:
        """Return roles for the current user (empty list if not authenticated)."""
        return (
            list(self.authenticated_user.get("roles", []))
            if self.authenticated_user
            else []
        )
