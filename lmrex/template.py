from typing import Callable

import imports

from .components.menu import menu
from .components.navbar import navbar


def template() -> rx.Component:
    return rx.box(
        rx.flex(),
        navbar(),
        rx.vstack(
            rx.heading(State.label, size="9"),
            rx.text(
                "This gon' b alright ...",
                rx.code({"./"}),
                size="5",
            ),
            rx.input(
                placeholder="type some shit",
                on_change=State.handle_input_change,
            ),
            rx.button("Lizzard", on_click=State.change_label),
            spacing="5",
            justify_self="none",
            min_height="85vh",
        ),
        rx.color_mode.button(position="bottom-center", width="100%"),
        justify_self="normal",
        padding_top="1em",
        # display="contents",
    )
