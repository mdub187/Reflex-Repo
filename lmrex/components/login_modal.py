# lmrex/components/login_modal.py
"""
Login Modal Component - Integrated with reflex-local-auth
Provides a modal dialog for login and registration
"""

import reflex as rx
import reflex_local_auth
from lmrex.state.auth_state import AuthState


class LoginModalState(rx.State):
    """State management for the login modal"""

    show_modal: bool = False
    active_tab: str = "login"  # "login" or "register"

    @rx.event
    def toggle_modal(self):
        """Toggle modal visibility"""
        self.show_modal = not self.show_modal

    @rx.event
    def open_modal(self, tab: str = "login"):
        """Open modal with specific tab"""
        self.show_modal = True
        self.active_tab = tab

    @rx.event
    def close_modal(self):
        """Close the modal"""
        self.show_modal = False

    @rx.event
    def switch_to_register(self):
        """Switch to registration tab"""
        self.active_tab = "register"

    @rx.event
    def switch_to_login(self):
        """Switch to login tab"""
        self.active_tab = "login"


def login_modal() -> rx.Component:
    """
    Login modal component with authentication integration.
    Provides both login and registration forms in a dialog.
    """

    return rx.dialog.root(
        # Trigger button
        rx.dialog.trigger(
            rx.button(
                rx.icon("log-in", size=16),
                "Login",
                variant="soft",
                on_click=LoginModalState.open_modal("login"),
            ),
        ),

        # Modal content
        rx.dialog.content(
            rx.vstack(
                # Header
                rx.heading(
                    rx.cond(
                        LoginModalState.active_tab == "login",
                        "Welcome Back",
                        "Create Account",
                    ),
                    size="6",
                ),

                # Tab selector
                rx.tabs.root(
                    rx.tabs.list(
                        rx.tabs.trigger(
                            "Login",
                            value="login",
                            on_click=LoginModalState.switch_to_login,
                        ),
                        rx.tabs.trigger(
                            "Register",
                            value="register",
                            on_click=LoginModalState.switch_to_register,
                        ),
                    ),

                    # Login tab content
                    rx.tabs.content(
                        rx.form(
                            rx.vstack(
                                rx.input(
                                    placeholder="Username",
                                    name="username",
                                    required=True,
                                    size="3",
                                ),
                                rx.input(
                                    placeholder="Password",
                                    name="password",
                                    type="password",
                                    required=True,
                                    size="3",
                                ),
                                rx.button(
                                    "Sign In",
                                    type="submit",
                                    size="3",
                                    width="100%",
                                ),
                                spacing="3",
                                width="100%",
                            ),
                            on_submit=reflex_local_auth.LoginState.on_submit,
                            width="100%",
                        ),
                        value="login",
                    ),

                    # Register tab content
                    rx.tabs.content(
                        rx.form(
                            rx.vstack(
                                rx.input(
                                    placeholder="Username",
                                    name="username",
                                    required=True,
                                    size="3",
                                ),
                                rx.input(
                                    placeholder="Password",
                                    name="password",
                                    type="password",
                                    required=True,
                                    size="3",
                                ),
                                rx.input(
                                    placeholder="Confirm Password",
                                    name="confirm_password",
                                    type="password",
                                    required=True,
                                    size="3",
                                ),
                                rx.button(
                                    "Create Account",
                                    type="submit",
                                    size="3",
                                    width="100%",
                                ),
                                spacing="3",
                                width="100%",
                            ),
                            # on_submit=reflex_local_auth.RegistrationState,
                            width="100%"),

                        value="register",

                    ),
                    value=LoginModalState.active_tab,
                    width="100%",
                ),

                # Status message
                rx.cond(
                    AuthState.is_logged_in,
                    rx.hstack(
                        rx.badge(
                            rx.icon("check-circle", size=14),
                            f"Logged in as {AuthState.user_email}",
                            color_scheme="green",
                        ),
                        rx.button(
                            "Go to Account",
                            on_click=[
                                rx.redirect("/Account"),
                                LoginModalState.close_modal,
                            ],
                            size="2",
                            variant="soft",
                        ),
                        spacing="2",
                        width="100%",
                        justify="between",
                    ),
                ),

                # Close button
                rx.dialog.close(
                    rx.button(
                        "Close",
                        variant="soft",
                        color_scheme="gray",
                        on_click=LoginModalState.close_modal,
                    ),
                ),

                spacing="4",
                width="100%",
                align="stretch",
            ),
            max_width="400px",
        ),

        open=LoginModalState.show_modal,
    )


def login_button_trigger() -> rx.Component:
    """
    Standalone login button that opens the modal.
    Use this anywhere you want a login button.
    """
    return rx.button(
        rx.icon("log-in", size=16),
        "Login",
        on_click=LoginModalState.open_modal("login"),
        variant="soft",
    )


def register_button_trigger() -> rx.Component:
    """
    Standalone register button that opens the modal.
    Use this anywhere you want a register button.
    """
    return rx.button(
        rx.icon("user-plus", size=16),
        "Sign Up",
        on_click=LoginModalState.open_modal("register"),
        variant="soft",
        color_scheme="blue",
    )


def user_menu() -> rx.Component:
    """
    User menu component showing login status and account options.
    Shows login button if not authenticated, user menu if authenticated.
    """
    return rx.cond(
        AuthState.is_logged_in,
        # Logged in - show user menu
        rx.menu.root(
            rx.menu.trigger(
                rx.button(
                    rx.icon("user", size=16),
                    AuthState.user_email,
                    variant="soft",
                    color_scheme="green",
                ),
            ),
            rx.menu.content(
                rx.menu.item(
                    rx.icon("user", size=14),
                    "Account",
                    on_click=rx.redirect("/Account"),
                ),
                rx.menu.separator(),
                rx.menu.item(
                    rx.icon("log-out", size=14),
                    "Logout",
                    on_click=AuthState.logout_and_redirect,
                    color_scheme="red",
                ),
            ),
        ),
        # Not logged in - show login button
        login_button_trigger(),
    )
