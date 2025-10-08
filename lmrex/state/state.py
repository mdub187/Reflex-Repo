import reflex as rx
from ..models.user_model import User1, NewUser, Gallery

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

    # Media carousel state with external URLs
    media: list[dict[str, str]] = [
        {
            "type": "image", 
            "src": "https://picsum.photos/600/400?random=1", 
            "title": "Random Photo 1"
        },
        {
            "type": "video", 
            "src": "https://www.youtube.com/embed/dQw4w9WgXcQ", 
            "title": "Rick Roll (YouTube)"
        },
        {
            "type": "image", 
            "src": "https://picsum.photos/600/400?random=2", 
            "title": "Random Photo 2"
        },
        {
            "type": "video", 
            "src": "https://www.youtube.com/embed/jNQXAC9IVRw", 
            "title": "Me at the zoo (First YouTube video)"
        },
        {
            "type": "image", 
            "src": "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=600&h=400&fit=crop", 
            "title": "Unsplash Mountain"
        }
    ]
    current_index: int = 0

    def previous_item(self):
        """Navigate to the previous item in the carousel."""
        if len(self.media) > 0:
            self.current_index = (self.current_index - 1) % len(self.media)

    def next_item(self):
        """Navigate to the next item in the carousel."""
        if len(self.media) > 0:
            self.current_index = (self.current_index + 1) % len(self.media)

    @rx.var
    def current_media_item(self) -> dict[str, str]:
        """Get the current media item to display."""
        if len(self.media) > 0:
            return self.media[self.current_index]
        return {"type": "image", "src": ""}

    show_modal: bool = False

    @rx.event
    def toggle_modal(self):
        print("togly")
        print(f"Modal visibility toggled. Current state: {self.show_modal}")
        self.show_modal = not self.show_modal

class FormState(rx.State):
    @rx.event
    def handle_submit(self, form_data):
        """Handle the form submit."""
        print(f"Form submitted with data: {form_data}")
