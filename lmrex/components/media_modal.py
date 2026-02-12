# lmrex/components/media_modal.py
from ..imports import rx
from ..state.state import State
from ..models.media_model import MediaService

class MediaFormState(rx.State):
    """Local state for the media modal form."""
    media_type: str = ""
    media_title: str = ""
    media_url: str = ""

    @rx.event
    def set_media_type(self, value: str):
        self.media_type = value

    @rx.event
    def set_media_title(self, value: str):
        self.media_title = value

    @rx.event
    def set_media_url(self, value: str):
        self.media_url = value

    @rx.event
    def handle_submit(self):
        """Create a media item, add it to the global State, reset the form, and close the modal."""
        try:
            media_type = self.media_type or "image"
            if not MediaService.is_valid_media_type(media_type):
                raise ValueError(f"Invalid media type: {media_type}")
            new_item = MediaService.create_media_item(
                self.media_title, self.media_url, media_type
            )
            State.media = State.media + [new_item]
            print("Media added:", new_item)
        except ValueError as e:
            print(f"Failed to add media: {e}")
            return

        # Reset form fields
        self.media_type = ""
        self.media_title = ""
        self.media_url = ""

        # Close the modal that is controlled by global State
        State.show_modal = False

def media_modal() -> rx.Component:
    return rx.dialog.root(
        # Use a trigger that toggles the global state so external "Add Media" buttons can also control it
        rx.dialog.trigger(rx.button("Add Media", id="Add_Media", on_click=State.toggle_modal)),
        rx.dialog.content(
            rx.heading("Add Media", size="6"),
            rx.text("What media would you like to add?"),
            rx.form(
                rx.input(
                    placeholder="Type of",
                    value=MediaFormState.media_type,
                    on_change=MediaFormState.set_media_type,
                ),
                rx.input(
                    placeholder="Title",
                    value=MediaFormState.media_title,
                    on_change=MediaFormState.set_media_title,
                ),
                rx.input(
                    placeholder="URL",
                    value=MediaFormState.media_url,
                    on_change=MediaFormState.set_media_url,
                ),
                rx.button(
                    "Submit",
                    on_click=MediaFormState.handle_submit,
                ),
            ),
            rx.spacer(column=1),
        ),
        is_open=State.show_modal,
    )
