# lmrex/middleware/auth_logic.py
import reflex as rx
import reflex_local_auth
from lmrex.ui import account

class ProtectedState(reflex_local_auth.LocalAuthState):
    """State for protected pages using reflex-local-auth"""

    data: str = ""

    def on_load(self):
        """Check authentication on page load"""
        if not self.is_authenticated:
            return reflex_local_auth.LoginState.redir
        self.data = f"This is truly private data for {self.authenticated_user.username}"

    def do_logout(self):
        """Handle logout"""
        self.data = ""
        return reflex_local_auth.LocalAuthState.do_logout
