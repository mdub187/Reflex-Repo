import reflex as rx


def account():
    return rx.box(
        rx.text("Account Page"),
        rx.button("Logout", on_click=rx.redirect("/index")),
    )
    return account
