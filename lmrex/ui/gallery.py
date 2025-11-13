# lmrex/ui/gallery.py

from lmrex.components.color_mode import color_mode
from lmrex.components.footer import footer
from lmrex.components.media_carousel import media_carousel
from lmrex.components.media_modal import media_modal
from lmrex.components.menu import menu
from lmrex.components.navbar import navbar
from lmrex.models.media_model import MediaService
from lmrex.state.state import State
from lmrex.ui.gallery_music import gallery_music

from ..imports import rx
from ..template import template

gallery_url = "pages/gallery"


def gallery():
    return rx.box(
        template(),
        # navbar(),
        # rx.vstack(
        #     rx.heading(
        #         State.label,
        #         size="9",
        #         style={
        #             "background": "linear-gradient(45deg, #667eea, #764ba2)",
        #             "background_clip": "text",
        #             "color": "transparent",
        #             "margin_bottom": "1rem",
        #         },
        #     ),
        rx.box(media_carousel(media_modal)),
        rx.text(
            rx.code("creative"),
            url_redirect=gallery_url,
            size="5",
        ),
        rx.container(
            rx.menu.root(
                rx.menu.trigger(
                    rx.button(
                        id="Add_Media",
                        label="Add Media",
                        on_click=State.toggle_modal,
                    )
                ),
                rx.menu.content(menu()),
            ),
        ),
        # media_carousel(current_media_item=State.current_media_item),
        rx.button("Add Media", on_click=State.toggle_modal),
        # url_redirect=f"{gallery_music}",
        size="5",
        key="gallery",
        justify="center",
        align="center",
        min_height="80vh",
    )
    # rx.container(
    #     footer(),
    #     color_mode(),
    # ),
    # # media_modal(),
