# lmrex/ui/gallery_music.py

from ..imports import rx
from ..state.state import State


def gallery_music():
    """Render a gallery of audio media items."""
    return rx.container(
        rx.foreach(
            State.audio_only,  # ✅ use the reactive var directly
            lambda m: rx.card(
                rx.vstack(
                    rx.text(m.get("title", "Untitled"), size="4"),
                    rx.audio(src=m["url"], controls=True, width="100%"),
                ),
                width="100%",
                padding="1em",
                border_radius="1em",
                box_shadow="md",
            ),
        ),
        width="100%",
        padding="1em",
    )
