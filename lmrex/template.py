## root level template.py
# /lmrex/template.py

from typing import Callable
import reflex as rx


from .components.menu import menu
from .components.navbar import navbar
from .components.footer import footer
from .components.color_mode import color_mode
from .components.heading import header


# from .components.heading import heading
class State(rx.State):
    label: str = "LMREX"


class Template(rx.Component):
    def __init__(self):
        super().__init__()
        self.state = State()
        # return (self)


def template(child: rx.Component, args, **kwargs) -> rx.Component:
    # print([type(x) for x in args])
    if not isinstance(child, rx.Component):
        child = rx.heading("Invalid child", size="9")
    return rx.container(
        child,
        # rx.flex(),
        # args,
        # header(),
        navbar(),
        # color_mode(),
        footer(),
        rx.heading(State.label, size="9"),
        # min_height="50vh",
        color_mode(),
    )
    return template


if __name__ == "__main__":
    print(template)
