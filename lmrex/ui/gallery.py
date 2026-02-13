# lmrex/ui/gallery.py
from lmrex.components.color_mode import color_mode
from lmrex.components.footer import footer
from lmrex.components.media_carousel import media_carousel
from lmrex.components.media_modal import media_modal
from lmrex.components.menu import menu
from lmrex.components.heading import header
from lmrex.components.navbar import navbar
from lmrex.state.state import State
from ..ui.responsive_utils import apply_responsive_styles
from ..imports import rx

def gallery() -> rx.Component:
    return rx.box(
        navbar(),
        rx.vstack(
            header(),
            rx.text(
                rx.code("Creative"),
                size="5",
                # style={
                # 		"margin": "1rem 0 2rem 0",
                #  		"color": "#6b7280",
                # },
            ),
            rx.box(
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
            media_modal(),
            media_carousel(current_media_item=State.current_media_item),
            rx.button("Add Media", on_click=State.toggle_modal),
            rx.container(
                footer(),
                color_mode(),
            ),
            spacing="5",
            justify="center",
            align="center",
            min_height="80vh",
            text_align="center",
        ),
        style=apply_responsive_styles(),
    )
