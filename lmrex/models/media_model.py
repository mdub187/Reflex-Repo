# .lmrex/models/media_model.py
#
"""Media service for managing media data and operations."""

from typing import Dict, List, Optional, Tuple


class MediaService:
    """Service class for managing media items."""

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
        {
            "title": "Test_Audio",
            "url": "https://on.soundcloud.com/LSgMc7ip5ZocgIF431",
            "type": "audio",
        },
    ]

    VALID_MEDIA_TYPES = ["image", "video", "audio", "text"]

    # ─────────────────────────────
    # Retrieval Methods
    # ─────────────────────────────
    @staticmethod
    def get_default_media_items() -> List[Dict[str, str]]:
        """Return a copy of the default media items."""
        return MediaService.DEFAULT_MEDIA_ITEMS.copy()

    @staticmethod
    def get_media_count(media_list: List[Dict[str, str]]) -> int:
        """Return the total number of media items."""
        return len(media_list)

    @staticmethod
    def get_media_item_by_index(
        media_list: List[Dict[str, str]], index: int
    ) -> Optional[Dict[str, str]]:
        """Return a media item by index. Returns None if index is invalid."""
        if 0 <= index < len(media_list):
            return media_list[index]
        return None

    @staticmethod
    def get_empty_media_item() -> Dict[str, str]:
        """Return an empty media item structure."""
        return {"title": "", "url": "", "type": "image"}

    # ─────────────────────────────
    # Creation / Mutation Methods
    # ─────────────────────────────
    @staticmethod
    def is_valid_media_type(media_type: str) -> bool:
        """Check if the media type is valid."""
        return media_type.lower() in MediaService.VALID_MEDIA_TYPES

    @staticmethod
    def create_media_item(title: str, url: str, media_type: str) -> Dict[str, str]:
        """Create a new media item dictionary."""
        if not MediaService.is_valid_media_type(media_type):
            raise ValueError(f"Invalid media type: {media_type}")
        return {"title": title.strip(), "url": url.strip(), "type": media_type.lower()}

    @staticmethod
    def add_media(
        media_list: List[Dict[str, str]], title: str, url: str, media_type: str
    ) -> List[Dict[str, str]]:
        """Add a new media item to the list."""
        new_item = MediaService.create_media_item(title, url, media_type)
        return media_list + [new_item]
        media_list.append(new_item)

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


if __name__ == "__main__":
    print(__name__)
