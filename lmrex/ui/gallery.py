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
            rx.heading(
                State.label,
                size="9",
                style={
                    "background": "linear-gradient(45deg, #667eea, #764ba2)",
                    "background_clip": "text",
                    "color": "transparent",
                    "margin_bottom": "1rem",
                },
            ),
            rx.text(
                rx.code("creative"),
                url_redirect=gallery_url,
                size="5",
            ),
            rx.container(),
            media_carousel(current_media_item=State.current_media_item),
            rx.container(media_carousel(State.current_media_item)),
            rx.code({"creative"}),
            url_redirect=gallery_url,
            size="5",
            key="gallery",
        ),
        rx.container(
            media_carousel(current_media_item=State.current_media_item),
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
