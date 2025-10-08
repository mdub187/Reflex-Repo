import reflex as rx

class State(rx.State):
    # Simple list of dictionaries with string URLs
    media: list[dict[str, str]] = [
        {
            "title": "Cat Photo 1",
            "url": "https://www.behance.net/gallery/209581411/Mood",  # String URL
            "type": "image"
        },
        {
            "title": "Cat Video",
            "url": "https://www.behance.net/gallery/215885751/TD-STARS",  # String URL
            "type": "video"
        },
        {
            "title": "Online Image",
            "url": "https://vimeo.com/1124553909",  # String URL
            "type": "image"
        }
    ]

    current_index: int = 0

    def add_media_item(self, title: str, url: str, media_type: str):
        """Add new media item to the list."""
        new_item = {
            "title": title,
            "url": url,  # Still a string
            "type": media_type
        }
        self.media.append(new_item)
