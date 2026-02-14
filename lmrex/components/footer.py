# lmrex/components/__init__.py
import reflex as rx
from .color_mode import color_mode
from .social_icons import social_icons_footer

def footer() -> rx.Component:
    """Simple footer component for debugging social icons."""
    return rx.box(
        rx.container(
            rx.hstack(
                # Copyright text
                rx.text("© 2025 Marc Weeks", size="2", color="gray.600"),
                # Social icons
                social_icons_footer(
                ),
                rx.box(),
                align_content="center",
                # Color mode toggle
                justify="center",
                align="center",
                width="100%",
            ),
            # max_width="1200px",
        ),
        width="100%",
        padding="4",
        border_top="1px solid",
        border_color="gray.200",
        background="gray.50",
        _dark={"border_color": "gray.700", "background": "gray.900"},
    )
