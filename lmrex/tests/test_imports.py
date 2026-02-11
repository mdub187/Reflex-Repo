"""
Unit tests for import-time sanity checks.

These tests ensure:
- The top-level `lmrex.lmrex` module exposes the `app` variable Reflex expects.
- The `login_modal` component can be imported and invoked without raising
  import-time recursion/circular-import errors and returns a component-like object.

Run with pytest:
    pytest lmrex/tests/test_imports.py
"""

import importlib
from typing import Any

import pytest


def test_lmrex_exports_app():
    """The lmrex.lmrex module should expose an `app` variable."""
    mod = importlib.import_module("lmrex.lmrex")
    assert hasattr(mod, "app"), "lmrex.lmrex must expose an `app` variable"
    app = getattr(mod, "app")
    assert app is not None


def test_login_modal_import_and_render():
    """
    Import the `login_modal` factory and call it.

    We check that:
    - `login_modal` is callable,
    - calling `login_modal()` does not raise,
    - it returns an object that looks like a reflex component.
    """
    from lmrex.components.login_modal import login_modal
    from lmrex.imports import rx

    # Factory exists and is callable
    assert callable(login_modal), "login_modal should be a callable factory"

    # This should not raise (no recursion / circular import error)
    comp = login_modal()
    assert comp is not None, "login_modal() returned None"

    # If rx.Component is a real class, prefer `isinstance` check
    rx_component_cls = getattr(rx, "Component", None)
    if isinstance(rx_component_cls, type):
        assert isinstance(comp, rx_component_cls), "login_modal() did not return an rx.Component"

    # Fallback structural checks: the returned object should not be callable and should have component-like attrs
    assert not callable(comp), "login_modal() should return a component object, not a callable"
    assert any(hasattr(comp, attr) for attr in ("children", "_props", "props", "render"))


if __name__ == "__main__":
    pytest.main([__file__])