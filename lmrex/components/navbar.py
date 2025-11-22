# ./lmrex/components/navbar.py
import reflex as rx

from .user_login import AuthState, user_login


def navbar_link(text, url) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium", display="contents"),
        href=url,
        padding="10px",
        min_width="48px",  # Minimum touch target size
        min_height="48px",  # Minimum touch target size
    )


def navbar() -> rx.Component:
    return rx.container(
        rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/music-notes-minus-thin.svg",
                        width="2.25em",
                        height="auto",
                        border_radius="55%",
                    ),
                    rx.heading("We Gon", size="7", weight="bold"),
                    width="100%",
                    align_items="center",  # Ensure alignment
                ),
                rx.hstack(
                    rx.button(navbar_link("home", "/")),
                    rx.button(navbar_link("about", "/About")),
                    rx.button(navbar_link("gallery", "/Gallery")),
                    rx.button(navbar_link("contact", "/Contact")),
                    rx.button(navbar_link("Login", '/login/protected/account')),
                    # rx.button(navbar_link("Register", '/register')),
                    spacing="5",
                    align_items="center",  # Ensure alignment
                ),
                width="100%",
                justify="between",
                align_items="center",
                background="linear-gradient(45deg, #667eea, #764ba2)",  # Ensure alignment
            ),
<<<<<<< Updated upstream
        )
        # width="100%",
        # max_width="none",
        # )
        # rx.container(
        # rx.mobile_and_tablet(
        #     rx.hstack(
        #         rx.hstack(
        #             rx.image(
        #                 src="/music-notes-minus-thin.svg",
        #                 width="1.5em",
        #                 height="auto",
        #                 border_radius="25%",
        #             ),
        #             rx.heading("B alright", size="7", weight="bold"),
        #             align_items="center",
        #         ),
        #         rx.menu.root(
        #             rx.menu.trigger(rx.icon("menu", size=30)),
        #             rx.menu.content(
        #                 navbar_link("Home", "/"),
        #                 navbar_link("About", "/About"),
        #                 navbar_link("Gallery", "/Gallery"),
        #                 navbar_link("Contact", "/Contact"),
        #                 rx.menu.item(rx.link(user_login(), create_account=True)),
        #             ),
        #         ),
        #         min_width="100%",
        #         justify="between",
        #         align_items="center",  # Ensure alignment
        #     ),
        # ),
        # top="2px",
        # z_index="5",
        # width="100%",
        # min_width="100%",
        # padding="0px",
        # )
    ),
)
=======
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/music-notes-minus-thin.svg",
                        width="1.5em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading("B alright", size="7", weight="bold"),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(rx.icon("menu", size=30)),
                    rx.menu.content(
                        rx.button("Home", "/"),
                        rx.button("About", "/About"),
                        rx.button("Gallery", "/Gallery"),
                        rx.button("Contact", "/Contact"),
                        # rx.menu.item(rx.link(rx.text("Login"), create_account=True, on_click=user_login)),
                    ),
                ),
                width="100%",
                justify="between",
                align_items="center",  # Ensure alignment
            ),
        ),
        top="2px",
        z_index="5",
        width="100%",
        padding="10px",
    )
>>>>>>> Stashed changes
