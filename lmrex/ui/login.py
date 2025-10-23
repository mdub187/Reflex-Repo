import reflex as rx
from ..state.state import State
from ..components.footer import footer
from ..components.color_mode import color_mode


def user_login() -> rx.Component:
    print("Debug: user_login component is being rendered")
    return rx.box(
        rx.vstack(
<<<<<<< HEAD
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
            rx.alert_dialog.trigger(
                rx.box(
                    rx.hstack(
                    rx.heading("Debug Modal"),
                    size="3",
                    # rx.box("This is a simple modal for debugging."),
                        justify="center"
                    ),
                    rx.button("Close", on_click=State.toggle_modal),
            rx.alert_dialog.cancel(
                    rx.button(
                        "Cancel",
                        variant="soft",
                        color_scheme="gray",
                    )
                # is_open=True,  # Force modal to always render for debugging
                ), # Toggle modal visibility on close action
            spacing="5",
            justify="center",
            align="center",
            justify="center",
            min_height="60vh",
        ),
        footer(),
        color_mode(),
        style={"padding": "18px"},
    ),
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
=======
            rx.alert_dialog.root(
                rx.alert_dialog.content(
                rx.alert_dialog.trigger(
                    rx.box(
                        rx.hstack(
                            rx.heading("Debug Modal"),
                            size="3",
                            # rx.box("This is a simple modal for debugging."),
                            justify="center"
                        ),
                        rx.button("Close", on_click=State.toggle_modal),
                        rx.alert_dialog.cancel(
                            rx.button(
                                "Cancel",
                                variant="soft",
                            color_scheme="gray",
>>>>>>> parent of 4a4eed8 (cleaning up refactor, added filed to .gitignore, added authentication logic, the logic is sitll a work in progress and isnt yet working. encountered some roadblocks i did have some help for co pilot. i want to clean up and make sure it didnt overcomplicate things.)
                        ),
                    ),
                # is_open=True,  # Force modal to always render for debugging
                ), # Toggle modal visibility on close action
            ),
            ),
            spacing="5",
            justify="center",
            align="center",
            min_height="80vh",
            text_align="center",
        ),
        rx.container(
            footer(),
            color_mode(),
        ),
    )
)
