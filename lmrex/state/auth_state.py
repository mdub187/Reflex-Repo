# lmrex/state/auth_state.py
"""
Authentication State Management using reflex-local-auth
Provides secure token-based authentication with session management
"""

import reflex as rx
import reflex_local_auth
from typing import Optional, List


class AuthState(reflex_local_auth.LocalAuthState):
    """
    Main authentication state extending reflex-local-auth.LocalAuthState
    Provides token-based authentication with secure session management
    """

    # Override to customize behavior
    def on_load(self):
        """Called when any page loads - checks authentication status"""
        # This allows access to authenticated_user and session info
        pass

    @rx.var
    def user_email(self) -> str:
        """Get the authenticated user's email/username"""
        if self.authenticated_user and self.authenticated_user.username:
            return str(self.authenticated_user.username)
        return ""

    @rx.var
    def is_logged_in(self) -> bool:
        """Check if user is currently logged in"""
        return self.is_authenticated

    @rx.var
    def user_info(self) -> dict:
        """Get user information as a dictionary"""
        if self.authenticated_user:
            return {
                "username": self.authenticated_user.username,
                "id": self.authenticated_user.id,
                "enabled": self.authenticated_user.enabled,
            }
        return {}

    @rx.event
    def logout_and_redirect(self):
        """Logout and redirect to home page"""
        self.do_logout()
        return rx.redirect("/Home")

    @rx.event
    def check_login_redirect(self):
        """Check if logged in and redirect to account page"""
        if self.is_authenticated:
            return rx.redirect("/Account")
        return rx.window_alert("Please log in first")


class ProtectedState(AuthState):
    """
    State for protected pages that require authentication
    Automatically redirects to login if not authenticated
    """

    protected_data: str = ""

    def on_load(self):
        """Check authentication on protected page load"""
        if not self.is_authenticated:
            # Redirect to login page if not authenticated
            return reflex_local_auth.LoginState.redir
        
        # Load protected data for authenticated users
        self.protected_data = f"Welcome {self.authenticated_user.username}! This is your protected content."

    @rx.event
    def load_user_data(self):
        """Load user-specific data"""
        if self.is_authenticated:
            self.protected_data = f"User data for {self.authenticated_user.username}"
        else:
            self.protected_data = ""