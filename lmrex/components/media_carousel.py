import reflex as rx
from ..state.state import State


def media_carousel() -> rx.Component:
    """
    A carousel component that displays media items (images or videos).
    """
    return rx.box(
        rx.cond(
            State.media,
            rx.vstack(
                rx.cond(
                    State.current_media_item["type"] == "video",
                    rx.el.iframe(
                        src=State.current_media_item["url"],
                        width="100%",
                        height="100%",
                        frameborder="0",
                        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture",
                        allowfullscreen=True,
                        style={
                            "border_radius": "8px",
                        },
                    ),
                    rx.image(
                        src=State.current_media_item["url"],
                        width="100%",
                        height="100%",
                        object_fit="cover",
                        style={
                            "border_radius": "8px",
                        },
                    ),
                ),
                rx.vstack(
                    rx.hstack(
                        rx.button(
                            "Previous",
                            on_click=State.previous_item,
                            style={
                                "margin": "10px",
                            },
                        ),
                        rx.text(
                            f"{State.current_index + 1} of {State.media_count}",
                            size="2",
                            style={"color": "#6b7280"},
                        ),
                        rx.button(
                            "Next",
                            on_click=State.next_item,
                            style={
                                "margin": "10px",
                            },
                        ),
                        spacing="6",
                        justify="center",
                        align="center",
                        width="100%",
                    ),
                    # Thumbnails + pager (click a thumbnail to jump to that item)
                    rx.hstack(
                        rx.button(
                            "◀",
                            on_click=State.previous_thumbnail_page,
                            size="3",
                            variant="outline",
                            disabled=State.thumbnail_page == 0,
                            style={
                                "min_width": "40px",
                                "margin_right": "6px",
                            },
                        ),
                        rx.foreach(
                            State.visible_thumbnails,
                            lambda item: rx.cond(
                                item["url"] == State.current_media_item["url"],
                                rx.box(
                                    rx.image(
                                        src=item["url"],
                                        width="64px",
                                        height="48px",
                                        object_fit="cover",
                                        border_radius="6px",
                                    ),
                                    on_click=lambda item=item: State.set_current_index_by_item(
                                        item
                                    ),
                                    style={
                                        "padding": "2px",
                                        "border": "3px solid #3b82f6",
                                        "border_radius": "8px",
                                        "cursor": "pointer",
                                        "margin": "0 6px",
                                    },
                                ),
                                rx.box(
                                    rx.image(
                                        src=item["url"],
                                        width="64px",
                                        height="48px",
                                        object_fit="cover",
                                        border_radius="6px",
                                    ),
                                    on_click=lambda item=item: State.set_current_index_by_item(
                                        item
                                    ),
                                    style={
                                        "padding": "2px",
                                        "border": "1px solid #e5e7eb",
                                        "border_radius": "8px",
                                        "cursor": "pointer",
                                        "margin": "0 6px",
                                    },
                                ),
                            ),
                        ),
                        rx.button(
                            "▶",
                            on_click=State.next_thumbnail_page,
                            size="3",
                            variant="outline",
                            disabled=State.thumbnail_page
                            >= (State.total_thumbnail_pages - 1),
                            style={"min_width": "40px", "margin_left": "6px"},
                        ),
                        spacing="2",
                        align="center",
                        justify="center",
                        width="100%",
                    ),
                    spacing="3",
                    align="center",
                ),
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
                    "align_items": "center",
                    "justify_content": "center",
                },
            ),
            rx.text("No media items available."),
        ),
        style={
            "width": "100%",
            "padding": "20px",
        },
    )
