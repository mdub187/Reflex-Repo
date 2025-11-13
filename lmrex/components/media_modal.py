# ./lmrex/components/media_modal.py
import reflex as rx

from lmrex.models.media_model import MediaService  # Import MediaService
from lmrex.state.state import State  # Import the State class for breadcrumbs


def media_modal() -> rx.Component:
    print("[Breadcrumb] Rendering media_modal")
    return rx.fragment(
        rx.button("Add Media", on_click=State.toggle_modal),
        rx.cond(
            State.show_modal,
            rx.box(
                rx.vstack(
                    rx.heading("Add Media"),
                    rx.input(
                        placeholder="Enter media title",
                        on_change=State.set_media_title,
                        value=State.media_title,
                    ),
                    rx.input(
                        placeholder="Enter media URL",
                        on_change=State.set_media_url,
                        value=State.media_url,
                    ),
                    rx.select(
                        placeholder="Select media type",
                        options=MediaService.VALID_MEDIA_TYPES,
                        on_change=State.set_media_type,
                        value=State.media_type,
                    ),
                    rx.button("Upload", on_click=State.handle_submit),
                    spacing="4",
                ),
                is_open=State.show_modal,
                # on_close=State.toggle_modal,
            ),
        ),
    )
