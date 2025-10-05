import reflex as rx
from ..state.state import FormState

def form_data(self, state: FormState):
    return rx.form.root(
            rx.flex(
                rx.form.field.root(
                    rx.form.field.label("Email"),
                    rx.form.field.input(placeholder="Enter your email", type="email"),
                    name="email",
                    required=True,
                ),
                rx.form.field.root(
                    rx.form.field.label("Password"),
                    rx.form.field.input(placeholder="Enter your password", type="password"),
                    name="password",
                    required=True,
                ),
                rx.flex(
                    rx.dialog.close(
                        rx.button(
                            "Cancel",
                            variant="soft",
                            color_scheme="gray",
                            on_click=State.change,
                        )
                    ),
                    rx.dialog.close(
                        rx.button("Log In", type="submit"),
                    ),
                    justify="end",
                    spacing="2",
                    margin_top="16px",
                ),
                direction="column",
                spacing="3",
            ),
            on_submit=lambda: rx.window_alert("Login submitted (not implemented)"),
            reset_on_submit=True,
        )
