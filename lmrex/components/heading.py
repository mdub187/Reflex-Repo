# lmrex/components/heading.py

import reflex as rx

from lmrex.state.state import State


def header() -> rx.Component:
    return rx.vstack(
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
    )
