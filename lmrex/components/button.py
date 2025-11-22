# ./lmrex/components/button.py

import reflex as rx

def button() -> rx.Component:
	rx.button(
    "Button",
    on_click=State.change_label,
    spacing="5",
    justify_self="none",
    min_height="85vh",
)
