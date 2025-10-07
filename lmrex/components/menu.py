# lmrex/components/menu.py

import reflex as rx


def menu() -> rx.Component:
    return rx.container(
        rx.menu.root(
            rx.menu.trigger(rx.icon("menu", size=30)),
            rx.menu.content(
                rx.menu.item("Home"),
                rx.menu.item("About"),
                rx.menu.item("Gallery"),
                rx.menu.item("Contact"),
                rx.menu.item("Login")
            ),
        ),
    )
