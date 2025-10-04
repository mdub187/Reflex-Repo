# lmrex/nav.py
import reflex as rx
from lmrex.state.state import State


def navlinks():
    return rx.hstack(
        rx.button("Home"),
        rx.button("About"),
        rx.button("Contact"),
        spacing="4",
    )
