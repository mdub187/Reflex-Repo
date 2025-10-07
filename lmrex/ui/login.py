import reflex as rx
from ..state.state import State

def user_login(self) -> rx.Component:
    print("Debug: user_login component is being rendered")
    return rx.vstack(
        rx.alert_dialog.trigger(
            content=rx.box(
                rx.heading("Debug Modal", size="3"),
                rx.box("This is a simple modal for debugging."),
                rx.hstack(
                    rx.button("Close", on_click=State.toggle_modal),
                    justify="center"
                ),
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
    )
    return user_login
