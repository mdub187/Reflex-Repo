# ./lmrex/components/user_login.py
import reflex as rx


from ..state.auth_state import AuthState


class LoginState(rx.State):
    """State for login form"""
    username: str = ""
    password: str = ""

    def set_username(self, value: str):
        """Set username value"""
        self.username = value

    def set_password(self, value: str):
        """Set password value"""
        self.password = value


def user_login() -> rx.Component:
    """Login dialog component"""
    return rx.dialog.root(
        rx.dialog.trigger(rx.button("Login")),
        rx.dialog.title(
        rx.dialog.content(
            rx.heading("Sign-in or Register", size="6"),
            rx.text("Enter your credentials below."),
            rx.form(
                rx.input(
                    placeholder="Username",
                    on_change=LoginState.set_username,
                    value=LoginState.username,
                ),
            ),
                rx.input(
                    placeholder="Password",
                    type="password",
                    on_change=LoginState.set_password,
                    value=LoginState.password,
                ),
            ),
            rx.dialog.close(
                rx.button(
                    "Submit",
                    on_click=AuthState.handle_login_success(
                        LoginState.username, LoginState.password
                    )
                )
            ),
        ),
            rx.spacer(column=1),
            rx.dialog.trigger(rx.button("Create Account")),
    )
