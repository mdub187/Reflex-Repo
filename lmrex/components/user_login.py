# # ./lmrex/components/user_login.py

import reflex as rx

def user_login() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
        rx.container(
        rx.dialog.title("Login"),
        rx.dialog.content(
            rx.text("Enter your credentials below."),
            rx.form(
                rx.input(placeholder="Username"),
                rx.input(placeholder="Password", type="password"),
                rx.button("Login", on_click=rx.redirect("/Account")),
            ),
         rx.dialog.trigger(rx.button("Create Account"),
        ),
        ),
        rx.spacer(column=1),
        ),
    ),
)
