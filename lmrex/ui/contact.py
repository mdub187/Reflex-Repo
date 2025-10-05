# lmrex/ui/contact.py

import reflex as rx
from lmrex.components.navbar import navbar
from lmrex.components.heading import header
from lmrex.components.color_mode import color_mode
from lmrex.state.state import State

contact = "pages/contact"


def contact() -> rx.Component:
    return rx.box(
        navbar(),
        rx.vstack(
            rx.heading(State.label, size="9"),
            rx.text(
                rx.code({"contact"}),
                url_redirect=(f"{contact}"),
                size="5",
            ),
        ),
        color_mode(),
    )
    return contact
