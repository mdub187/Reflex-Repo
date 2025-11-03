# lmrex/components/menu.py

import reflex as rx


def menu() -> rx.Component:
    return rx.container(
        rx.menu.root(
            rx.menu.trigger(rx.icon("Media", size=30)),
            rx.menu.content(
                rx.menu.item("Photo", href="./photo"),
                rx.menu.item("Video", href="/video"),
                rx.menu.item("Graphic", href="/graphic"),
                rx.menu.item("Audio", href="/audio"),
                rx.menu.item("Ideas", href="/ideas"),
            ),
        ),
    )
