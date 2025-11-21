# ./lmrex/components/navbar.py
import reflex as rx

# from .media_modal import media_modal
from lmrex.ui.login import login


def navbar_link(text, url) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium", display="contents"),
        href=url,
        padding="10px",
        min_width="48px",  # Minimum touch target size
        min_height="48px",  # Minimum touch target size
    )


def navbar() -> rx.Component:
    return rx.container(
        rx.box(),
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        href="/",
                        src="/music-notes-minus-thin.svg",
                        width="2.25em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading("We Gon", size="7", weight="bold"),
                    width="100%",
                ),
                rx.hstack(
                    rx.link("home", href="/"),
                    rx.link("about", href="/About"),
                    rx.link("gallery", href="/Gallery"),
                    rx.link("contact", href="/Contact"),
                    rx.button("login"),
                ),
            ),
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
                        # navbar_link("Home", "/"),
                        # navbar_link("About", "/About"),
                        # navbar_link("Gallery", "/Gallery"),
                        # navbar_link("Contact", "/Contact"),
                        # rx.menu.item(rx.link(login(), create_account=True)),
                        # # rx.menu.item(media_modal()),
                        # # rx.menu.item(user_login()),
                    ),
                ),
            ),
        ),
        # xxbg=rx.color("accent", 3),
        top="2px",
        z_index="5",
    )
