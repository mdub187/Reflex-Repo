import reflex as rx
from ..state.state import State

rx.input(
    placeholder="type some shit",
    on_change=State.handle_input_change,
)
