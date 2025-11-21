# lmrex/ui/contact.py

from lmrex.components.color_mode import color_mode
from lmrex.components.footer import footer
from lmrex.components.heading import header
from lmrex.components.navbar import navbar
from lmrex.components.menu import menu

from ..imports import rx

contact_url = "pages/contact"


def contact() -> rx.Component:
    return rx.box(
        navbar(),
        rx.vstack(
            header(),
            menu(),
            rx.text(
                rx.code("Resources"),
                size="5",
            ),
            rx.vstack(
                rx.text("Get in touch with me:"),
                rx.text(
                    "Email: ",
                    rx.link("This is my email", href="mailto:maweeks85@comcast.net"),
                ),
                rx.text("Phone: (555) 123-4567"),
                spacing="2",
            ),
            spacing="5",
            justify="center",
            align="center",
            min_height="80vh",
            text_align="center",
        ),
        rx.container(footer(), color_mode()),
    )
