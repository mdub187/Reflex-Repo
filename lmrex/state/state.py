# ./state/state.py

import reflex as rx

# from ..models.user_model import User1, NewUser
from lmrex.models.media_model import MediaService


class State(rx.State):
    """Global app state controller."""

    label: str = ""
    label_arr: list[str] = ["We", "Gonna", "Be", "Alright"]

    def change_label(self):
        """Cycle through the label array."""
        if not self.label or self.label not in self.label_arr:
            self.label = self.label_arr[0]
        else:
            current_index = self.label_arr.index(self.label)
            next_index = (current_index + 1) % len(self.label_arr)
            self.label = self.label_arr[next_index]

    def handle_input_change(self, value: str):
        """Update label based on user input."""
        self.label = value.strip()

    def change(self):
            """Toggle the dialog visibility."""
            self.show_dialog = not self.show_dialog

    def toggle_modal(self):
            """Toggle the modal visibility."""
            print(f"Modal toggled. Current state: {self.show_modal}")
            self.show_modal = not self.show_modal

    class FormState(rx.State):
        """State for handling form submission."""

        email: str = ""
        password: str = ""

        def set_email(self, value: str):
            self.email = value

        def set_password(self, value: str):
            self.password = value

        @rx.event
        def handle_submit(self, form_data: dict):
            """Handle form submissions."""
            print(f"Form submitted with data: {form_data}")

    def handle_login(self):
        """Handle user login."""
        # Add authentication logic here
        print("Login button clicked!")
