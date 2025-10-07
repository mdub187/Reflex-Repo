# import reflex as rx
# from reflex import App, Component, alert_dialog, button, text, vstack


# def debug_modal() -> Component:
#     """A standalone debug modal component for testing purposes."""
#     return vstack(
#         alert_dialog(
#             alert_dialog.content(
#                 alert_dialog.title("Debug Modal"),
#                 rx.section(
#                     rx.text("This is a standalone debug modal for testing.")
#                 ),
#                 alert_dialog.footer(
#                     button("Close", on_click=lambda: print("Close button clicked"))
#                 ),
#             ),
#             is_open=True,  # Force the modal to always render
#             on_close=lambda: print("Modal closed"),
#         )
#     )


# class DebugApp(App):
#     """A minimal Reflex app for testing the debug modal."""

#     def render(self) -> Component:
#         return debug_modal()


# if __name__ == "__main__":
#     app = DebugApp()
#     app.run()
