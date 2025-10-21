import reflex as rx
from ..state.state import AuthState
from ..components.navbar import navbar
from ..components.footer import footer
from ..components.color_mode import color_mode


def user_login() -> rx.Component:
    """
    Combined login/demo page used for local development.

    - "Simulate login" stores a demo token and calls `AuthState.handle_login_success`.
    - "Simulate admin token" stores an admin demo token.
    - "Logout" clears the stored token.
    """
    return rx.box(
        navbar(),
        rx.vstack(
            rx.heading("Login / Demo", size="6"),
            rx.text(
                "This page simulates a login flow for local development. "
                "Click a button below to store a demo token and set the authenticated user state."
            ),
            rx.hstack(
                rx.button(
                    "Simulate login",
                    on_click=lambda: AuthState.handle_login_success("demo-token"),
                    style={"background_color": "#10b981", "color": "white"},
                ),
                rx.button(
                    "Simulate admin token",
                    on_click=lambda: AuthState.handle_login_success("demo-admin-token"),
                    style={"background_color": "#2563eb", "color": "white"},
                ),
                rx.button(
                    "Logout",
                    on_click=lambda: AuthState.clear_auth_token(),
                    style={"background_color": "#ef4444", "color": "white"},
                ),
                spacing="4",
            ),
            rx.text(
                "After a successful simulated login you'll be redirected (if the handler returns a redirect). "
                "You can then visit the protected secret page."
            ),
            spacing="6",
            align="center",
            justify="center",
            min_height="60vh",
        ),
        footer(),
        color_mode(),
        style={"padding": "18px"},
    )


# Alias for compatibility with modules that expect a `login` function
def login() -> rx.Component:
    return user_login()


def secret() -> rx.Component:
    """
    Protected UI that displays secret content only when the user is authenticated.

    This is client-side gating for demo purposes. For real applications,
    validate tokens on the server before returning sensitive data.
    """
    return rx.box(
        navbar(),
        rx.vstack(
            rx.cond(
                AuthState.authenticated_user,
                rx.vstack(
                    rx.heading("Secret Area", size="6"),
                    rx.text(
                        "🎉 Congratulations — you have access to this protected page."
                    ),
                    rx.text(
                        "This content is gated by AuthState.authenticated_user. "
                        "For real applications, protect sensitive data on the server too."
                    ),
                    rx.cond(
                        AuthState.authenticated_user,
                        rx.vstack(
                            rx.text("Account info:"),
                            rx.text(AuthState.authenticated_user.email),
                        ),
                        rx.fragment(),
                    ),
                    spacing="4",
                    align="center",
                ),
                rx.vstack(
                    rx.heading("Protected", size="6"),
                    rx.text("You must be logged in to view this page."),
                    rx.link("Go to login demo", href="/login"),
                    spacing="3",
                    align="center",
                ),
            ),
            min_height="60vh",
            align="center",
            justify="center",
            spacing="6",
        ),
        # footer(),
        style={"padding": "18px"},
    )


__all__ = ["user_login", "login", "secret"]
