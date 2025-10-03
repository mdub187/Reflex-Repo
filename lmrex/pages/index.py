import reflex as rx
from lmrex.components.navbar import navbar
from lmrex.components.color_mode import color_mode
from lmrex.state.state import State
from lmrex.components.input import input as input


def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.vstack(
            rx.heading(State.label, size="9"),
            rx.text(
                "This gon' b alright ...",
                rx.code({"./"}),
                size="5",
            ),
            input("self"),
            rx.button("Lizzard", on_click=State.change_label),
            spacing="5",
            justify_self="none",
            min_height="85vh",
        ),
        rx.color_mode.button(),
        # rx.color_mode.button(position="bottom-center", width="100%"),
        # padding_top="1em",
    )
    return index()


index()
