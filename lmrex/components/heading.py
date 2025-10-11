# lmrex/components/heading.py

import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.heading("Welcome", size="9"),
        rx.color_mode.button(),
        spacing="3",
        align="center",
    )
