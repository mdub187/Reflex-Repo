# ./lmrex/components/navbar.py
import reflex as rx
from lmrex.state.auth_state import AuthState
from .login_modal import user_menu, login_modal, LoginModalState

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
                    # width="100%",
                ),
                rx.hstack(
                    rx.button(navbar_link("Home", "/Home")),
                    rx.button(navbar_link("About", "/About")),
                    rx.button(navbar_link("Gallery", "/Gallery")),
                    rx.button(navbar_link("Contact", "/Contact")),
                    # Login modal + user menu
                    # # rx.button(

                    #     navbar_link(
                    #     text="Login Modal",
                    #     on_click=user_menu,
                    #     # padding="10px",
                    #     # min_width="48px",


                    # ),

                    # Optional: Keep link to login page
                    rx.button(rx.link(login_modal())),
                    # rx.button(navbar_link("login")),
                ),
                # min_width="100%",
                justify="between",
                # align_items="center",
                # background=("linear-gradient(45deg, #667eea, #764ba2)"),
            ),
        ),
        xxbg=rx.color("accent", 5),
        top="2px",
        # z_index="5",
        # width="100%",
        bg=rx.color("accent", 7),
        # padding="1px",
        # border_radius="5%"
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
                        rx.button(rx.link(login_modal())),

                        # Mobile login - use login modal trigger
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
                            # Login modal in menu
                            # login_modal(),
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
)
