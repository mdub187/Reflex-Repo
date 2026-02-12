# ./lmrex/components/navbar.py
import reflex as rx

from .user_login import user_login

def navbar_link(text, url) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium", display="contents"),
        href=url,
        padding="10px",
        min_width="48px",
        min_height="48px",
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
                    width="100%",
                ),
                rx.hstack(
                    rx.button(navbar_link("Home", "/Home")),
                    rx.button(navbar_link("About", "/About")),
                    rx.button(navbar_link("Gallery", "/Gallery")),
                    rx.button(navbar_link("Contact", "/Contact")),
                    rx.button(navbar_link("Login", "/Login")),
                ),
                min_width="100%",
                justify="between",
                align_items="center",
                background="linear-gradient(45deg, #667eea, #764ba2)",
            ),
        ),
        top="2px",
        max_width="100%",
        padding="0px",
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
                    ),
                ),
                width="100%",
                justify="between",
                align_items="center",
            ),
        top="2px",
        z_index="5",
        width="100%",
        padding="10px",
    ),
)
