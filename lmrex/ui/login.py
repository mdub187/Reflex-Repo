import reflex as rx
from ..state.auth_state import AuthState
from ..components.footer import footer
from ..components.color_mode import color_mode


def user_login() -> rx.Component:
    print("Debug: user_login component is being rendered")
    return rx.box(
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
            justify="center",
            align="center",
            min_height="60vh",
        ),
        footer(),
        # color_mode(),
        style={"padding": "18px"},
    )


def login() -> rx.Component:
    """Alias for compatibility with modules that expect a `login` function"""
    return user_login()


def secret() -> rx.Component:
    """
    Protected UI that displays secret content only when the user is authenticated.
    This is client-side gating for demo purposes. For real applications,
    validate tokens on the server before returning sensitive data.
    """
    return rx.box(
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
                            spacing="2",
                        ),
                    ),
                    spacing="4",
                ),
                rx.vstack(
                    rx.heading("Access Denied", size="6"),
                    rx.text("Please log in to view this content."),
                    spacing="4",
                ),
            ),
            spacing="5",
            justify="center",
            align="center",
            min_height="80vh",
            text_align="center",
        ),
        footer(),
        # color_mode(),
    )
