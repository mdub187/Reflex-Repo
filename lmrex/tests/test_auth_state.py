"""
Unit tests for the demo AuthState.

Run with pytest (install pytest if you don't have it):

    python -m pip install pytest
    pytest Reflex_pylot/lmrex/tests/test_auth_state.py

The tests are defensive about the `@rx.var` decorator: some decorated methods
become property-like or callables depending on the Reflex runtime. Tests
handle both cases by calling callables and returning non-callables as-is.
"""

from typing import Any
from lmrex.state.auth_state import AuthState

def _unwrap_var(value: Any) -> Any:
    """
    If `value` is callable, call it; otherwise return it as-is.

    This handles `@rx.var` decorated methods that may be descriptors or
    callables depending on the Reflex runtime. Tests should work in either case.
    """
    return value() if callable(value) else value

def test_handle_login_success_sets_token_and_user():
    auth = AuthState()
    # Ensure initially logged out
    assert auth.auth_token is None
    assert auth.authenticated_user is None

    # Simulate a normal (non-admin) login
    auth.handle_login_success("token")

    assert auth.auth_token == "demo-token"
    assert auth.authenticated_user is not None
    assert auth.authenticated_user.get("email") == "demo@example.local"

    # roles should be available via the var helper
    roles = _unwrap_var(auth.get_roles)
    assert roles == ["user"]

def test_handle_login_success_admin_sets_admin_user():
    auth = AuthState()

    auth.handle_login_success("demo-admin-token")

    assert auth.auth_token == "demo-admin-token"
    assert auth.authenticated_user is not None
    assert auth.authenticated_user.get("email") == "admin@example.local"

    roles = _unwrap_var(auth.get_roles)
    assert "admin" in roles

def test_clear_auth_token_clears_user_and_token(token):
    auth = AuthState()
    auth.handle_login_success("token")
    assert auth.auth_token is not None
    assert auth.authenticated_user is not None

    auth.clear_auth_token()
    assert auth.auth_token is None
    assert auth.authenticated_user is None

    is_auth = _unwrap_var(auth.is_authenticated)
    assert not is_auth

def test_set_user_email_updates_email():
    auth = AuthState()
    auth.handle_login_success("token")
    assert auth.authenticated_user is not None

    auth.set_user_email("new@example.local")

    assert auth.authenticated_user is not None
    assert auth.authenticated_user.get("email") == "new@example.local"
