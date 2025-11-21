# lmrex/ui/index.py

from lmrex.components.color_mode import color_mode
from lmrex.components.footer import footer
from lmrex.components.heading import header
from lmrex.components.input import input
from lmrex.components.navbar import navbar
from lmrex.state.state import State

# from lmrex.ui.responsive_utils import apply_responsive_styles
from ..imports import rx

# index = "/"


def index() -> rx.Component:
    return rx.box(
        # apply_responsive_styles(),
        navbar(),
        rx.vstack(
            # Welcome section with nice styling
        header(),
            rx.text(
                rx.code({"Hello"}),
                size="5",
                style={
                    "margin": "1rem 0 2rem 0",
                    "color": "#6b7280",
                },
            ),
            header(),
            rx.text(
                rx.code({"Yourself"}),
                size="5",
                style={
                    "margin": "1rem 0 2rem 0",
                    "color": "#6b7280",
                },
            ),
            # Interactive elements in a nice container
            rx.box(
                rx.vstack(
                    input(rx.input),
                    rx.button(
                        "Lizzard",
                        on_click=State.change_label(),
                        size="3",
                        style={
                            "background_color": "#667eea",
                            "color": "white",
                            "border_radius": "8px",
                            "padding": "0.75rem 2rem",
                            "margin_top": "1rem",
                        },
                    ),
                    spacing="4",
                    align="center",
                ),
                style={
                    "background_color": "white",
                    "border_radius": "12px",
                    "padding": "2rem",
                    "box_shadow": "0 4px 6px rgba(0, 0, 0, 0.1)",
                    "max_width": "400px",
                },
            ),
            spacing="6",
            justify="center",
            align="center",
            min_height="80vh",
            text_align="center",
        ),
        rx.container(
            footer(),
            color_mode(),
            # icon_dir(),
        ),
    )
