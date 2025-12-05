# lmrex/ui/gallery.py

import reflex as rx

from lmrex.components.color_mode import color_mode
from lmrex.components.footer import footer
from lmrex.components.heading import header
from lmrex.components.media_carousel import media_carousel
from lmrex.components.menu import menu
from lmrex.components.navbar import navbar
from lmrex.models.media_model import MediaService
from lmrex.state.media_state import MediaState
from lmrex.state.state import State

gallery_url = "pages/gallery"


def gallery() -> rx.Component:
    return rx.box(
        navbar(),
        rx.container(
        rx.vstack(
            header(),
             rx.text(
                    rx.code({"Creative"}),
                    size="5",
                    style={
                        "margin": "1rem 0 2rem 0",
                        "color": "#6b7280",
                    },
             ),
            rx.box(
            # State.change_label,
            rx.vstack(
                rx.menu.root(
                    rx.menu.trigger(
                        rx.button("Media"),
                    ),
                    rx.menu.content(menu()),
                    current_media_item = MediaState.current_media_item
            ),
            # rx.box(media_carousel(MediaState.current_media_item)),
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
        # border box styling
        style={
                        "background_color": "white",
                        "border_radius": "16px",
                        "padding": "2rem",
                        "box_shadow": "0 4px 6px rgba(0, 0, 0, 0.1)",
                        "margin": "0 auto",
                        # Responsive width
                        "width": "90%",
                        "max_width": "400px",
                        # "max_width": "480px",
                    },
                    ),
                spacing="6",
                justify="center",
                align="center",
                min_height="80vh",
                text_align="center",
        		),
          padding="20px",
          # style={
          #       "max_width": "1200px",
          #       "margin": "0 auto",
          #   },
         ),
        rx.container(
            footer(),
            color_mode(),
        	),
   )
    # return gallery()
