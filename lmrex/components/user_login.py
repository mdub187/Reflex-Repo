# ./lmrex/components/user_login.py
import reflex as rx

def user_login() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(rx.button("Login")),
        rx.dialog.content(
            rx.heading("Sign In", size="6"),
            rx.text("Enter your credentials below."),
            rx.input(placeholder="Username"),
            rx.input(placeholder="Password", type="password"),
            rx.dialog.close(rx.button("Submit")),
            rx.spacer(column=1),
            rx.dialog.trigger(rx.button("Create Account"))

        ),
    )
