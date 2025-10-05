# ./lmrex/components/color_mode.py

import reflex as rx


def color_mode() -> rx.Component:
    return rx.container(
        # rx.footer(),
        rx.color_mode.button(
            class_name="color-mode-button",
            position="bottom-center",
            width="100%",
            justify_self="center",
            padding_top="1em",
        ),
    )
    return color_mode
