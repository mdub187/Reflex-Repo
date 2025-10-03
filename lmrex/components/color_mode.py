import reflex as rx


def color_mode() -> rx.Component:
    return (
        rx.button(
            class_name="color-mode-button",
            position="bottom-center",
            width="100%",
            justify_self="center",
            padding_top="1em",
        ),
    )
