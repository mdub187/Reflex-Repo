import reflex as rx
from typing import List
from lmrex.models.media_model import MediaService

class MediaState(rx.State):
    media: List[dict[str, str]] = MediaService.get_default_media_items()
    current_index: int = 0



    @rx.var
    def current_media_item(self) -> dict[str, str]:
        """Get the current media item to display."""
        item = MediaService.get_media_item_by_index(self.media, self.current_index)
        return item or MediaService.get_empty_media_item()

    def next_item(self):
        """Navigate to the next item in the carousel."""
        if self.media:
            self.current_index = (self.current_index + 1) % len(self.media)

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
