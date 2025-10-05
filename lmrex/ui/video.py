# lmrex/ui/video.py

import reflex as rx


def video_component():
    return rx.container(
        rx.video(url="https://vimeo.com/1124553909", type="video/mov"),
        # controls=True,
        autoplay=True,
        muted=True,
        loop=True,
    )
    return video_component
