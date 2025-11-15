# lmrex/ui/gallery_video.py

from ..imports import rx


@rx.var
def video_count(self) -> int:
    """Count the number of video items."""
    return len([m for m in self.media if m.get("type") == "video"])


@rx.var
def has_videos(self) -> bool:
    """Check if there are any video items."""
    return self.video_count > 0


@rx.var
def get_videos_only(self) -> list[dict[str, str]]:
    """Return only video items."""
    return [m for m in self.media if m.get("type") == "video"]
