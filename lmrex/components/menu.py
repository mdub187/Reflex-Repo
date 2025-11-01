# lmrex/components/menu.py

import reflex as rx


def menu() -> rx.Component:
    return rx.container(
        rx.menu.root(
            rx.menu.trigger(rx.icon("Media", size=30)),
            rx.menu.content(
                rx.menu.item("Photo"),
                rx.menu.item("Video"),
                rx.menu.item("Graphic"),
                rx.menu.item("Audio"),
                rx.menu.item("Ideas"),
            ),
        ),
    )
