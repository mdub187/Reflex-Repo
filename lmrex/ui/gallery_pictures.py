# lmrex/ui/gallery_pictures.py

from ..imports import rx


def gallery_pictures(self) -> rx.Component:
    """Create a gallery of pictures."""
    return rx.container(gallery_pictures(self))


@rx.var
def has_images(self) -> bool:
    """Check if there are any image items."""
    return self.image_count > 0


@rx.var
def image_count(self) -> int:
    """Count the number of image items."""
    return len([m for m in self.media if m.get("type") == "image"])


@rx.var
def get_images_only(self) -> list[dict[str, str]]:
    """Return only image items."""
    return [m for m in self.media if m.get("type") == "image"]


if __name__ == "__main__":
    print(__name__)
