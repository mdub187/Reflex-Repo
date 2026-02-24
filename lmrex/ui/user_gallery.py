# ui.user_gallery.py


import reflex as rx
from ..state import state



def user_gallery() -> rx.Component:
	return rx.box(
            rx.heading("Add Media", size="6"),
            rx.text("What media would you like to add?"),
            rx.form(
                rx.input(
                    placeholder="Type of",
                    value=state.State.media_type,
                    # on_change=FormState.set_media_type,
                ),
                rx.input(
                    placeholder="Title",
                    value=state.State.media_title,
                    # on_change=FormState.set_media_title,
                ),
                rx.input(
                    placeholder="URL",
                    value=state.State.media_url,
                    # on_change=MediaFormState.set_media_url,
                ),
                rx.button(
                    "Submit",
                    on_click=state.FormState.handle_submit,
                ),
            ),
            rx.spacer(column=1),
        )
