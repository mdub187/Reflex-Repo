# lmrex/ui/about.py

import reflex as rx
from lmrex.components.navbar import navbar
from lmrex.components.color_mode import color_mode
from lmrex.state.state import State
from lmrex import template

about = "pages/about"


def about() -> rx.Component:
    return rx.box(
        navbar(),
        rx.vstack(
            rx.heading(State.label, size="9"),
            rx.text(rx.code({"about"}), url_redirect=(f"{about}"), size="5"),
        ),
        color_mode(),
    )
    return about
