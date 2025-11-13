# responsive_utils.py

from lmrex.components.navbar import navbar
from lmrex.imports import rx


def apply_responsive_styles():
    rx.hstack(
        rx.link(
            navbar(),
            # Define your responsive styles here
            styles={
                "link": {
                    "padding": "10px",
                    "margin": "5px",
                    "display": "inline-block",
                    "min_width": "48px",  # Minimum touch target size
                    "min_height": "48px",  # Minimum touch target size
                }
            },
        ),
    )
    return apply_responsive_styles
