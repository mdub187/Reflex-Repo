# Social Icons Configuration Guide

This guide explains how to customize the social media icons in your Reflex application.

## Quick Setup

### 1. Update Your Social Media URLs

Edit the `SOCIAL_CONFIG` dictionary in `social_icons.py`:

```python
SOCIAL_CONFIG = {
    "github": "https://github.com/yourusername",
    "linkedin": "https://linkedin.com/in/yourusername",
    "youtube": "https://youtube.com/@yourusername",
    "instagram": "https://instagram.com/yourusername",
    "facebook": "https://facebook.com/yourusername",
    "reddit": "https://reddit.com/u/yourusername"
}
```

Replace `yourusername` with your actual usernames for each platform.

## Available Social Platforms

The following social media platforms are supported with icons:

- **behance** - Behance portfolio
- **dropbox** - Dropbox file sharing
- **facebook** - Facebook profile/page
- **github** - GitHub repositories
- **instagram** - Instagram profile
- **linkedin** - LinkedIn profile
- **reddit** - Reddit user profile
- **soundcloud** - SoundCloud music
- **spotify** - Spotify music
- **twitch** - Twitch streaming
- **vimeo** - Vimeo videos
- **whatsapp** - WhatsApp contact
- **youtube** - YouTube channel

## Usage Examples

### Footer Icons (Default)

```python

from lmrex.components.social_icons import social_icons_footer

# Uses configured URLs with common platforms (github, linkedin, youtube)
social_icons_footer()
```

### Custom Platform Selection

```python

from lmrex.components.social_icons import social_icons

# Only show specific platforms
social_icons(
    include_platforms=["github", "instagram", "youtube", "linkedin"],
    size="24px",
    spacing="4"
)
```

### Custom URLs

```python

from lmrex.components.social_icons import social_icons

my_urls = {
    "github": "https://github.com/mycompany",
    "linkedin": "https://linkedin.com/company/mycompany"
}

social_icons(urls=my_urls, include_platforms=["github", "linkedin"])

```

### Large Icons for Hero Section

```python

from lmrex.components.social_icons import social_icons_hero

# Large icons with more spacing
social_icons_hero()

```

## Customization Options

### Size Options

- `"16px"` - Small icons
- `"20px"` - Default footer size
- `"24px"` - Medium icons
- `"32px"` - Large icons
- `"48px"` - Extra large icons

### Spacing Options

- `"2"` - Tight spacing
- `"3"` - Default spacing
- `"4"` - Medium spacing
- `"6"` - Large spacing

### Platform Filtering

```python

# Include only specific platforms
social_icons(include_platforms=["github", "linkedin", "youtube"])

# Exclude specific platforms
social_icons(exclude_platforms=["whatsapp", "reddit"])

```

## Complete Example

```python

def my_custom_social_footer() -> rx.Component:
    """Custom footer with social icons."""
    my_social_urls = {
        "github": "https://github.com/myusername",
        "linkedin": "https://linkedin.com/in/myprofile",
        "youtube": "https://youtube.com/@mychannel",
        "instagram": "https://instagram.com/myhandle"
    }

    return rx.container(
        rx.hstack(
            rx.text("Follow us:", size="3", weight="bold"),
            social_icons(
                urls=my_social_urls,
                include_platforms=["github", "linkedin", "youtube", "instagram"],
                size="24px",
                spacing="4"
            ),
            spacing="6",
            align="center",
            justify="center"
        ),
        padding="4"
    )

```

## Adding New Icons

To add new social media icons:

1. Add the PNG icon file to `assets/social_icons/`
2. Update the `ICON_MAP` dictionary in `social_icons.py`:

```python

ICON_MAP = {
    # ... existing icons ...
    "tiktok": "social_icons/tiktok.png",
    "discord": "social_icons/discord.png"
}
```

3. Add the URLs to your `SOCIAL_CONFIG`:

```python

SOCIAL_CONFIG = {
    # ... existing URLs ...
    "tiktok": "https://tiktok.com/@yourusername",
    "discord": "https://discord.gg/yourserver"
}
```

## Troubleshooting

### Icons Not Showing

1. Verify icon files exist in `assets/social_icons/` directory
2. Check that file paths in `ICON_MAP` are correct
3. Restart your Reflex development server after adding new icons

### Wrong Links

1. Update the URLs in `SOCIAL_CONFIG` or pass custom `urls` parameter
2. Make sure URLs include `https://` protocol

### Styling Issues

1. Adjust `size` and `spacing` parameters
2. Use CSS classes for advanced styling
3. Wrap in containers for custom layouts

## File Structure

```

assets/
└── social_icons/
    ├── github.png
    ├── linkedin.png
    ├── youtube.png
    └── ... (other icon files)

lmrex/components/
├── social_icons.py          # Main component
├── footer.py               # Uses social_icons_footer()
└── SOCIAL_ICONS_CONFIG.md  # This guide
```
