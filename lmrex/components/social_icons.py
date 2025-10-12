import reflex as rx
from typing import Dict, List, Optional

# Icon mapping - paths relative to assets directory
ICON_MAP = {
    "behance": "social_icons/behance.png",
    "dropbox": "social_icons/dropbox.png",
    "facebook": "social_icons/facebook.png",
    "github": "social_icons/github.png",
    "instagram": "social_icons/instagram.png",
    "linkedin": "social_icons/linkedin.png",
    "reddit": "social_icons/reddit.png",
    "soundcloud": "social_icons/soundcloud.png",
    "spotify": "social_icons/spotify.png",
    "twitch": "social_icons/twitch.png",
    "vimeo": "social_icons/vimeo.png",
    "whatsapp": "social_icons/whatsapp.png",
    "youtube": "social_icons/youtube.png",
    "music-notes": "music-notes-minus-thin.svg",
}

def social_icons(
    icons: Optional[Dict[str, str]] = None,
    urls: Optional[Dict[str, str]] = None,
    size: str = "24px",
    spacing: str = "4",
    include_platforms: Optional[List[str]] = None,
    exclude_platforms: Optional[List[str]] = None
) -> rx.Component:
    """
    Create a horizontal stack of social media icons.

    Args:
        icons: Custom icon mapping (platform -> icon_path)
        urls: URL mapping (platform -> social_media_url)
        size: Icon size (default: "24px")
        spacing: Space between icons (default: "4")
        include_platforms: Only include these platforms
        exclude_platforms: Exclude these platforms
    """
    # Use provided icons or default to ICON_MAP
    icon_data = icons or ICON_MAP.copy()

    # Default URLs (replace with your actual social media URLs)
    default_urls = {
        "behance": "https://behance.net/lmrex",
        "facebook": "https://facebook.com/lmrex",
        "github": "https://github.com/lmrex",
        "instagram": "https://instagram.com/lmrex",
        "linkedin": "https://linkedin.com/in/lmrex",
        "reddit": "https://reddit.com/u/lmrex",
        "soundcloud": "https://soundcloud.com/lmrex",
        "spotify": "https://spotify.com/lmrex",
        "twitch": "https://twitch.tv/lmrex",
        "vimeo": "https://vimeo.com/lmrex",
        "whatsapp": "https://wa.me/1234567890",
        "youtube": "https://youtube.com/@lmrex",
        "dropbox": "https://dropbox.com/lmrex",
    }

    # Use provided URLs or defaults
    social_urls = urls or default_urls

    # Filter platforms
    platforms_to_show = set(icon_data.keys())

    # Always exclude non-social icons
    if exclude_platforms is None:
        exclude_platforms = ["music-notes"]
    else:
        exclude_platforms = list(exclude_platforms) + ["music-notes"]

    if include_platforms:
        platforms_to_show &= set(include_platforms)

    if exclude_platforms:
        platforms_to_show -= set(exclude_platforms)

    # Create icon components
    icon_components = []
    for platform in sorted(platforms_to_show):
        if platform in icon_data:
            icon_path = icon_data[platform]
            social_url = social_urls.get(platform, "#")

            icon_components.append(
                rx.link(
                    rx.image(
                        src=f"/{icon_path}",
                        alt=f"{platform.capitalize()} icon",
                        width=size,
                        height=size,
                        _hover={
                            "opacity": 0.7,
                            "transform": "scale(1.1)",
                            "transition": "all 0.2s ease"
                        }
                    ),
                    href=social_url,
                    is_external=True,
                    _hover={"text_decoration": "none"}
                )
            )

    return rx.hstack(
        *icon_components,
        spacing=spacing,
        align="center"
    )

def social_icons_simple() -> rx.Component:
    """Simple version with default settings."""
    return social_icons()

def social_icons_large() -> rx.Component:
    """Large version of social icons."""
    return social_icons(size="32px", spacing="6")

def social_icons_minimal(platforms: List[str]) -> rx.Component:
    """Minimal version with only specified platforms."""
    return social_icons(include_platforms=platforms)

# Export the ICON_MAP for use in other components
social_icons_data = ICON_MAP

# Easy configuration - replace with your actual URLs
SOCIAL_CONFIG = {
    "github": "https://github.com/mdub187",
    "linkedin": "https://www.linkedin.com/in/marc-weeks91/",
    "youtube": "https://www.youtube.com/bottleofabsinth1",
    "instagram": "https://instagram.com/yourusername",
    "facebook": "https://facebook.com/yourusername",
    "reddit": "https://reddit.com/u/yourusername",
    "behance": "https://www.behance.net/marcweeks",
    "soundcloud": "https://soundcloud.com/marc-weeks"
}

def social_icons_configured() -> rx.Component:
    """Social icons using the configured URLs above."""
    return social_icons(
        urls=SOCIAL_CONFIG,
        include_platforms=list(SOCIAL_CONFIG.keys()),
        size="20px",
        spacing="3"
    )

def social_icons_footer() -> rx.Component:
    """Footer-sized social icons with common platforms."""
    return social_icons(
        urls=SOCIAL_CONFIG,
        include_platforms=["github", "linkedin", "youtube", "soundcloud", "behance"],
        size="18px",
        spacing="3"
    )

def social_icons_hero() -> rx.Component:
    """Large social icons for hero sections."""
    return social_icons(
        urls=SOCIAL_CONFIG,
        include_platforms=["github", "linkedin", "youtube", "behance", "soundlcoud"],
        size="32px",
        spacing="6"
    )
