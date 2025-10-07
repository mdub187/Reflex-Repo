
# import reflex as rx
# from ..state.state import State

# def media_carousel(self, state):
#     return rx.vstack(
#         rx.heading("My Photo and Video Carousel", size="lg"),
#         rx.carousel(
#             rx.foreach(
#                 State.media,
#                 lambda item: rx.cond(
#                     item["type"] == "video",
#                     rx.carousel_item(
#                         rx.video(
#                             url=item["src"],
#                             controls=True,
#                             width="100%",
#                             height="auto",
#                         )
#                     ),
#                     rx.carousel_item(
#                         rx.image(
#                             src=item["src"],
#                             width="100%",
#                             height="auto",
#                         )
#                     ),
#                 ),
#             ),
#             # Optional: Add controls and indicators
#             rx.carousel_previous_button(),
#             rx.carousel_next_button(),
#             rx.carousel_indicators(),
#             width="600px", # Example size
#         ),
#     )
#     return media_carousel(self, state)
