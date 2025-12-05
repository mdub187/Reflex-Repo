import reflex as rx

from ..routes import routes

account = "login/protected/account"


def account_ui():
    return rx.container(
        rx.text("Account Page"),
        rx.button("Logout", on_click=rx.redirect("/")),
    )
    # return routes.account
