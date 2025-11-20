# lmrex/ui/video.py

import reflex as rx


def video_component():
    return rx.container(
        rx.box(
            rx.video(
                url="https://vimeo.com/1124553909",
                type="video/mp4",
                controls=True,
                autoplay=True,
                muted=True,
                loop=True,
                width="100%",
                height="100%",
            ),
            style={
                "width": "100%",
                "height": "400px",
                "border_radius": "8px",
                "overflow": "hidden",
            },
        ),
        style={"max_width": "800px", "margin": "0 auto", "padding": "20px"},
    )
