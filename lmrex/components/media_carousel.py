import reflex as rx
from ..state.state import State

def media_carousel():
    return rx.vstack(
        # Title
        rx.heading("My Media Carousel", size="9", text_align="center"),

        # Main media container with consistent sizing
        rx.box(
            rx.cond(
                State.current_media_item["type"] == "video",
                # Video container with fixed dimensions
                rx.el.iframe(
                    src=State.current_media_item["src"],
                    width="100%",
                    height="100%",
                    frameborder="0",
                    display="block",
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture",
                    allowfullscreen=True,
                    style={
                        "border_radius": "8px",
                    }
                ),
                # Image container with fixed dimensions and object-fit
                rx.image(
                    src=State.current_media_item["src"],
                    width="100%",
                    height="100%",
                    object_fit="cover",
                    style={
                        "border_radius": "8px",
                    }
                ),
            ),
            # Container styles - fixed dimensions for consistency
            style={
                "width": "600px",
                "height": "400px",
                "border": "1px solid #ddd",
                "border_radius": "12px",
                "padding": "10px",
                "background_color": "#f8f9fa",
                "margin": "0 auto",
                "box_shadow": "0 4px 6px rgba(0, 0, 0, 0.1)",
                "overflow": "hidden",
                # "display": "flex",
                "align_items": "center",
                "justify_content": "center",
            },
        ),

        # Media title (if available)
        rx.cond(
            State.current_media_item.get("title", "") != "",
            rx.text(
                State.current_media_item.get("title", ""),
                size="4",
                weight="medium",
                text_align="center",
                style={
                    "margin_top": "15px",
                    "color": "#374151",
                    "max_width": "600px"
                }
            ),
            rx.box()
        ),

        # Navigation controls
        rx.hstack(
            rx.button(
                "← Previous",
                on_click=State.previous_item,
                disabled=State.media.length() == 0,
                variant="outline",
                size="3",
                style={
                    "min_width": "100px",
                }
            ),
            # Counter with consistent spacing
            rx.box(
                rx.text(
                    State.current_index + 1,
                    " / ",
                    State.media.length(),
                    size="3",
                    weight="medium",
                    text_align="center",
                ),
                style={
                    "min_width": "80px",
                    "padding": "0 20px",
                }
            ),
            rx.button(
                "Next →",
                on_click=State.next_item,
                disabled=State.media.length() == 0,
                variant="outline",
                size="3",
                style={
                    "min_width": "100px",
                }
            ),
            spacing="4",
            justify="center",
            align="center",
            width="100%",
        ),

        # Container styles for the entire carousel
        spacing="6",
        align="center",
        width="100%",
        max_width="800px",
        margin="0 auto",
        padding="20px",
        style={
            "background_color": "white",
            "border_radius": "16px",
            "box_shadow": "0 1px 3px rgba(0, 0, 0, 0.1)",
        }
    )
