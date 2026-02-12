# lmrex/components/input.py
import reflex as rx
from ..state.state import State

def input(self) -> rx.Component:
    return rx.input(
        placeholder="type some shit",
        on_change=State.handle_input_change,
    )
    return input
