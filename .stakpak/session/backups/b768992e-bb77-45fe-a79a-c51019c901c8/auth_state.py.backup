# lmrex/components/auth_state.py

import typing as t

import reflex as rx


class AuthState(rx.State):
    _auth_token: t.Optional[str] = None
    authenticated_user: t.Optional[dict] = None

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
    def handle_login_success(self, token: str, redirect: bool = True):
        self.auth_token = token
        self.authenticated_user = self._user_from_token(token)
        print(f"[AuthState] Login success for {self.authenticated_user['name']}")
        if redirect:
            return rx.redirect("login/protected/")

    @rx.event
    def clear_auth_token(self):
        print("[AuthState] Clearing auth token and authenticated user")
        self.auth_token = None
        self.authenticated_user = None


@rx.event
def set_user_email(self, email: str):
    if self.authenticated_user:
        print(f"[AuthState] Updating authenticated user email to: {email}")
        self.authenticated_user["email"] = email
    else:
        print("[AuthState] No authenticated user to update")

    # @rx.event
    # def fetch_protected_data(self):
    #     if not self._auth_token:
    #         print("No token found — cannot fetch data")
    #         return
    #     headers = {"Authorization": f"Bearer {self._auth_token}"}
    #     resp = requests.get("https://api.yourservice.com/data", headers=headers)

    if resp.ok:
        print("Fetched data:", resp.json())
    elif resp.status_code == 401:
        print("Auth failed")
    else:
        print("Bad request")


@rx.var
def get_roles(self) -> t.List[str]:
    return (
        list(self.authenticated_user.get("roles", []))
        if self.authenticated_user
        else []
    )

    @rx.event
    def handle_login_success(self, token: str):
        self._auth_token = token
        self.authenticated_user = self._user_from_token(token)
        return rx.redirect("/protected")

    @rx.event
    def fetch_user_data(self):
        if not self._auth_token:
            print("Not authenticated")
            return

        headers = {"Authorization": f"Bearer {self._auth_token}"}
        r = requests.get("https://api.yourservice.com/me", headers=headers)
        print(r.json())
