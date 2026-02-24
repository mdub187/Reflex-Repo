# ./lmrex/components/navbar.py
import reflex as rx
from lmrex.state.auth_state import AuthState
from .login_modal import login_modal
from .icon import logo_icon, small_logo_icon

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
                    logo_icon(),
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

                    # Conditional: Show Account button if logged in, Login modal if not
                    # Optional: Keep link to login page
                    rx.cond(
                    	 AuthState.is_logged_in,
                      rx.button(navbar_link("Account", "/Account")),
                      rx.button(navbar_link(login_modal())),
                    ),
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
                        # Conditional: Show user info/account if logged in, login modal if not
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
                            login_modal(),
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
