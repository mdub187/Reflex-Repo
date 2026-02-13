# lmrex/components/user_login.py
"""
User Login Component - Simple wrapper for the login modal
Import and use login_modal for authentication functionality
"""

import reflex as rx
from .login_modal import login_modal, login_button_trigger, register_button_trigger, user_menu


def user_login() -> rx.Component:
    """
    User login component.
    Returns the login modal with trigger button.
    This is the main component to use in your navbar or pages.
    """
    return login_modal()


# Export commonly used components for convenience
__all__ = [
    "user_login",
    "login_modal",
    "login_button_trigger",
    "register_button_trigger", 
    "user_menu",
]