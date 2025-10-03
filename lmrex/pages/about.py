import reflex as rx
from lmrex.template import State
from ..components.navbar import navbar
from .components.color_mode import color_mode

# from lmrex.state.state import State
from .components.input import input as input


def about() -> rx.Component:
    return rx.box(
        navbar(),
        rx.vstack(
            rx.heading(State.label, size="9"),
            rx.text("About", rx.code({"./about"}), size="5"),
        ),
    )
    return about()


about()
