# lmrex/template.py
from lmrex.components.color_mode import color_mode
from lmrex.components.footer import footer
from lmrex.components.heading import header
from lmrex.components.navbar import navbar
from lmrex.state.state import State

from .imports import rx


def template() -> rx.Component:
    return rx.box(
        navbar(),
        rx.container(
            rx.vstack(
                header(),
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
                spacing="6",
                justify="center",
                align="center",
                min_height="80vh",
                text_align="center",
            ),
            padding="20px",
            style={
                "max_width": "1200px",
                "margin": "0 auto",
            },
        ),
        rx.container(
            footer(),
            color_mode(),
        ),
    )
