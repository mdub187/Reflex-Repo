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

    show_dialog: bool = False
    show_modal: bool = False

    def change(self):
        """Toggle the dialog visibility."""
        self.show_dialog = not self.show_dialog

    @rx.event
    def toggle_modal(self):
        """Toggle the modal visibility."""
        print(f"Modal toggled. Current state: {self.show_modal}")
        self.show_modal = not self.show_modal

    media: list[dict[str, str]] = MediaService.get_default_media_items()
    current_index: int = 0
    media_type: str = ""
    media_title: str = ""
    media_url: str = ""

    @rx.var
    def media_count(self) -> int:
        """Get the total number of media items."""
        return len(self.media)

    def previous_item(self):
        """Navigate to the previous item in the carousel."""
        if self.media:
            self.current_index = (self.current_index - 1) % len(self.media)

    def next_item(self):
        """Navigate to the next item in the carousel."""
        if self.media:
            self.current_index = (self.current_index + 1) % len(self.media)

    @rx.var
    def current_media_item(self) -> dict[str, str]:
        """Get the current media item to display."""
        item = MediaService.get_media_item_by_index(self.media, self.current_index)
        return item or MediaService.get_empty_media_item()

    @rx.event
    def add_media_item(self):
        """Add a new media item to the state with default values."""
        new_item = MediaService.create_media_item(
            "New Title", "https://example.com/new_media", "image"
        )
        self.media = self.media + [new_item]
        print("Media added:", new_item)

    def remove_media_item(self, index: int):
        """Remove media item at the specified index."""
        self.media = MediaService.remove_media_item(self.media, index)
        # Adjust current_index to stay within bounds
        self.current_index = min(self.current_index, max(len(self.media) - 1, 0))

    def update_media_item(self, index: int, title: str, url: str, media_type: str):
        """Update media item at the specified index."""
        try:
            self.media = MediaService.update_media_item(
                self.media, index, title, url, media_type
            )
        except ValueError as e:
            print(f"Error updating media item: {e}")

    def remove_current_item(self):
        """Remove the currently displayed media item."""
        if self.media:
            self.remove_media_item(self.current_index)

    def reset_to_defaults(self):
        """Reset media list to default items."""
        self.media = MediaService.get_default_media_items()
        self.current_index = 0

    def clear_all_media(self):
        """Clear all media items."""
        self.media = []
        self.current_index = 0


class FormState(rx.State):
    """State for handling form submission."""

    @rx.event
    def handle_submit(self):
        """Handle form submissions."""
        new_item = MediaService.create_media_item(
            self.media_title, self.media_url, self.media_type
        )
        self.media = self.media + [new_item]
        print("Media added:", new_item)
        # Reset form inputs
        self.media_type = ""
        self.media_title = ""
        self.media_url = ""


if __name__ == "__main__":
    print(State())
