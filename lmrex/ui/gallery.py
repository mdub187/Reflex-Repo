# lmrex/ui/gallery.py

import reflex as rx
from lmrex.components.navbar import navbar
from lmrex.components.color_mode import color_mode
from lmrex.state.state import State
from lmrex.components.media_carousel import media_carousel

gallery_url = "pages/gallery"

def gallery() -> rx.Component:
    return rx.box(
        navbar(),
        rx.vstack(
            rx.heading(State.label, size="9"),
            rx.text(
                "Gallery Page",
                url_redirect=gallery_url,
                size="5",
            ),
            rx.container(
            media_carousel()
            ),
        ),
        color_mode(),
    )
