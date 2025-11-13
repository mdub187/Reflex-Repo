from ..imports import rx


def contact_component() -> rx.Component:
    return rx.box(
        rx.container(
            rx.text("Get in touch with me:"),
            rx.text(
                "Email: ",
                rx.link("This is my email", href="mailto:maweeks85@comcast.net"),
            ),
            rx.text("Phone: (555) 123-4567"),
            spacing="2",
        ),
        spacing="5",
        justify="center",
        align="center",
        min_height="80vh",
        text_align="center",
    )
