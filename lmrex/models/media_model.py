# ./models/media_model.py

"""Media service for managing media data and operations."""

from typing import List, Dict, Optional, Tuple


class MediaService:
    """Service class for managing media items."""

    # Default media items
    DEFAULT_MEDIA_ITEMS: List[Dict[str, str]] = [
        {
            "title": "Panama Rose",
            "url": "https://mir-s3-cdn-cf.behance.net/project_modules/1400_webp/230b6e209581411.6778b1b7b0b77.jpeg",
            "type": "image",
        },
        {
            "title": "~OM~",
            "url": "https://mir-s3-cdn-cf.behance.net/project_modules/1400_webp/09397a148430145.62d5a256db3d1.jpg",
            "type": "image",
        },
        {
            "title": "Swirls",
            "url": "https://player.vimeo.com/video/1127068081?",
            "type": "video",
        },
    ]

    VALID_MEDIA_TYPES = ["image", "video"]

    @staticmethod
    def get_default_media_items() -> List[Dict[str, str]]:
        """Get a copy of the default media items."""
        return MediaService.DEFAULT_MEDIA_ITEMS.copy()

    @staticmethod
    def create_media_item(title: str, url: str, media_type: str) -> Dict[str, str]:
        """Create a new media item dictionary."""
        if not MediaService.is_valid_media_type(media_type):
            raise ValueError(f"Invalid media type: {media_type}")

        return {"title": title.strip(), "url": url.strip(), "type": media_type.lower()}

    @staticmethod
    def add_media_item(
        media_list: List[Dict[str, str]], title: str, url: str, media_type: str
    ) -> List[Dict[str, str]]:
        """Add a new media item to the list."""
        new_item = MediaService.create_media_item(title, url, media_type)
        return media_list + [new_item]

    @staticmethod
    def remove_media_item(
        media_list: List[Dict[str, str]], index: int
    ) -> List[Dict[str, str]]:
        """Remove a media item at the specified index."""
        if 0 <= index < len(media_list):
            return media_list[:index] + media_list[index + 1 :]
        return media_list

    @staticmethod
    def update_media_item(
        media_list: List[Dict[str, str]],
        index: int,
        title: str,
        url: str,
        media_type: str,
    ) -> List[Dict[str, str]]:
        """Update a media item at the specified index."""
        if not (0 <= index < len(media_list)):
            return media_list

        updated_item = MediaService.create_media_item(title, url, media_type)
        new_list = media_list.copy()
        new_list[index] = updated_item
        return new_list

    @staticmethod
    def get_media_count(media_list: List[Dict[str, str]]) -> int:
        """Get the total number of media items."""
        return len(media_list)

    @staticmethod
    def is_valid_media_type(media_type: str) -> bool:
        """Check if the media type is valid."""
        return media_type.lower() in MediaService.VALID_MEDIA_TYPES

    @staticmethod
    def get_media_item_by_index(
        media_list: List[Dict[str, str]], index: int
    ) -> Optional[Dict[str, str]]:
        """Get a media item by index, returns None if index is invalid."""
        if 0 <= index < len(media_list):
            return media_list[index]
        return None

    @staticmethod
    def find_media_items_by_type(
        media_list: List[Dict[str, str]], media_type: str
    ) -> List[Dict[str, str]]:
        """Find all media items of a specific type."""
        return [
            item
            for item in media_list
            if item.get("type", "").lower() == media_type.lower()
        ]

    @staticmethod
    def validate_media_item(item: Dict[str, str]) -> Tuple[bool, str]:
        """Validate a media item dictionary. Returns (is_valid, error_message)."""
        if not isinstance(item, dict):
            return False, "Media item must be a dictionary"

        required_fields = ["title", "url", "type"]
        for field in required_fields:
            if field not in item:
                return False, f"Missing required field: {field}"
            if not isinstance(item[field], str) or not item[field].strip():
                return False, f"Field '{field}' must be a non-empty string"

        if not MediaService.is_valid_media_type(item["type"]):
            return False, f"Invalid media type: {item['type']}"

        return True, ""

    @staticmethod
    def get_empty_media_item() -> Dict[str, str]:
        """Get an empty media item structure."""
        return {"title": "", "url": "", "type": "image"}


# Convenience functions for backwards compatibility
def get_media_items() -> List[Dict[str, str]]:
    """Get default media items."""
    return MediaService.get_default_media_items()


def add_media_item(
    media_list: List[Dict[str, str]], title: str, url: str, media_type: str
) -> List[Dict[str, str]]:
    """Add a new media item to the list."""
    return MediaService.add_media_item(media_list, title, url, media_type)


def get_media_count(media_list: List[Dict[str, str]]) -> int:
    """Get the total number of media items."""
    return MediaService.get_media_count(media_list)


def is_valid_media_type(media_type: str) -> bool:
    """Check if the media type is valid."""
    return MediaService.is_valid_media_type(media_type)
