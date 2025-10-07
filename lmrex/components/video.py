# lmrex/ui/video.py

import reflex as rx


def video_component():
    return rx.container(
        rx.box(
        rx.video(url="https://vimeo.com/1124553909", type="video/mov",
        controls=True,
        autoplay=True,
        muted=True,
        loop=True,
        # align_items="center",
        # z_index="4",
        # width="500%",
        # height="-500%"
            )
        )
    )
    return video_component
