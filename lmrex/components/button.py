# ./lmrex/components/button.py

import reflex as rx
from lmrex.state.state import State

rx.button(
    # "Button",
    on_click=State.change_label,
    spacing="5",
    justify_self="none",
    min_height="85vh",
)
