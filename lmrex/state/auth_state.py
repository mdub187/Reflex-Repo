# lmrex/state/auth_state.py

import typing as t

import reflex as rx


class AuthState(rx.State):
    _auth_token: t.Optional[str] = None
    authenticated_user: t.Optional[dict] = None
    is_add_media_modal_open: bool = False
    media_url: str = ""
    username: str = ""
    password: str = ""

    @rx.var
    def is_authenticated(self) -> bool:
        return self.authenticated_user is not None

    @staticmethod
    def _user_from_token(token: str) -> dict:
        if "admin" in (token or "").lower():
            return {
                "email": "admin@example.local",
                "name": "Admin User",
                "roles": ["admin"],
            }
        return {"email": "demo@example.local", "name": "Demo User", "roles": ["user"]}

    @rx.event
    def handle_login_success(self):
        # Extract the token from the event or use a default token
        token = "default_token"  # Replace with actual logic to get the token
        self._auth_token = token
        self.authenticated_user = self._user_from_token(token)
        print(f"[AuthState] Login success for {self.authenticated_user['name']}")
        return rx.redirect("/login/protected/")

    @rx.event
    def clear_auth_token(self):
        print("[AuthState] Clearing auth token and authenticated user")
        self._auth_token = None
        self.authenticated_user = None

    @rx.event
    def set_user_email(self, email: str):
        if self.authenticated_user:
            print(f"[AuthState] Updating authenticated user email to: {email}")
            self.authenticated_user["email"] = email
        else:
            print("[AuthState] No authenticated user to update")

    # @rx.event
    # def toggle_add_media_modal(self):
    # self.is_add_media_modal_open = not self.is_add_media_modal_open

    # @rx.event
    # def set_media_url(self, media_url: str):
    #     self.media_url = media_url

    # @rx.event
    # def handle_upload(self):
    #     # Handle the media upload logic here
    #     print(f"Media uploaded with URL: {self.media_url}")
    #     self.is_add_media_modal_open = False
    #     self.media_url = ""

    @rx.event
    def set_username(self, username: str):
        self.username = username

    @rx.event
    def set_password(self, password: str):
        self.password = password

    @rx.event
    def handle_login(self):
        # Handle the login logic here
        print(f"Username: {self.username}, Password: {self.password}")
        self.username = ""
        self.password = ""
