# lmrex/middleware/auth_logic.py

import reflex as rx
import reflex_local_auth


class ProtectedState(reflex_local_auth.LocalAuthState):
    data: str

    def on_load(self):
        if not self.is_authenticated:
            return reflex_local_auth.LoginState.redir
        self.data = f"This is truly private data for {self.authenticated_user.username}"

    def do_logout(self):
        self.data = ""
        return reflex_local_auth.LocalAuthState.do_logout


# @rx.page(on_load=ProtectedState.on_load)
@reflex_local_auth.require_login
def protected_page():
    @rx.page()
    @reflex_local_auth.require_login
    def protected_page():
        return rx.heading("Welcome, authenticated user!")
        return rx.heading(ProtectedState.data)
