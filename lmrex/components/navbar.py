import reflex as rx


def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium", display="contents"), href=url
    )


def navbar() -> rx.Component:
    return rx.container(
        rx.box(),
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/music-notes-minus-thin.svg",  # Corrected path
                        width="2.25em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading("Web App Example", size="7", weight="bold"),
                    width="100%",
                ),
                rx.hstack(
                    navbar_link("Home", "/#"),
                    navbar_link("About", "/#"),
                    navbar_link("Gallery", "/#"),
                    navbar_link("Contact", "/#"),
                    spacing="5",
                ),
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/music-notes-minus-thin.svg",  # Corrected path
                        width="1.5em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading("Dumbass Shit", size="7", weight="bold"),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(rx.icon("menu", size=30)),
                    rx.menu.content(
                        rx.menu.item("Home"),
                        rx.menu.item("About"),
                        rx.menu.item("Gallery"),
                        rx.menu.item("Contact"),
                    ),
                ),
            ),
        ),
        bg=rx.color("accent", 3),
        top="2px",
        z_index="5",
    )
