# ./state/state.py

import reflex as rx
from ..models.user_model import User1, NewUser
from ..models.media_model import MediaService


class State(rx.State):
    """Global app state controller."""

    # ─────────────────────────────
    # Basic Label Management
    # ─────────────────────────────
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

    # ─────────────────────────────
    # Dialog + Modal Control
    # ─────────────────────────────
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

    # ─────────────────────────────
    # Media Carousel State
    # ─────────────────────────────
    media: list[dict[str, str]] = MediaService.get_default_media_items()
    current_index: int = 0

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

    def add_media_item(self, title: str, url: str, media_type: str):
        """Add new media item to the list."""
        try:
            new_item = MediaService.create_media_item(title, url, media_type)
            self.media = self.media + [new_item]
        except ValueError as e:
            print(f"Error adding media item: {e}")

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

    def duplicate_current_item(self):
        """Duplicate the currently displayed media item."""
        if self.media:
            item = self.current_media_item
            self.add_media_item(
                title=f"{item['title']} (Copy)",
                url=item["url"],
                media_type=item["type"],
            )

    def reset_to_defaults(self):
        """Reset media list to default items."""
        self.media = MediaService.get_default_media_items()
        self.current_index = 0

    def clear_all_media(self):
        """Clear all media items."""
        self.media = []
        self.current_index = 0

    # ─────────────────────────────
    # Media Filters
    # ─────────────────────────────
    # @rx.var
    # def image_count(self) -> int:
    #     """Count the number of image items."""
    #     return len([m for m in self.media if m.get("type") == "image"])

    # @rx.var
    # def video_count(self) -> int:
    #     """Count the number of video items."""
    #     return len([m for m in self.media if m.get("type") == "video"])

    # @rx.var
    # def has_images(self) -> bool:
    #     """Check if there are any image items."""
    #     return self.image_count > 0

    # @rx.var
    # def has_videos(self) -> bool:
    #     """Check if there are any video items."""
    #     return self.video_count > 0

    # @rx.var
    # def get_images_only(self) -> list[dict[str, str]]:
    #     """Return only image items."""
    #     return [m for m in self.media if m.get("type") == "image"]

    # @rx.var
    # def get_videos_only(self) -> list[dict[str, str]]:
    #     """Return only video items."""
    #     return [m for m in self.media if m.get("type") == "video"]


class FormState(rx.State):
    """State for handling form submission."""

    @rx.event
    def handle_submit(self, form_data: dict):
        """Handle form submissions."""
        print(f"Form submitted with data: {form_data}")
