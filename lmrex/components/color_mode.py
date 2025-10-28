# ./lmrex/components/color_mode.py

import reflex as rx


def color_mode() -> rx.Component:
    return rx.container(
        # rx.footer(),
        rx.color_mode.button(
            class_name="color-mode-button",
            # position="",
            width="100%",
            justify_self="bottom-right",
            padding_top="1em",
        ),
    )
    # return color_mode
