

def navbar() -> rx.Component:
    return rx.container(
        rx.box(),
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="../music-notes-minus-thin.svg",
                        width="2.25em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading("Web App Example", size="7", weight="bold"),
                    # align_items="center",
                    # justify="start",
                    width="100%",
                ),
                rx.hstack(
                    navbar_link("Home", "/#"),
                    navbar_link(
                        "About", "/#"
                    ),  # adding a link ... replace the "/#" with a https://+{link}
                    navbar_link("Pricing", "/#"),
                    navbar_link("Contact", "/#"),
                    # justify="end",
                    spacing="5",
                ),
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="'../music-notes-minus-thin.svg'",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading("Dumbass Shit", size="6", weight="bold"),
                    align_items="center",
                ),
                rx.menu,
                # rx.menu.root(
                #     rx.menu.trigger(rx.icon("menu", size=30)),
                #     rx.menu.content(
                #         rx.menu.item("Home"),
                #         rx.menu.item("About"),
                #         rx.menu.item("Pricing"),
                #         rx.menu.item("Contact"),
                #     ),
                # justify="content",
                # ),
                # justify="between",
                # align_items="center",
                # width="100%",
            ),
            # max_width="890px",
        ),
        bg=rx.color("accent", 3),
        # padding="1em",
        justify_self="normal",
        # position="dynamic",
        top="0px",
        z_index="5",
        # width="100%",
    )
