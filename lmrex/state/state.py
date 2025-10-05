# lmrex/state/state.py

import reflex as rx
# from .state import AuthState


class State(rx.State):
    """The app state."""

    label: str = ""
    label_arr: list[str] = ["Be", "Alright"]

    def change_label(self):
        if self.label == self.label_arr[0]:
            self.label = self.label_arr[1]
        else:
            self.label = self.label_arr[0]

    def handle_input_change(self, value: str):
        self.label = value

    show_dialog: bool = False

    def change(self):
        """Toggle the dialog on and off."""
        self.show_dialog = not self.show_dialog


class FormState(rx.State):
        @rx.event
        def handle_submit(self, form_data: dict):
            """Handle the form submit."""
            self.form_data = form_data
