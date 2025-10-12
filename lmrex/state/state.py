import reflex as rx
from ..models.user_model import User1, NewUser
from ..models.media_model import MediaService

class State(rx.State):
    """The app state."""

    label: str = ""
    label_arr: list[str] = ["We", "Gonna", "Be", "Alright"]

    # for label in label_arr:
    #     print(label)

    def change_label(self):
        if self.label == self.label_arr[0]:
            # self.label = self.label_arr[1 + 0]
            self.label = self.label_arr[1 + 0]
        elif self.label == self.label_arr[1]:
            self.label = self.label_arr[2 + 0]
        elif self.label == self.label_arr[2]:
            self.label = self.label_arr[3 + 0]
        elif self.label == self.label_arr[3]:
            self.label = self.label_arr[0]
        else:
            self.label = self.label_arr[0]

    def handle_input_change(self, value: str):
        self.label = value

    show_dialog: bool = False

    def change(self):
        """Toggle the dialog on and off."""
        self.show_dialog = not self.show_dialog

    # Media carousel state with external URLs
    media: list[dict[str, str]] = MediaService.get_default_media_items()

    current_index: int = 0

    @rx.var
    def media_count(self) -> int:
        """Get the total number of media items."""
        return MediaService.get_media_count(self.media)

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
        media_item = MediaService.get_media_item_by_index(self.media, self.current_index)
        return media_item if media_item else MediaService.get_empty_media_item()

    def add_media_item(self, title: str, url: str, media_type: str):
        """Add new media item to the list."""
        try:
            self.media = MediaService.add_media_item(self.media, title, url, media_type)
        except ValueError as e:
            print(f"Error adding media item: {e}")

    def remove_media_item(self, index: int):
        """Remove media item at the specified index."""
        self.media = MediaService.remove_media_item(self.media, index)
        # Adjust current_index if necessary
        if self.current_index >= len(self.media) and len(self.media) > 0:
            self.current_index = len(self.media) - 1
        elif len(self.media) == 0:
            self.current_index = 0

    def update_media_item(self, index: int, title: str, url: str, media_type: str):
        """Update media item at the specified index."""
        try:
            self.media = MediaService.update_media_item(self.media, index, title, url, media_type)
        except ValueError as e:
            print(f"Error updating media item: {e}")

    def remove_current_item(self):
        """Remove the currently displayed media item."""
        if len(self.media) > 0:
            self.remove_media_item(self.current_index)

    def duplicate_current_item(self):
        """Duplicate the currently displayed media item."""
        if len(self.media) > 0:
            current_item = self.current_media_item
            self.add_media_item(
                title=f"{current_item['title']} (Copy)",
                url=current_item['url'],
                media_type=current_item['type']
            )

    def reset_to_defaults(self):
        """Reset media list to default items."""
        self.media = MediaService.get_default_media_items()
        self.current_index = 0

    def clear_all_media(self):
        """Clear all media items."""
        self.media = []
        self.current_index = 0

    @rx.var
    def image_count(self) -> int:
        """Get the number of image items."""
        return len([item for item in self.media if item.get("type") == "image"])

    @rx.var
    def video_count(self) -> int:
        """Get the number of video items."""
        return len([item for item in self.media if item.get("type") == "video"])

    @rx.var
    def has_images(self) -> bool:
        """Check if there are any image items."""
        return self.image_count > 0

    @rx.var
    def has_videos(self) -> bool:
        """Check if there are any video items."""
        return self.video_count > 0

    @rx.var
    def get_images_only(self) -> list[dict[str, str]]:
        """Get only the image items."""
        return [item for item in self.media if item.get("type") == "image"]

    @rx.var
    def get_videos_only(self) -> list[dict[str, str]]:
        """Get only the video items."""
        return [item for item in self.media if item.get("type") == "video"]

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
