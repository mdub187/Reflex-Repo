# ./lmrex/components/navbar.py
import reflex as rx
from typing import Optional
from lmrex.state.auth_state import AuthState
from .login_modal import login_modal, login_button_trigger
from .icon import logo_icon, small_logo_icon

def navbar_link(text: str, url: Optional[str] = None, on_click=None) -> rx.Component:
    """Create a simple navbar link."""
    return rx.link(
        rx.text(text, size="4", weight="medium", display="contents"),
        href=url if url else "#",
        on_click=on_click,
        padding="10px",
        min_width="48px",
    )


def navbar() -> rx.Component:
    """
    Top navigation bar.

    - Shows logo + title on the left.
    - Shows navigation links and a conditional Login / Account control on the right.
    - Uses `login_button_trigger()` as the single trigger for the modal.
    - Mounts `login_modal()` once so programmatic opens (via LoginModalState events) work.
    """
    return rx.container(
        # Desktop header
        rx.box(
            rx.desktop_only(
                rx.hstack(
                    # Left: logo + title
                    rx.hstack(
                        logo_icon(),
                        rx.heading("We Gon", size="7", weight="bold"),
                    ),
                    # Right: nav links + auth control
                    rx.hstack(
                        navbar_link("Home", "/Home"),
                        navbar_link("About", "/About"),
                        navbar_link("Gallery", "/Gallery"),
                        navbar_link("Contact", "/Contact"),
                        # Show Account when logged in, otherwise show the login button trigger
                        rx.cond(
                            AuthState.is_logged_in,
                            navbar_link("Account", "/Account"),
                            login_button_trigger(),
                        ),
                    ),
                    justify="between",
                ),
            ),
            xxbg=rx.color("accent", 5),
            top="2px",
            bg=rx.color("accent", 7),
            box_shadow="linear-gradient(90deg, #667eea, #764ba2) 50px 50px",
        ),

        # Mobile / Tablet header
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    small_logo_icon(),
                    rx.heading("B alright", size="7", weight="bold"),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(rx.icon("menu", size=30)),
                    rx.menu.content(
                        navbar_link("Home", "/Home"),
                        navbar_link("About", "/About"),
                        navbar_link("Gallery", "/Gallery"),
                        navbar_link("Contact", "/Contact"),
                        # Auth section in the menu: account/logout when logged in, login trigger when not
                        rx.cond(
                            AuthState.is_logged_in,
                            rx.vstack(
                                rx.text(f"Logged in: {AuthState.user_email}", size="2"),
                                navbar_link("Account", "/Account"),
                                rx.menu.separator(),
                                rx.button(
                                    "Logout",
                                    on_click=AuthState.logout_and_redirect,
                                    variant="soft",
                                    color_scheme="red",
                                    size="2",
                                ),
                                spacing="1",
                            ),
                            # Use the same login button trigger (opens the single mounted modal)
                            login_button_trigger(),
                        ),
                    ),
                ),
                width="100%",
                justify="between",
                align_items="center",
            ),
            xxbg=rx.color("accent", 1),
            bg=rx.color("accent", 5),
            top="2px",
            z_index="10",
            width="100%",
            padding="10px",
        ),

        # Mount the modal once so LoginModalState events can open/close it reliably.
        login_modal(),
    )