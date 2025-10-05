# ./lmrex/components/footer.py

import reflex as rx
from .color_mode import color_mode


def footer() -> rx.Component:
    return rx.container(
        (
            rx.container(
                rx.color_mode.button(),
            ),
        )
    )
    return footer
