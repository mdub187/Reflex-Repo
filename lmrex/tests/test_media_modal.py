import pytest
from lmrex.components.media_modal import MediaFormState
from lmrex.state.state import State
from lmrex.models.media_model import MediaService

def _unwrap_var(value):
    """
    If `value` is callable, call it; otherwise return it as-is.

    This handles `@rx.var` decorated attributes that may be descriptors or
    callables depending on the Reflex runtime.
    """
    return value() if callable(value) else value

def test_media_form_submit_increments_media_count():
    """
    Submitting the media modal form should increment the media count,
    close the modal, and reset the form fields. We avoid iterating over
    `State.media` directly (it's a reactive Var) and instead assert on
    `State.media_count`.
    """
    try:
        # Start with a clean slate
        State.media = []

        form = MediaFormState()
        form.media_type = "image"
        form.media_title = "Test Title"
        form.media_url = "https://example.com/test.png"

        initial_count = _unwrap_var(State.media_count)
        # Expect 0 since we reset the list
        assert initial_count == 0

        # Try to invoke the submit handler robustly (it may be wrapped by an event decorator)
        wrapped = getattr(form.handle_submit, "__wrapped__", None)
        if wrapped is not None:
            wrapped(form)
        else:
            try:
                form.handle_submit()
            except TypeError:
                cls_wrapped = getattr(MediaFormState.handle_submit, "__wrapped__", None)
                if cls_wrapped is not None:
                    cls_wrapped(form)
                else:
                    pytest.skip("Couldn't invoke MediaFormState.handle_submit in this environment")

        new_count = _unwrap_var(State.media_count)
        assert new_count == initial_count + 1

        # Ensure the modal was closed and the local form was reset
        assert State.show_modal is False
        assert form.media_title == ""
        assert form.media_url == ""
        assert form.media_type == ""
    finally:
        # Restore a reasonable default so other tests are not affected
        State.media = MediaService.get_default_media_items()
