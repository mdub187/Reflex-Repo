# lmrex/components/icon.py

import reflex as rx


def logo_icon(
    width: str = "2.25em",
    height: str = "auto",
    border_radius: str = "55%",
) -> rx.Component:
    return rx.image(
        src="/music-notes-minus-thin.svg",
        width=width,
        height=height,
        border_radius=border_radius,
        on_click=rx.redirect("/Home")
    )


def small_logo_icon() -> rx.Component:
    return logo_icon(width="1.5em", border_radius="25%")
