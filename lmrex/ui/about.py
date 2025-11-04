# lmrex/ui/about.py

import reflex as rx

from lmrex import template
from lmrex.components.color_mode import color_mode
from lmrex.components.footer import footer
from lmrex.components.heading import header
from lmrex.components.navbar import navbar
from lmrex.state.state import State

about = "pages/about"


def about() -> rx.Component:
    return rx.box(
        navbar(),
        rx.vstack(
            header(),
            rx.text(rx.code({"about"}), url_redirect=(f"{about}"), size="5"),
            spacing="5",
            justify="center",
            align="center",
            min_height="80vh",
            text_align="center",
        ),
        rx.container(
            footer(),
            color_mode(),
        ),
    )
