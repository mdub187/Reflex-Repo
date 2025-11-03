# ./lmrex/components/navbar.py
import reflex as rx

from .user_login import user_login


def navbar_link(text, url) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium", display="contents"), href=url
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
                    rx.link(user_login(), create_account=True, spacing="5"),
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
                        rx.menu.item("Home"),
                        rx.menu.item("About"),
                        rx.menu.item("Gallery"),
                        rx.menu.item("Contact"),
                        rx.menu.item("Login"),  # could hook modal here too
                    ),
                ),
            ),
        ),
        # xxbg=rx.color("accent", 3),
        top="2px",
        z_index="5",
    )
