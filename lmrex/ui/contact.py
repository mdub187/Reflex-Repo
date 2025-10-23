# lmrex/ui/contact.py

import reflex as rx
from lmrex.components.navbar import navbar
from lmrex.components.heading import heading.header
from lmrex.components.color_mode import color_mode
from lmrex.components.footer import footer
from lmrex.state.state import State

contact_url = "pages/contact"

def contact() -> rx.Component:
    return rx.box(
        navbar(),
        rx.vstack(
<<<<<<< HEAD
<<<<<<< Updated upstream
            rx.heading(
                (State.label),
                header(),
                rx.text(
                    rx.code("Resources"),
                    size="5",
                ),
                rx.vstack(
                    rx.text("Get in touch with me:"),
                    rx.text(
                        "Email: ",
                        rx.link("mdub187@dub.com", href="mailto:mdub187@dub.com"),
                    ),
                    rx.text("Phone: (555) 123-4567"),
                    spacing="2",
                ),
                spacing="5",
                justify="center",
                align="center",
                min_height="80vh",
                text_align="center",
            ),
            rx.container(
                # footer(),
                # color_mode(),
=======
            rx.heading(rx.text(State.label)),
            rx.text(
                rx.code({"Resources"}),
                size="5",
            ),
            rx.vstack(
                rx.text("Get in touch with me:"),
                rx.text(
                    "Email: ", rx.link("mdub187@dub.com", href="mailto:mdub187@dub.com")
                ),
                rx.text("Phone: (555) 123-4567"),
                spacing="2",
>>>>>>> Stashed changes
=======
            header(),
            rx.text(rx.code({"Resources"}),
                size="5",
            ),
            rx.vstack(
                rx.text("Get in touch with me:"),
                rx.text("Email: ", rx.link("mdub187@dub.com", href="mailto:mdub187@dub.com")),
                rx.text("Phone: (555) 123-4567"),
                spacing="2",
>>>>>>> parent of 4a4eed8 (cleaning up refactor, added filed to .gitignore, added authentication logic, the logic is sitll a work in progress and isnt yet working. encountered some roadblocks i did have some help for co pilot. i want to clean up and make sure it didnt overcomplicate things.)
            ),
            spacing="5",
            justify="center",
            align="center",
            min_height="80vh",
            text_align="center",
        ),
        rx.container(
            footer(),
            # color_mode(),
        ),
    )
