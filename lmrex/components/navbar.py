# ./lmrex/components/navbar.py
import reflex as rx
from lmrex.state.auth_state import AuthState
from .login_modal import user_menu, login_modal
from lmrex.state.login_state import LoginState

def navbar_link(text, url=None, on_click=None) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium", display="contents"),
        href=url if url else "#",
        on_click=on_click,
        padding="10px",
        min_width="48px",
        # min_height="48px"
    )

def navbar() -> rx.Component:
    return rx.container(
        rx.box(
            rx.desktop_only(
                rx.hstack(
                    rx.hstack(
                        rx.image(
                            src="/music-notes-minus-thin.svg",
                            width="2.25em",
                            height="auto",
                            border_radius="55%",
                        ),
                        rx.heading("We Gon", size="7", weight="bold"),
                    ),
                    rx.hstack(
                        rx.button(navbar_link("Home", "/Home")),
                        rx.button(navbar_link("About", "/About")),
                        rx.button(navbar_link("Gallery", "/Gallery")),
                        rx.button(navbar_link("Contact", "/Contact")),
                        # LoginState.is_logged_in, rx.link(user_menu(),
                        rx.button(rx.link(login_modal(),
                        rx.cond(
                            LoginState.is_logged_in,
                            rx.button("Account"),  # Show if logged in
                            # rx.button("Login"),
                        ),
                        ),
                        # rx.cond(
                        #     # AuthState.is_logged_in,

                        #     # rx.button(rx.link(user_menu())),
                        #     # rx.button(rx.link(login_modal())),

                        ),
                    ),
                    justify="between",
                ),
            ),
            bg=rx.color("accent", 7),
            top="2px",
            box_shadow="linear-gradient(90deg, #667eea, #764ba2) 50px 50px",
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/music-notes-minus-thin.svg",
                        width="1.5em",
                        height="auto",
                        border_radius="25%",
                    ),
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
                        AuthState.is_logged_in,
                        rx.cond(
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
                            rx.button(rx.link(login_modal())),
                        ),
                    ),
                ),
                width="100%",
                justify="between",
                align_items="center",
            ),
            bg=rx.color("accent", 5),
            top="2px",
            z_index="10",
            width="100%",
            padding="10px",
        ),
    )
