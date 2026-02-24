# lmrex/ui/about.py
import reflex as rx
from lmrex import template
from lmrex.components.color_mode import color_mode
from lmrex.components.footer import footer
from lmrex.components.heading import header
from lmrex.components.navbar import navbar
from lmrex.state.state import State
from lmrex.assets.loremtext import lorem_image


def about() -> rx.Component:
    return rx.box(
        navbar(),
        rx.vstack(
            rx.text(rx.code({"About"}), url_redirect=(f"{about}"), size="5"),
            header(),
            rx.box(
            """Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa.
            justify_self="column",
            Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem.
            Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo.
            Nullam dictum felis eu pede mollis pretium.""",
            rx.container(lorem_image()),
            """Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus.
            Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet.
            Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar,""",
            rx.container(lorem_image()),
            rx.text(
            rx.code({"""---Mea culpa unum Marc---"""}),
            ),
            ),
            spacing="5",
            align="center",
            min_height="80vh",
            text_align="center",
        ),
        rx.container(
            footer(),
            color_mode(),
        ),
    )
