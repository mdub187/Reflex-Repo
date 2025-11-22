# responsive_utils.py
def apply_responsive_styles():
    # Define your responsive styles here
    styles = {
    "width": {
        "max_width": "none",
        "min_width": "100%",  # Minimum touch target size
        "min_height": "48px",  # Minimum touch target size
    },
        "link": {
            "padding": "10px",
            "margin": "5px",
            "display": "inline-block",
            "min_width": "100%",  # Minimum touch target size
            "min_height": "48px",  # Minimum touch target size
        }
    }
    return styles
