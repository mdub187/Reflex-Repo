import reflex as rx
from ..state.state import State
from ..components.footer import footer
from ..components.color_mode import color_mode


def user_login() -> rx.Component:
    print("Debug: user_login component is being rendered")
    return rx.box(
        rx.vstack(
            rx.alert_dialog.trigger(
                rx.box(
                    rx.hstack(
                    rx.heading("Debug Modal"),
                    size="3",
                    # rx.box("This is a simple modal for debugging."),
                        justify="center"
                    ),
                    rx.button("Close", on_click=State.toggle_modal),
            rx.alert_dialog.cancel(
                    rx.button(
                        "Cancel",
                        variant="soft",
                        color_scheme="gray",
                        ),
                    ),
                # is_open=True,  # Force modal to always render for debugging
                ), # Toggle modal visibility on close action
            ),
            spacing="5",
            justify="center",
            align="center",
            min_height="80vh",
            text_align="center",
        ),
        rx.container(
            footer(),
            color_mode(),
        ),
    )