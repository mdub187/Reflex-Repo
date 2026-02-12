# lmrex/components/debug/debug_modal.py
from reflex import Component, alert_dialog, button, text, vstack


def debug_modal() -> Component:
    """A standalone debug modal component for testing purposes."""
    return vstack(
        alert_dialog(
            alert_dialog.content(
                alert_dialog.title("Debug Modal"),
                text("This is a standalone debug modal for testing."),
                alert_dialog.footer(
                    button("Close", on_click=lambda: print("Close button clicked"))
                ),
            ),
            is_open=True,  # Force the modal to always render
            on_close=lambda: print("Modal closed"),
        )
    )
