import reflex as rx
from ..models.user_model import User, NewUser
from ..models.media_model import MediaService
from ..logic.auth import get_user_from_token, UserInfo


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

    # Thumbnail pagination config for carousel (thumbnail navigation settings)
    thumbnails_per_page: int = 5
    thumbnail_page: int = 0

    @rx.var
    def media_count(self) -> int:
        """Get the total number of media items."""
        return MediaService.get_media_count(self.media)

    @rx.event
    def previous_item(self):
        """Navigate to the previous item in the carousel (event)."""
        if len(self.media) > 0:
            self.current_index = (self.current_index - 1) % len(self.media)
            # Ensure the current item is visible in the thumbnail pager
            self.thumbnail_page = self.current_index // self.thumbnails_per_page

    @rx.event
    def next_item(self):
        """Navigate to the next item in the carousel (event)."""
        if len(self.media) > 0:
            self.current_index = (self.current_index + 1) % len(self.media)
            # Ensure the current item is visible in the thumbnail pager
            self.thumbnail_page = self.current_index // self.thumbnails_per_page

    @rx.var
    def current_media_item(self) -> dict[str, str]:
        """Get the current media item to display."""
        media_item = MediaService.get_media_item_by_index(
            self.media, self.current_index
        )
        return media_item if media_item else MediaService.get_empty_media_item()

    @rx.var
    def current_media_type(self) -> str:
        """Get the type of the current media item."""
        return self.current_media_item.get("type", "image")

    @rx.var
    def current_media_url(self) -> str:
        """Get the URL of the current media item."""
        return self.current_media_item.get("url", "")

    @rx.var
    def current_media_title(self) -> str:
        """Get the title of the current media item."""
        return self.current_media_item.get("title", "")

    @rx.event
    def add_media_item(self, title: str, url: str, media_type: str):
        """Add new media item to the list (event)."""
        try:
            self.media = MediaService.add_media_item(self.media, title, url, media_type)
            # Move to the newly added item and make it visible in thumbnails
            self.current_index = len(self.media) - 1
            self.thumbnail_page = self.current_index // self.thumbnails_per_page
        except ValueError as e:
            print(f"Error adding media item: {e}")

    @rx.event
    def remove_media_item(self, index: int):
        """Remove media item at the specified index (event)."""
        self.media = MediaService.remove_media_item(self.media, index)
        # Adjust current_index if necessary
        if self.current_index >= len(self.media) and len(self.media) > 0:
            self.current_index = len(self.media) - 1
        elif len(self.media) == 0:
            self.current_index = 0
        # Ensure thumbnail page is within bounds
        if len(self.media) > 0:
            max_page = (len(self.media) - 1) // self.thumbnails_per_page
            if self.thumbnail_page > max_page:
                self.thumbnail_page = max_page
        else:
            self.thumbnail_page = 0

    @rx.event
    def update_media_item(self, index: int, title: str, url: str, media_type: str):
        """Update media item at the specified index (event)."""
        try:
            self.media = MediaService.update_media_item(
                self.media, index, title, url, media_type
            )
        except ValueError as e:
            print(f"Error updating media item: {e}")

    @rx.event
    def remove_current_item(self):
        """Remove the currently displayed media item (event)."""
        if len(self.media) > 0:
            self.remove_media_item(self.current_index)

    @rx.event
    def duplicate_current_item(self):
        """Duplicate the currently displayed media item (event)."""
        if len(self.media) > 0:
            current_item = self.current_media_item
            self.add_media_item(
                title=f"{current_item['title']} (Copy)",
                url=current_item["url"],
                media_type=current_item["type"],
            )

    @rx.event
    def reset_to_defaults(self):
        """Reset media list to default items (event)."""
        self.media = MediaService.get_default_media_items()
        self.current_index = 0
        self.thumbnail_page = 0

    @rx.event
    def clear_all_media(self):
        """Clear all media items (event)."""
        self.media = []
        self.current_index = 0
        self.thumbnail_page = 0

    @rx.var
    def total_thumbnail_pages(self) -> int:
        """Total number of thumbnail pages."""
        if len(self.media) == 0:
            return 0
        return (
            len(self.media) + self.thumbnails_per_page - 1
        ) // self.thumbnails_per_page

    @rx.var
    def visible_thumbnails(self) -> list[dict[str, str]]:
        """Return the list of thumbnails for the current thumbnail page."""
        if len(self.media) == 0:
            return []
        start = self.thumbnail_page * self.thumbnails_per_page
        end = start + self.thumbnails_per_page
        return self.media[start:end]

    def get_media_item_url(self, item: dict[str, str]) -> str:
        """Get the URL of a media item."""
        return item.get("url", "")

    def get_media_item_type(self, item: dict[str, str]) -> str:
        """Get the type of a media item."""
        return item.get("type", "image")

    def get_visible_thumbnail_index(self, item: dict[str, str]) -> int:
        """Get the index of an item in the visible thumbnails."""
        try:
            return self.visible_thumbnails.index(item)
        except ValueError:
            return -1

    @rx.var
    def active_thumbnail_index(self) -> int:
        """Index of the active thumbnail within the current visible set."""
        return self.current_index - (self.thumbnail_page * self.thumbnails_per_page)

    @rx.event
    def next_thumbnail_page(self):
        """Advance to the next thumbnail page if available."""
        if self.thumbnail_page < max(0, self.total_thumbnail_pages - 1):
            self.thumbnail_page += 1

    @rx.event
    def previous_thumbnail_page(self):
        """Go back to the previous thumbnail page if available."""
        if self.thumbnail_page > 0:
            self.thumbnail_page -= 1

    @rx.event
    def jump_to_index(self, index: int):
        """Jump to a specific index in the carousel and move thumbnails accordingly."""
        if 0 <= index < len(self.media):
            self.current_index = index
            self.thumbnail_page = index // self.thumbnails_per_page

    @rx.event
    def set_current_index_by_item(self, item: dict[str, str]):
        """Set the current index based on the provided media item.

        This helper is useful for UI callbacks that receive an item and need to
        make it the current carousel item. It first tries to find the exact
        dict in the media list; if not found, it falls back to matching by URL.
        """
        if not item or not isinstance(item, dict):
            return

        # Try to find the exact item object in the media list
        try:
            idx = self.media.index(item)
            self.jump_to_index(idx)
            return
        except ValueError:
            pass

        # Fallback: match by unique URL if present
        url = item.get("url")
        if url:
            for i, m in enumerate(self.media):
                if m.get("url") == url:
                    self.jump_to_index(i)
                    return

        # If no match found, do nothing (safe no-op)
        return

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


class AuthState(rx.State):
    auth_token: str = rx.LocalStorage(str)
    login_error_message: str = ""

    def handle_login_success(self, token: str):
        # The token is returned by your login API.
        self.auth_token = token
        self.login_error_message = ""
        # Redirect to a protected page after login.
        return rx.redirect("/protected/account")

    @rx.var
    def authenticated_user(self) -> UserInfo | None:
        """Get the authenticated user, or None if not logged in."""
        token = self.auth_token
        if not token:
            return None
        else:
            # Validate the token using the centralized auth helper and return a
            # normalized `UserInfo` object (or None if verification fails).
            user_info = get_user_from_token(token)
            return user_info
            return token

    def clear_auth_token(self):
        self.auth_token = ""
        self.login_error_message = ""
        return rx.redirect("/login")

    def clear_auth_token_and_redirect(self):
        self.clear_auth_token()
        return rx.redirect("/login")
