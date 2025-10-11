# lmrex/ui/contact.py

import reflex as rx
from lmrex.components.navbar import navbar
from lmrex.components.heading import header
from lmrex.components.color_mode import color_mode
from lmrex.components.footer import footer
from lmrex.state.state import State

contact_url = "pages/contact"

def contact() -> rx.Component:
    return rx.box(
        navbar(),
        rx.vstack(
            rx.heading(State.label, size="9"),
            rx.text(
                "Contact Page",
                size="5",
            ),
            rx.vstack(
                rx.text("Get in touch with us:"),
                rx.text("Email: contact@example.com"),
                rx.text("Phone: (555) 123-4567"),
                spacing="2",
            ),
            spacing="5",
            justify="center",
            align="center",
            min_height="80vh",
            text_align="center",
        ),
        rx.container(
            footer(),
            # color_mode(),
        ),
    )