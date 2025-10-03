import reflex as rx
from lmrex.components.navbar import navbar
from lmrex.components.color_mode import color_mode
from lmrex.state.state import State
# from lmrex.components.input import input as input


def products() -> rx.Component:
    return rx.box(
        navbar(),
        rx.vstack(
            rx.heading(State.label, size="9"),
            rx.text("Gallery", rx.code({""}), url_redirect=("/gallery"), size="5"),
        ),
    )
