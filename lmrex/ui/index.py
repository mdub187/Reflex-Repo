# lmrex/ui/index.py

import reflex as rx
from lmrex.components.navbar import navbar
from lmrex.components.color_mode import color_mode
from lmrex.state.state import State
from lmrex.components.input import input
from lmrex.components.footer import footer
from lmrex.components.heading import header
# from lmrex.components.media_carousel import media_carousel
# from lmrex.template import template

index = "/index"

def index() -> rx.Component:
    return rx.box(
        header(),
        # UserLogin(State),
        navbar(),
        rx.vstack(
            # rx.text("This gon'"),
            rx.heading(State.label, size="9"),
            rx.text(rx.code({"alright"}),
                # rx.code({"./"}),
                size="5",
                justify_items="center",
            ),
            # media_carousel,
            input(rx.input),
            rx.button("Lizzard", on_click=State.change_label),
            spacing="5",
            justify_self="none",
            min_height="85vh",
            # rx.color_mode.button(),
            #
            ),
        color_mode(),
        )
        # footer(),
        # rx.color_mode.button(position="bottom-center", width="100%"),
        # padding_top="1em",
    return index
