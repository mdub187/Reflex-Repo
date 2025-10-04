import reflex as rx
from lmrex.components.navbar import navbar
from lmrex.components.color_mode import color_mode
from lmrex.state.state import State

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
            rx.video(
                url="./assets/Main.mov",
                # auto_play=True,
                # loop=True,
                # muted=True,
                style={
                    "src": ("./assets/Main.mov"),
                    "vph": "100%",
                    "min_height": "100%",
                    "min_width": "100%",
                    "object_fit": "cover",
                    "right": 0,
                    "bottom": 0,
                    "z_index": 1,
                },
            ),
        ),
    )
    return gallery
