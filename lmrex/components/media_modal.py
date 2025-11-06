# lmrex/components/media_modal.py

from ..imports import rx
from ..state.state import State


def media_modal() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(rx.button("Add Media", id="Add_Media")),
        rx.dialog.content(
            rx.heading("Add Media", size="6"),
            rx.text("What media would you like to add?"),
            rx.form(
                rx.input(placeholder="Type of", id="media_type"),
                rx.input(placeholder="Title", id="media_title"),
                rx.input(placeholder="URL", id="media_url"),
                rx.dialog.close(
                    rx.button(
                        "Submit",
                        on_click=lambda: State.add_media_item(
                            rx.get_value("media_title"),
                            rx.get_value("media_url"),
                            rx.get_value("media_type"),
                        ),
                    )
                ),
            ),
            rx.spacer(column=1),
        ),
        is_open=State.show_modal,
    )
