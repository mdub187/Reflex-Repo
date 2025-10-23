import reflex as rx
from ..state.state import State

def media_carousel(current_media_item):
    return rx.vstack(
        # Title
        rx.heading("", size="9", text_align="center"),

<<<<<<< HEAD
<<<<<<< Updated upstream
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
=======
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
=======
>>>>>>> parent of 4a4eed8 (cleaning up refactor, added filed to .gitignore, added authentication logic, the logic is sitll a work in progress and isnt yet working. encountered some roadblocks i did have some help for co pilot. i want to clean up and make sure it didnt overcomplicate things.)
        # Main media container with consistent sizing
        rx.box(
            rx.cond(
                State.current_media_item["type"] == "video",
                # Video container with fixed dimensions
<<<<<<< HEAD
                rx.box(
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
                    rx.image(
                        src=State.current_media_item["url"],
                        width="100%",
                        height="100%",
                        object_fit="cover",
                        style={
                            "border_radius": "8px",
                        },
                    ),
=======
                rx.el.iframe(
                    src=State.current_media_item["url"],
                    width="100%",
                    height="100%",
                    frameborder="0",
                    display="felx",
                    flex_direction="column",
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture",
                    allowfullscreen=True,
                    style={
                        "border_radius": "8px",
                    }
>>>>>>> parent of 4a4eed8 (cleaning up refactor, added filed to .gitignore, added authentication logic, the logic is sitll a work in progress and isnt yet working. encountered some roadblocks i did have some help for co pilot. i want to clean up and make sure it didnt overcomplicate things.)
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
                variant="outline",
                size="3",
                disabled=State.media_count == 0,
                style={
                    "min_width": "100px",
                }
            ),
            # Counter with consistent spacing
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
                }
            ),
            rx.button(
                "Next →",
                on_click=State.next_item,
                variant="outline",
                size="3",
                disabled=State.media_count == 0,
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
        # Additional controls
        # rx.hstack(
        #     rx.button(
        #         "Add Image",
        #         on_click=State.add_media_item(
        #             "Sample Image",
        #             "https://picsum.photos/800/600",
        #             "image"
        #         ),
        #         size="2",
        #         variant="outline",
        #         color_scheme="green",
        #     ),
        #     rx.button(
        #         "Remove Current",
        #         on_click=State.remove_current_item,
        #         size="2",
        #         variant="outline",
        #         color_scheme="red",
        #         disabled=State.media_count == 0,
        #     ),
        #     rx.button(
        #         "Duplicate Current",
        #         on_click=State.duplicate_current_item,
        #         size="2",
        #         variant="outline",
        #         color_scheme="blue",
        #         disabled=State.media_count == 0,
        #     ),
        #     rx.button(
        #         "Reset to Defaults",
        #         on_click=State.reset_to_defaults,
        #         size="2",
        #         variant="outline",
        #         color_scheme="gray",
        #     ),
        #     spacing="3",
        #     justify="center",
        #     wrap="wrap",
        # ),

        # # Media statistics
        # rx.hstack(
        #     rx.badge(
        #         f"Images: {State.image_count}",
        #         color_scheme="blue",
        #         size="2",
        #     ),
        #     rx.badge(
        #         f"Videos: {State.video_count}",
        #         color_scheme="purple",
        #         size="2",
        #     ),
        #     rx.badge(
        #         f"Total: {State.media_count}",
        #         color_scheme="gray",
        #         size="2",
        #     ),
        #     spacing="3",
        #     justify="center",
        # ),

        spacing="6",
        align="center",
        width="100%",
        max_width="800px",
        margin="0 auto",
        padding="20px",
        style={
<<<<<<< HEAD
            "width": "100%",
            "padding": "20px",
=======
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
            # Counter with consistent spacing
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
>>>>>>> Stashed changes
        },
=======
            "background_color": "white",
            "border_radius": "16px",
            "box_shadow": "0 1px 3px rgba(0, 0, 0, 0.1)",
        }
>>>>>>> parent of 4a4eed8 (cleaning up refactor, added filed to .gitignore, added authentication logic, the logic is sitll a work in progress and isnt yet working. encountered some roadblocks i did have some help for co pilot. i want to clean up and make sure it didnt overcomplicate things.)
    )
