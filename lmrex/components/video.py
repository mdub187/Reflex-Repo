# lmrex/ui/video.py

import reflex as rx


def video_component():
    return rx.container(
        rx.box(
            style={
                "width": "100%",
                "height": "400px",
                "border_radius": "8px",
                "overflow": "hidden",
            },
        ),
        style={"max_width": "800px", "margin": "0 auto", "padding": "20px"},
    )
