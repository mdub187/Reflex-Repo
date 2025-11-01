# lmrex/ui/gallery.py

import reflex as rx

from lmrex.components.color_mode import color_mode
from lmrex.components.footer import footer
from lmrex.components.media_carousel import media_carousel
from lmrex.components.menu import menu
from lmrex.components.navbar import navbar
from lmrex.state.state import State

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
                # rx.code("creative"),
                url_redirect=gallery_url,
                size="5",
            ),
            rx.container(
                rx.menu.root(
                    rx.menu.trigger(
                        rx.button("Media"),
                    ),
                    rx.menu.content(menu()),
                ),
            ),
            media_carousel(current_media_item=State.current_media_item),
            # rx.container(media_carousel(State.current_media_item)),
            # rx.code({"creative"}),
            url_redirect=gallery_url,
            size="5",
            key="gallery",
            justify="center",
            align="center",
        ),
        # rx.container(
        #     # media_carousel(current_media_item=State.current_media_item),
        #     spacing="5",
        #     min_height="80vh",
        #     text_align="center",
        # ),
        rx.container(
            footer(),
            color_mode(),
        ),
    )
