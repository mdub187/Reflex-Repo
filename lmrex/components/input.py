# lmrex/components/input.py
import reflex as rx
from ..state.state import State

def input(self) -> rx.Component:
    return rx.input(
        placeholder="type some shit",
        on_change=State.handle_input_change,
        style = {"resize": "both",
        						"max-width": "75%",
              				"max-height": "75%",
                        "overflow": "auto",
                        "padding":"50px"
        }
    )
    return input
