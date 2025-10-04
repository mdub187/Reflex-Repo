import reflex as rx
from color_mode import color_mode


def footer() -> rx.Component:
    (
        rx.container(
            rx.color_mode.button(position="bottom-center", padding_top="1em"),
        ),
    )
    return footer
