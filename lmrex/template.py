from typing import Callable
import reflex as rx


from .components.menu import menu
from .components.navbar import navbar


class State(rx.State):
    label: str = "LMREX"


def pages(self):
    []


class Pages(rx.Component):
    def __init__(self):
        super().__init__()
        self.state = State()
        # return (self)
        self.pages = [[0], [1], [2]]
        self.current_page = self.pages
        print(Pages)


class Template(rx.Component):
    def __init__(self):
        super().__init__()
        self.state = State()
        # return (self)


def template(child: rx.Component, args, **kwargs) -> rx.Component:
    print([type(x) for x in args])
    if not isinstance(child, rx.Component):
        child = rx.heading("Invalid child", size="9")
    return rx.container(
        child,
        # rx.flex(),
        args,
        # navbar(),
        rx.vstack(
            rx.heading(State.label, size="9"),
            # rx.color_mode.button(position="bottom-left"),
        ),
    )


if __name__ == "__main__":
    print(template)
