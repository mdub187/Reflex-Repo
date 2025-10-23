# import reflex as rx
# from ..state.state import State
# from ..components.media_carousel import media_carousel
# from ..components.layout import centered_page, content_section, grid_layout


# def media_stats_card():
#     """Display media statistics in a card."""
#     return rx.card(
#         rx.vstack(
#             rx.heading("Media Statistics", size="5", text_align="center"),
#             rx.hstack(
#                 rx.vstack(
#                     rx.text(State.media_count, size="6", weight="bold", color="blue"),
#                     rx.text("Total Items", size="2", color="gray"),
#                     align="center",
#                     spacing="1",
#                 ),
#                 rx.vstack(
#                     rx.text(State.image_count, size="6", weight="bold", color="green"),
#                     rx.text("Images", size="2", color="gray"),
#                     align="center",
#                     spacing="1",
#                 ),
#                 rx.vstack(
#                     rx.text(State.video_count, size="6", weight="bold", color="purple"),
#                     rx.text("Videos", size="2", color="gray"),
#                     align="center",
#                     spacing="1",
#                 ),
#                 justify="around",
#                 width="100%",
#                 spacing="4",
#             ),
#             spacing="4",
#             padding="1.5rem",
#         ),
#         style={
#             "background": "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
#             "color": "white",
#             "border_radius": "12px",
#             "box_shadow": "0 8px 16px rgba(0, 0, 0, 0.1)",
#         }
#     )


# def media_controls_panel():
#     """Panel with media management controls."""
#     return rx.card(
#         rx.vstack(
#             rx.heading("Media Controls", size="5", margin_bottom="1rem"),

#             # Primary controls
#             rx.hstack(
#                 rx.button(
#                     "➕ Add Sample Image",
#                     on_click=State.add_media_item(
#                         "Random Image",
#                         "https://picsum.photos/800/600?random=" + rx.Var.create("Math.random()", _var_is_string=False),
#                         "image"
#                     ),
#                     size="3",
#                     color_scheme="green",
#                     style={"min_width": "150px"},
#                 ),
#                 rx.button(
#                     "📹 Add Sample Video",
#                     on_click=State.add_media_item(
#                         "Sample Video",
#                         "https://www.w3schools.com/html/mov_bbb.mp4",
#                         "video"
#                     ),
#                     size="3",
#                     color_scheme="blue",
#                     style={"min_width": "150px"},
#                 ),
#                 spacing="3",
#                 justify="center",
#                 wrap="wrap",
#             ),

#             # Item manipulation controls
#             rx.hstack(
#                 rx.button(
#                     "📋 Duplicate Current",
#                     on_click=State.duplicate_current_item,
#                     size="3",
#                     variant="outline",
#                     color_scheme="cyan",
#                     disabled=State.media_count == 0,
#                     style={"min_width": "150px"},
#                 ),
#                 rx.button(
#                     "🗑️ Remove Current",
#                     on_click=State.remove_current_item,
#                     size="3",
#                     variant="outline",
#                     color_scheme="red",
#                     disabled=State.media_count == 0,
#                     style={"min_width": "150px"},
#                 ),
#                 spacing="3",
#                 justify="center",
#                 wrap="wrap",
#             ),

#             # Reset controls
#             rx.hstack(
#                 rx.button(
#                     "🔄 Reset to Defaults",
#                     on_click=State.reset_to_defaults,
#                     size="3",
#                     variant="outline",
#                     color_scheme="gray",
#                     style={"min_width": "150px"},
#                 ),
#                 rx.button(
#                     "🧹 Clear All",
#                     on_click=State.clear_all_media,
#                     size="3",
#                     variant="outline",
#                     color_scheme="orange",
#                     style={"min_width": "150px"},
#                 ),
#                 spacing="3",
#                 justify="center",
#                 wrap="wrap",
#             ),

#             spacing="4",
#             align="center",
#             width="100%",
#         ),
#         style={
#             "padding": "2rem",
#             "background_color": "#f8fafc",
#             "border": "1px solid #e2e8f0",
#             "border_radius": "12px",
#         }
#     )


# def media_type_filters():
#     """Display media items filtered by type."""
#     return rx.hstack(
#         # Images only
#         rx.card(
#             rx.vstack(
#                 rx.heading("📷 Images", size="4", color="green"),
#                 rx.cond(
#                     State.has_images,
#                     rx.vstack(
#                         rx.foreach(
#                             State.get_images_only(),
#                             lambda item: rx.hstack(
#                                 rx.image(
#                                     src=item["url"],
#                                     width="40px",
#                                     height="40px",
#                                     object_fit="cover",
#                                     border_radius="4px",
#                                 ),
#                                 rx.vstack(
#                                     rx.text(item["title"], size="2", weight="bold"),
#                                     rx.text("Image", size="1", color="gray"),
#                                     align="start",
#                                     spacing="1",
#                                     flex="1",
#                                 ),
#                                 spacing="2",
#                                 align="center",
#                                 padding="0.5rem",
#                                 style={
#                                     "border": "1px solid #e2e8f0",
#                                     "border_radius": "6px",
#                                     "background_color": "white",
#                                 }
#                             )
#                         ),
#                         spacing="2",
#                         width="100%",
#                     ),
#                     rx.text(
#                         "No images available",
#                         size="2",
#                         color="gray",
#                         style={"font_style": "italic"}
#                     )
#                 ),
#                 align="start",
#                 spacing="3",
#                 width="100%",
#             ),
#             style={
#                 "flex": "1",
#                 "min_height": "200px",
#                 "padding": "1rem",
#                 "border": "2px solid #10b981",
#                 "border_radius": "8px",
#             }
#         ),

#         # Videos only
#         rx.card(
#             rx.vstack(
#                 rx.heading("🎬 Videos", size="4", color="purple"),
#                 rx.cond(
#                     State.has_videos,
#                     rx.vstack(
#                         rx.foreach(
#                             State.get_videos_only(),
#                             lambda item: rx.hstack(
#                                 rx.box(
#                                     rx.text("📹", size="4"),
#                                     width="40px",
#                                     height="40px",
#                                     display="flex",
#                                     align_items="center",
#                                     justify_content="center",
#                                     style={
#                                         "background_color": "#f3f4f6",
#                                         "border_radius": "4px",
#                                         "border": "1px solid #d1d5db",
#                                     }
#                                 ),
#                                 rx.vstack(
#                                     rx.text(item["title"], size="2", weight="bold"),
#                                     rx.text("Video", size="1", color="gray"),
#                                     align="start",
#                                     spacing="1",
#                                     flex="1",
#                                 ),
#                                 spacing="2",
#                                 align="center",
#                                 padding="0.5rem",
#                                 style={
#                                     "border": "1px solid #e2e8f0",
#                                     "border_radius": "6px",
#                                     "background_color": "white",
#                                 }
#                             )
#                         ),
#                         spacing="2",
#                         width="100%",
#                     ),
#                     rx.text(
#                         "No videos available",
#                         size="2",
#                         color="gray",
#                         style={"font_style": "italic"}
#                     )
#                 ),
#                 align="start",
#                 spacing="3",
#                 width="100%",
#             ),
#             style={
#                 "flex": "1",
#                 "min_height": "200px",
#                 "padding": "1rem",
#                 "border": "2px solid #8b5cf6",
#                 "border_radius": "8px",
#             }
#         ),

#         spacing="4",
#         width="100%",
#         align="start",
#     )


# def current_item_details():
#     """Display detailed information about the current media item."""
#     return rx.card(
#         rx.vstack(
#             rx.heading("🔍 Current Item Details", size="5"),

#             rx.cond(
#                 State.media_count > 0,
#                 rx.vstack(
#                     # Item info
#                     rx.hstack(
#                         rx.text("Title:", weight="bold", size="3"),
#                         rx.text(State.current_media_item["title"], size="3"),
#                         spacing="2",
#                     ),
#                     rx.hstack(
#                         rx.text("Type:", weight="bold", size="3"),
#                         rx.badge(State.current_media_item["type"], size="2"),
#                         spacing="2",
#                     ),
#                     rx.hstack(
#                         rx.text("URL:", weight="bold", size="3"),
#                         rx.text(
#                             State.current_media_item["url"],
#                             size="2",
#                             color="blue",
#                             style={"word_break": "break-all"}
#                         ),
#                         spacing="2",
#                         align="start",
#                     ),
#                     rx.hstack(
#                         rx.text("Position:", weight="bold", size="3"),
#                         rx.text(
#                             f"{State.current_index + 1} of {State.media_count}",
#                             size="3"
#                         ),
#                         spacing="2",
#                     ),

#                     align="start",
#                     spacing="3",
#                     width="100%",
#                 ),
#                 rx.text(
#                     "No media items available. Add some items to see details!",
#                     size="3",
#                     color="gray",
#                     text_align="center",
#                     style={"font_style": "italic"}
#                 )
#             ),

#             align="start",
#             spacing="4",
#             width="100%",
#         ),
#         style={
#             "padding": "2rem",
#             "background": "linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%)",
#             "border_radius": "12px",
#             "box_shadow": "0 4px 8px rgba(0, 0, 0, 0.1)",
#         }
#     )


# def media_demo():
#     """Main demo page showcasing MediaService features."""
#     return centered_page(
#         # Statistics overview
#         media_stats_card(),

#         # Main carousel section
#         content_section(
#             media_carousel(State.current_media_item),
#             title="Media Gallery",
#             subtitle="Browse and interact with your media collection",
#             padding="3rem",
#             shadow=True,
#             max_width="1000px",
#         ),

#         # Controls panel
#         media_controls_panel(),

#         # Current item details
#         current_item_details(),

#         # Type filters section
#         content_section(
#             media_type_filters(),
#             title="📂 Items by Type",
#             subtitle="View media organized by content type",
#             padding="2rem",
#             shadow=True,
#             max_width="1000px",
#         ),

#         # Features overview
#         content_section(
#             rx.grid(
#                 rx.vstack(
#                     rx.text("✅ Add/Remove Items", weight="bold"),
#                     rx.text("✅ Update Items", weight="bold"),
#                     rx.text("✅ Type Validation", weight="bold"),
#                     align="start",
#                     spacing="1",
#                 ),
#                 rx.vstack(
#                     rx.text("✅ Filter by Type", weight="bold"),
#                     rx.text("✅ Item Navigation", weight="bold"),
#                     rx.text("✅ Statistics Tracking", weight="bold"),
#                     align="start",
#                     spacing="1",
#                 ),
#                 rx.vstack(
#                     rx.text("✅ Data Validation", weight="bold"),
#                     rx.text("✅ Error Handling", weight="bold"),
#                     rx.text("✅ Type Safety", weight="bold"),
#                     align="start",
#                     spacing="1",
#                 ),
#                 columns="3",
#                 spacing="4",
#                 width="100%",
#             ),
#             title="💡 MediaService Features",
#             subtitle="Comprehensive media management capabilities",
#             background_color="#f0f9ff",
#             padding="2rem",
#             shadow=True,
#             max_width="800px",
#         ),

#         title="🎬 MediaService Demo",
#         max_width="1200px",
#         padding="2rem",
#     )
