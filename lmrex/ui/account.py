import reflex as rx

from ..routes import routes


def account_ui():
    return rx.box(
        # account_ui(),
        rx.text("Account Page"),
        rx.button("Logout", on_click=rx.redirect("/")),
    )
    return routes.account
