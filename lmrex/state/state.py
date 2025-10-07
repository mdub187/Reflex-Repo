# lmrex/state/state.py

import reflex as rx
# from .state import AuthState
from ..models.user_model import User1, NewUser

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

    # media = [
    #         {"type": "image", "src": "/cat1.jpg"},
    #         {"type": "video", "src": "/cat_video.mp4"},
    #         {"type": "image", "src": "/cat2.jpg"},
    #         {"type": "video", "src": "/cat_video2.mp4"},
    #     ]
    show_modal: bool = False

    @rx.event
    def toggle_modal(self):
        print("togly")
        print(f"Modal visibility toggled. Current state: {self.show_modal}")
        self.show_modal = not self.show_modal
        # class User1(rx.Model, table=True, extend_existing=True):
        class User2(rx.Model, extend_existing=True):
                current_user: dict[str, str] = {}

                def add_user(self, user_data: dict[str, str]):
                    """Add a new user to the database."""
                    self.current_user = user_data

                    # with rx.session() as session:
                    #     existing_user = session.exec(
                    #         User2(User2.email == self.current_user["email"])
                    #     ).first()


        #     f"User {self.current_user['name']} has been added.",
        # position="bottom-right",
        # # rx.cond(toggle_modal),
        #         self.add_user(User1(**self.current_user))

class FormState(rx.State):
        @rx.event
        def handle_submit(self, state):
            """Handle the form submit."""
            self.handle_submit
