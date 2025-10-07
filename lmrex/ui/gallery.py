# lmrex/ui/gallery.py

import reflex as rx
from lmrex.components.navbar import navbar
from lmrex.components.color_mode import color_mode
from lmrex.state.state import State
from lmrex.components.video import video_component as video

gallery = "pages/gallery"


def gallery() -> rx.Component:
    return rx.box(
        navbar(),
        rx.vstack(
            rx.heading(State.label, size="9"),
            rx.text(
                rx.code({"gallery"}),
                url_redirect=(f"{gallery}"),
                size="5",
            ),
            rx.container(video()),
        ),
        color_mode(),
    )
    return gallery
