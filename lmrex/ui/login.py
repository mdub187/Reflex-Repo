# lmrex/ui/login.py
"""
Login and Registration UI using reflex-local-auth built-in pages
"""

import reflex as rx
import reflex_local_auth.pages as auth_pages
from lmrex.state.auth_state import AuthState
from ..components import user_login

def login() -> rx.Component:
    """
    Login page using reflex-local-auth's built-in pages
    Combines login and registration in tabs with status indicator
    """

    return rx.box(
        rx.vstack(
            rx.heading("Login / Register", size="8", margin_bottom="2rem"),

            # Tabs for Login and Register
            rx.tabs.root(
                rx.tabs.list(
                    rx.tabs.trigger("Login", value="login"),
                    rx.tabs.trigger("Register", value="register"),
                ),

                # Login Tab - Use built-in login page
                rx.tabs.content(
                    rx.card(
                        rx.dialog.trigger("Login",
                            rx.button("Login",
                            rx.dialog.content(user_login.user_login()),
                            # user_login.user_login(),
                        padding="2rem",
                        max_width="400px",

                    value="login",
                ),
                ),
                ),
                # Register Tab - Use built-in register page
                rx.tabs.content(
                    rx.card(
                        auth_pages.register_page(),
                        padding="2rem",
                        max_width="400px",
                    ),
                    value="register",
                ),

                default_value="login",
            ),
            # Status Card - Shows if logged in
            rx.cond(
                AuthState.is_logged_in,
                rx.card(
                    rx.vstack(
                        rx.heading("You're Logged In!", size="4"),
                        rx.badge(
                            rx.icon("check-circle"),
                            f" {AuthState.user_email}",
                            color_scheme="green",
                            size="3",
                        ),
                        rx.hstack(
                            rx.button(
                                rx.icon("user", size=16),
                                "Go to Account",
                                on_click=rx.redirect("/Account"),
                                variant="soft",
                                color_scheme="blue",
                            ),
                            rx.button(
                                rx.icon("log-out", size=16),
                                "Logout",
                                on_click=AuthState.logout_and_redirect,
                                variant="soft",
                                color_scheme="red",
                            ),
                            spacing="2",
                        ),
                        spacing="3",
                        align="center",
                    ),
                    padding="2rem",
                    max_width="400px",
                    margin_top="2rem",
                ),
            ),
),
            # Info Card
            rx.card(
                rx.vstack(
                    rx.heading("How It Works", size="4"),
                    rx.text("Create an account or login to access protected pages", size="2"),
                    rx.text("Your session is managed with secure tokens", size="2"),
                    rx.text("Passwords are hashed with bcrypt", size="2"),
                    spacing="2",
                ),
                padding="1.5rem",
                max_width="400px",
                margin_top="1rem",
            ),

            spacing="4",
            align="center",
            justify="center",
            min_height="80vh",
            padding="2rem",
        ),
        width="100%",
    )
