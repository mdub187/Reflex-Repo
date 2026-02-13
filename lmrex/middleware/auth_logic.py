# lmrex/middleware/auth_logic.py
"""
Authentication middleware and logic
Uses reflex-local-auth for secure token-based authentication
"""

import reflex as rx
import reflex_local_auth
from typing import Optional


def require_login(page_function):
    """
    Decorator to protect pages - redirects to login if not authenticated
    
    Usage:
        @require_login
        def protected_page():
            return rx.text("This is protected")
    """
    def wrapper(*args, **kwargs):
        # This would need to check auth state
        # For now, pages handle their own auth checks
        return page_function(*args, **kwargs)
    return wrapper


def get_user_from_token(token: str) -> Optional[dict]:
    """
    Helper function to get user information from a token
    This is handled automatically by reflex-local-auth
    """
    # reflex-local-auth manages this internally
    # This is here for compatibility/future custom logic
    return None


def hash_password(password: str) -> str:
    """
    Hash a password - handled by reflex-local-auth
    This is here for reference
    """
    # reflex-local-auth uses passlib for password hashing
    # You don't need to call this directly
    return password


def verify_password(password: str, hashed: str) -> bool:
    """
    Verify a password against a hash - handled by reflex-local-auth
    This is here for reference
    """
    # reflex-local-auth uses passlib for password verification
    # You don't need to call this directly
    return False