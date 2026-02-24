# lmrex/ui/account.py
"""
Account page - Protected route that requires authentication
Displays user information and account management options
"""

import reflex as rx
from lmrex.state.auth_state import ProtectedState


def account_page() -> rx.Component:
    """
    Protected account page that shows user information
    Requires authentication - redirects to login if not authenticated
    """

    return rx.box(
        rx.vstack(
            # Header Section
            rx.hstack(
                rx.heading(
                    "My Account",
                    size="8",
                    weight="bold",
                ),
                rx.badge(
                    rx.icon("shield-check", size=18),
                    "Protected Page",
                    color_scheme="green",
                    size="2",
                ),
                spacing="3",
                align="center",
                margin_bottom="2rem",
            ),

            # User Info Card
            rx.card(
                rx.vstack(
                    rx.heading("User Information", size="5", margin_bottom="1rem"),

                    # Username
                    rx.hstack(
                        rx.text("Username:", weight="bold", size="3"),
                        rx.text(ProtectedState.user_email, size="3"),
                        spacing="2",
                        width="100%",
                    ),

                    # User ID
                    rx.hstack(
                        rx.text("User ID:", weight="bold", size="3"),
                        rx.text(ProtectedState.user_info.get("id", "N/A"), size="3"),
                        spacing="2",
                        width="100%",
                    ),

                    # Account Status
                    rx.hstack(
                        rx.text("Status:", weight="bold", size="3"),
                        rx.cond(
                            ProtectedState.user_info.get("enabled", False),
                            rx.badge("Active", color_scheme="green"),
                            rx.badge("Inactive", color_scheme="red"),
                        ),
                        spacing="2",
                        width="100%",
                    ),

                    # Authentication Status
                    rx.hstack(
                        rx.text("Authenticated:", weight="bold", size="3"),
                        rx.cond(
                            ProtectedState.is_authenticated,
                            rx.badge(
                                rx.icon("check", size=14),
                                "Yes",
                                color_scheme="green",
                            ),
                            rx.badge(
                                rx.icon("x", size=14),
                                "No",
                                color_scheme="red",
                            ),
                        ),
                        spacing="2",
                        width="100%",
                    ),

                    spacing="3",
                    padding="2rem",
                ),
                max_width="600px",
                width="100%",
            ),

            # Protected Content Card
            rx.card(
                rx.vstack(
                    rx.heading("Protected Content", size="5", margin_bottom="1rem"),
                    rx.text(
                        ProtectedState.protected_data,
                        size="3",
                        color="gray",
                    ),
                    rx.button(
                        rx.icon("refresh-cw", size=16),
                        "Reload Data",
                        on_click=ProtectedState.load_user_data,
                        variant="soft",
                        margin_top="1rem",
                    ),
                    spacing="3",
                    padding="2rem",
                ),
                max_width="600px",
                width="100%",
                margin_top="1rem",
            ),

            # Account Actions Card
            rx.card(
                rx.vstack(
                    rx.heading("Account Actions", size="5", margin_bottom="1rem"),

                    rx.vstack(
                        rx.button(
                            rx.icon("home", size=16),
                            "Go to Home",
                            on_click=rx.redirect("/Home"),
                            variant="soft",
                            color_scheme="blue",
                            width="100%",
                        ),
                        rx.button(
                            rx.icon("image", size=16),
                            "View Gallery",
                            on_click=rx.redirect("/Account/Gallery/"),
                            variant="soft",
                            color_scheme="purple",
                            width="100%",
                        ),
                        rx.button(
                            rx.icon("log-out", size=16),
                            "Logout",
                            on_click=ProtectedState.logout_and_redirect,
                            variant="soft",
                            color_scheme="red",
                            width="100%",
                        ),
                        spacing="2",
                        width="100%",
                    ),

                    spacing="3",
                    padding="2rem",
                ),
                max_width="600px",
                width="100%",
                margin_top="1rem",
            ),

            # Security Info
            rx.card(
                rx.vstack(
                    rx.heading("Security", size="4", margin_bottom="0.5rem"),
                    rx.text(
                        "Your session is secured with token-based authentication.",
                        size="2",
                        color="gray",
                    ),
                    rx.text(
                        "Sessions expire automatically for security.",
                        size="2",
                        color="gray",
                    ),
                    rx.text(
                        "All passwords are hashed and never stored in plain text.",
                        size="2",
                        color="gray",
                    ),
                    spacing="2",
                    padding="1.5rem",
                ),
                max_width="600px",
                width="100%",
                margin_top="1rem",
            ),

            spacing="4",
            align="center",
            justify="start",
            min_height="80vh",
            padding="2rem",
            on_mount=ProtectedState.on_load,
        ),
        width="100%",
    )
