# lmrex/components/login_modal.py
"""
Login modal component.

This component renders a small modal dialog for simulating login in the demo
app. It uses `AuthState.show_login_modal` to control visibility and calls
`AuthState.handle_login_success(..., redirect=True)` to perform a simulated
login and redirect the user to the account page.
"""

from ..imports import rx
from ..state.auth_state import AuthState
from ..state.login_state import LoginState
from ..state.form_state import FormState

# Removed unused import: login (modal uses its own form)
route = "/account/login"


def login() -> rx.Component:
    return rx.vstack(
        rx.form(
            rx.vstack(
                rx.input(placeholder="First Name", name="first_name"),
                rx.input(placeholder="Last Name", name="last_name"),
                rx.hstack(
                    rx.checkbox("Checked", name="check"),
                    rx.switch("Switched", name="switch"),
                ),
                rx.button("Submit", type="submit"),
            ),
            on_submit=FormState.handle_submit,
            reset_on_submit=True,
        ),
        rx.divider(),
        rx.heading("Results"),
        rx.text(FormState.form_data.to_string()),
    )
# def login_modal() -> rx.Component:
#     """A simple login modal with demo login buttons."""
#     return rx.dialog(
#     rx.dialog.root(
#         rx.dialog.content(
#             rx.vstack(
#                 rx.heading("Sign in", size="6"),
#                 rx.text(
#                     "This demo login will simulate an authenticated user and redirect you to your account."
#                 ),
#                 rx.form(
#                     rx.input(
#                         placeholder="Username",
#                         on_change=LoginState.set_username,
#                         value=LoginState.username,
#                     ),
#                     rx.input(
#                         placeholder="Password",
#                         type="password",
#                         on_change=LoginState.set_password,
#                         value=LoginState.password,
#                     ),
#                     rx.hstack(
#                         rx.button(
#                             "Submit",
#                             on_click=LoginState.submit,
#                             disabled=~LoginState.is_valid,
#                             style={"background_color": "#2563eb", "color": "white"},
#                         ),
#                         rx.button(
#                             "Cancel",
#                             on_click=AuthState.close_login_modal,
#                             style={"background_color": "#ef4444", "color": "white"},
#                         ),
#                         spacing="4",
#                     ),
#                 ),
#                 spacing="4",
#                 align="center",
#                 text_align="center",
#             ),
#             style={
#                 "max_width": "560px",
#                 "padding": "1.25rem",
#                 "border_radius": "12px",
#                 "background_color": "white",
#             },
#         ),
#         is_open=AuthState.show_login_modal,
#         z_index="9999",
#     )
# )
# login_modal()
