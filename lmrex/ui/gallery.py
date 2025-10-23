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
<<<<<<< HEAD
            rx.heading(
<<<<<<< Updated upstream
                State.label,
=======
                rx.text(State.label),
>>>>>>> Stashed changes
                size="9",
=======
            rx.heading(State.label, size="9",
>>>>>>> parent of 4a4eed8 (cleaning up refactor, added filed to .gitignore, added authentication logic, the logic is sitll a work in progress and isnt yet working. encountered some roadblocks i did have some help for co pilot. i want to clean up and make sure it didnt overcomplicate things.)
                style={
                    "background": "linear-gradient(45deg, #667eea, #764ba2)",
                    "background_clip": "text",
                    "color": "transparent",
                    "margin_bottom": "1rem",
                }),
            rx.text(
<<<<<<< HEAD
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
=======
                rx.code({"creative"}),
                url_redirect=gallery_url,
                size="5",
            ),
            rx.container(
            media_carousel(current_media_item=State.current_media_item)
            ),
>>>>>>> parent of 4a4eed8 (cleaning up refactor, added filed to .gitignore, added authentication logic, the logic is sitll a work in progress and isnt yet working. encountered some roadblocks i did have some help for co pilot. i want to clean up and make sure it didnt overcomplicate things.)
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
