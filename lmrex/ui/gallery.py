# lmrex/ui/gallery.py

import reflex as rx
from lmrex.components.heading import header
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
<<<<<<< Updated upstream
                State.label,
=======
                rx.text(State.label),
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
                url_redirect=gallery_url,
                size="5",
            ),
            rx.container(media_carousel()),
=======
                size="5",
            ),
            rx.container(media_carousel(State.current_media_item)),
>>>>>>> Stashed changes
            spacing="5",
            justify="center",
            align="center",
            min_height="80vh",
            text_align="center",
        ),
        rx.container(
            # footer(),
            # color_mode(),
        ),
    )
