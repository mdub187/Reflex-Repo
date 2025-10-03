from typing import Callable
import reflex as rx


from .components.menu import menu
from .components.navbar import navbar


class State(rx.State):
    label: str = "LMREX"


class Template(rx.Component):
    def __init__(self):
        super().__init__()
        self.state = State()
        # return (self)


def template(page: rx.Component) -> rx.Component:
    return rx.box(
        rx.flex(),
        navbar(),
        rx.vstack(rx.heading(State.label, size="9"), rx.color_mode.button()),
    )


if __name__ == "__main__":
    print(dir)
