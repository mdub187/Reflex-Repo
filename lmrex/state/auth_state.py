# lmrex/state/auth_state.py

import typing as t

import reflex as rx

from lmrex.middleware import auth_logic
from lmrex.routes import routes
from lmrex.ui.account import account_page


class AuthState(rx.State):
    """Authentication state management"""

    _auth_token: t.Optional[str] = None
    authenticated_user: t.Optional[dict] = None

    @rx.var
    def is_authenticated(self) -> bool:
        """Check if user is authenticated"""
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
        def login_and_redirect(token: str):
           AuthState.handle_login_success(token)
           # Redirect after successful login
           rx.redirect("account/")
           return login_and_redirect
           def user_login() -> rx.Component:
               """Login page with simulated login buttons and proper redirects."""

               # Helper functions


           def logout_and_redirect():
                   # AuthState._auth_token()
               return rx.redirect("/")  # Redirect to home after logout
           def login(login_and_redirect) -> rx.Component:
                   """Alias for compatibility with modules that expect a `login` function"""
           return user_login()


        token = f"{username}:{password}"
        self._auth_token = token
        self.authenticated_user = self._user_from_token(token)
        print(f"[AuthState] Login success for {self.authenticated_user['name']}")
        # Redirect to protected page after successful login
        # return rx.redirect(token)
        # rx.redirect(token)
        # rx.redirect("/protected/account/" + self.authenticated_user["email"])

    @rx.event
    def set_user_email(self, email: str):
        """Update authenticated user's email"""
        if self.authenticated_user:
            print(f"[AuthState] Updating authenticated user email to: {email}")
            self.authenticated_user["email"] = email
        else:
            print("[AuthState] No authenticated user to update")

    # @rx.event
    # def clear_auth_token(self):
    #     """Clear authentication state and log out"""
    #     print("[AuthState] Clearing auth token and authenticated user")
    #     self._auth_token = None
    #     self.authenticated_user = None
    #     return rx.redirect("/")
    #     auth_logic()

    @rx.event
    def do_logout(self):
        """Logout handler"""
        return self.clear_auth_token()
