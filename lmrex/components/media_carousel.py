import reflex as rx
from ..state.state import State


def media_carousel(current_media_item):
    return rx.vstack(
        # Title and type indicator
        rx.vstack(
            rx.heading(
                State.current_media_item["title"], size="9", text_align="center"
            ),
            rx.badge(
                State.current_media_item["type"].upper(),
                color_scheme=rx.cond(
                    State.current_media_item["type"] == "video", "purple", "blue"
                ),
                size="2",
            ),
            spacing="2",
            align="center",
        ),
        # Main media container with consistent sizing
        rx.box(
            rx.cond(
                State.current_media_item["type"] == "video",
                # Video container with fixed dimensions
                rx.box(
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
                    style={
                        "width": "100%",
                        "height": "100%",
                        "display": "flex",
                        "align_items": "center",
                        "justify_content": "center",
                    },
                ),
                # Image container with fixed dimensions and object-fit
                rx.image(
                    src=State.current_media_item["url"],
                    width="100%",
                    height="100%",
                    object_fit="contain",
                    style={
                        "border_radius": "8px",
                    },
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
                "display": "flex",
                "align_items": "center",
                "justify_content": "center",
            },
        ),
        # Navigation controls within the media container
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
            # Thumbnails + pager
            rx.hstack(
                rx.button(
                    "◀",
                    on_click=State.previous_item,
                    size="3",
                    variant="outline",
                    disabled=State.current_media_item == 0,
                    style={
                        "min_width": "40px",
                        "margin_right": "6px",
                    },
                ),
                # rx.foreach(
                #     State.current_media_item,
                #     lambda item: rx.cond(
                #         # item["url"] == State.current_media_item["url"],
                #         rx.box(
                #             rx.image(
                #                 # src=item["url"],
                #                 width="64px",
                #                 height="48px",
                #                 object_fit="cover",
                #                 border_radius="6px",
                #             ),
                #             on_click=lambda item=item: State.media_count(item),
                #             style={
                #                 "padding": "2px",
                #                 "border": "3px solid #3b82f6",
                #                 "border_radius": "8px",
                #                 "cursor": "pointer",
                #                 "margin": "0 6px",
                #             },
                #         ),
                #         rx.box(
                #             rx.image(
                #                 src=item["url"],
                #                 width="64px",
                #                 height="48px",
                #                 object_fit="cover",
                #                 border_radius="6px",
                #             ),
                #             on_click=lambda item=item: State.set_current_index_by_item(item["url"]),
                #                 item
                #             ),
                #             style={
                #                 "padding": "2px",
                #                 "border": "1px solid #e5e7eb",
                #                 "border_radius": "8px",
                #                 "cursor": "pointer",
                #                 "margin": "0 6px",
                #             },
                #     )
                rx.button(
                    "▶",
                    on_click=State.next_item,
                    size="3",
                    variant="outline",
                    # disabled=State.thumbnail_page >= (State.total_thumbnail_pages - 1),
                    style={"min_width": "40px", "margin_left": "6px"},
                    spacing="2",
                    align="center",
                    justify="center",
                    width="100%",
                ),
                spacing="3",
                align="center",
            ),
            # Media title (if available)
            rx.cond(
                current_media_item.get("title", "") != "",
                rx.text(
                    current_media_item.get("title", ""),
                    size="4",
                    weight="medium",
                    text_align="center",
                    style={
                        "align": "center",
                        "margin_top": "15px",
                        "color": "#374151",
                        "max_width": "600px",
                    },
                ),
            ),
            # Media info
            rx.hstack(
                rx.text(
                    "Type: ",
                    State.current_media_item["type"].capitalize(),
                    size="3",
                    color="gray",
                ),
                rx.text(
                    "Item ",
                    State.current_index + 1,
                    " of ",
                    State.media_count,
                    size="3",
                    color="gray",
                ),
                spacing="4",
                justify="center",
                style={"margin_top": "10px"},
            ),
            # Navigation controls
            rx.hstack(
                rx.button(
                    "← Previous",
                    on_click=State.previous_item,
                    variant="outline",
                    size="3",
                    disabled=State.media_count == 0,
                    style={
                        "min_width": "100px",
                    },
                ),
                rx.box(
                    rx.text(
                        State.current_index + 1,
                        " / ",
                        State.media_count,
                        size="3",
                        weight="medium",
                        text_align="center",
                    ),
                    style={
                        "min_width": "80px",
                        "padding": "0 20px",
                    },
                ),
                rx.button(
                    "Next →",
                    on_click=State.next_item,
                    variant="outline",
                    size="3",
                    disabled=State.media_count == 0,
                    style={
                        "min_width": "100px",
                    },
                ),
                spacing="4",
                justify="center",
                align="center",
                width="100%",
            ),
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
            },
        ),
    )
