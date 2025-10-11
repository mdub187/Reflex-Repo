# lmrex/ui/gallery.py

import reflex as rx
from lmrex.components.navbar import navbar
from lmrex.components.color_mode import color_mode
from lmrex.components.footer import footer
from lmrex.state.state import State
from lmrex.components.media_carousel import media_carousel

gallery_url = "pages/gallery"

def gallery() -> rx.Component:
    return rx.box(
        navbar(),
        rx.vstack(
            rx.heading(State.label, size="9"),
            rx.text(
                rx.code({"api so high"}),
                url_redirect=gallery_url,
                size="5",
            ),
            rx.container(
            media_carousel(current_media_item=State.current_media_item)
            ),
            spacing="5",
            justify="center",
            align="center",
            min_height="80vh",
            text_align="center",
        ),
        rx.container(
            footer(),
            # color_mode(),
        ),
    )
