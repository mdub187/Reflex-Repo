# Login Modal - Usage Examples

Quick copy-paste examples for using the login modal in your app.

---

## Basic Usage

### In Navbar (Already Done!)

```python
# lmrex/components/navbar.py
from .login_modal import user_menu

# In your navbar
user_menu()  # Shows login button or user menu
```

**Result:** Smart component that shows:
- Login button when logged out
- User menu dropdown when logged in

---

## 📝 Common Use Cases

### 1. Landing Page with Login & Register

```python
# lmrex/ui/landing.py
import reflex as rx
from lmrex.components.login_modal import login_button_trigger, register_button_trigger

def landing_page():
    return rx.center(
        rx.vstack(
            rx.heading("Welcome!", size="9"),
            rx.text("Join us today", size="5"),
            rx.hstack(
                login_button_trigger(),
                register_button_trigger(),
                spacing="3",
            ),
            spacing="6",
        ),
        min_height="80vh",
    )
```

---

### 2. Protected Content with Login Prompt

```python
# Show content only to logged-in users
import reflex as rx
from lmrex.state.auth_state import AuthState
from lmrex.components.login_modal import login_button_trigger

def members_only():
    return rx.cond(
        AuthState.is_logged_in,
        # Show content
        rx.box(
            rx.heading("Members Area"),
            rx.text(f"Welcome {AuthState.user_email}!"),
        ),
        # Show login prompt
        rx.card(
            rx.vstack(
                rx.icon("lock", size=40),
                rx.text("Please log in"),
                login_button_trigger(),
                spacing="3",
            ),
        ),
    )
```

---

### 3. Inline Login Form (No Modal)

```python
# Embed login directly in page
import reflex as rx
import reflex_local_auth

def simple_login():
    return rx.card(
        rx.form(
            rx.vstack(
                rx.input(placeholder="Username", name="username"),
                rx.input(placeholder="Password", name="password", type="password"),
                rx.button("Login", type="submit"),
                spacing="2",
            ),
            on_submit=reflex_local_auth.LoginState.on_submit,
        ),
    )
```

---

### 4. Custom Styled Modal Trigger

```python
# Big fancy login button
import reflex as rx
from lmrex.components.login_modal import LoginModalState

def hero_login_button():
    return rx.button(
        rx.hstack(
            rx.icon("sparkles", size=20),
            rx.text("Get Started Free", size="5"),
            rx.icon("arrow-right", size=20),
            spacing="2",
        ),
        on_click=LoginModalState.open_modal("register"),
        size="4",
        variant="solid",
        color_scheme="purple",
    )
```

---

### 5. Login Required Wrapper

```python
# Reusable wrapper for protected content
import reflex as rx
from lmrex.state.auth_state import AuthState
from lmrex.components.login_modal import login_button_trigger

def require_login(content: rx.Component, message: str = "Please log in"):
    return rx.cond(
        AuthState.is_logged_in,
        content,
        rx.center(
            rx.card(
                rx.vstack(
                    rx.icon("shield-alert", size=40),
                    rx.text(message),
                    login_button_trigger(),
                    spacing="3",
                ),
            ),
            min_height="60vh",
        ),
    )

# Usage
def protected_page():
    return require_login(
        rx.text("Secret content!"),
        message="Members only area"
    )
```

---

### 6. Multiple Call-to-Action Buttons

```python
# Different buttons for different flows
import reflex as rx
from lmrex.components.login_modal import LoginModalState

def pricing_page():
    return rx.vstack(
        rx.card(
            rx.vstack(
                rx.heading("Free Plan"),
                rx.button(
                    "Start Free Trial",
                    on_click=LoginModalState.open_modal("register"),
                ),
            ),
        ),
        rx.card(
            rx.vstack(
                rx.heading("Pro Plan"),
                rx.button(
                    "Sign Up for Pro",
                    on_click=LoginModalState.open_modal("register"),
                ),
            ),
        ),
        rx.text("Already have an account?"),
        rx.button(
            "Login",
            on_click=LoginModalState.open_modal("login"),
            variant="ghost",
        ),
    )
```

---

## Styling Examples

### Custom Modal Button

```python
# In lmrex/components/login_modal.py
# Change the trigger button style

rx.dialog.trigger(
    rx.button(
        rx.icon("user-circle", size=18),
        "Sign In",
        variant="solid",
        color_scheme="blue",
        size="3",
        on_click=LoginModalState.open_modal("login"),
    ),
)
```

---

### Themed Buttons

```python
# Match your app's theme
from lmrex.components.login_modal import LoginModalState

# Minimal style
rx.button(
    "Login",
    on_click=LoginModalState.open_modal(),
    variant="ghost",
)

# Bold style
rx.button(
    "Join Now",
    on_click=LoginModalState.open_modal("register"),
    variant="solid",
    color_scheme="green",
    size="4",
)

# Outline style
rx.button(
    "Sign In",
    on_click=LoginModalState.open_modal("login"),
    variant="outline",
)
```

---

## 🔧 Advanced Examples

### Auto-Open Modal on Page Load

```python
# Open login modal when page loads (if not logged in)
import reflex as rx
from lmrex.state.auth_state import AuthState
from lmrex.components.login_modal import LoginModalState, login_modal

def gated_page():
    return rx.box(
        rx.text("Protected content"),
        login_modal(),
        # Auto-open if not logged in
        on_mount=rx.cond(
            AuthState.is_logged_in,
            rx.noop(),  # Do nothing if logged in
            LoginModalState.open_modal(),  # Open if not logged in
        ),
    )
```

---

### Redirect After Login

```python
# Custom redirect after successful login
# Edit lmrex/components/login_modal.py

rx.form(
    # ... form fields
    on_submit=[
        reflex_local_auth.LoginState.on_submit,
        rx.redirect("/dashboard"),  # Custom redirect
        LoginModalState.close_modal,  # Close modal
    ],
)
```

---

### Login with Remember Me

```python
# Add remember me checkbox (future enhancement)
class LoginFormState(rx.State):
    remember_me: bool = False

rx.checkbox(
    "Remember me",
    checked=LoginFormState.remember_me,
    on_change=LoginFormState.set_remember_me,
)
```

---

## 📱 Responsive Examples

### Mobile-Friendly Login

```python
# Already responsive by default!
# But you can customize further:

rx.mobile_only(
    rx.button(
        rx.icon("log-in"),  # Icon only on mobile
        on_click=LoginModalState.open_modal(),
        size="2",
    ),
),
rx.desktop_only(
    rx.button(
        rx.icon("log-in", size=16),
        "Login",  # Text on desktop
        on_click=LoginModalState.open_modal(),
    ),
),
```

---

## Quick Reference

### Import Statements

```python
# Main components
from lmrex.components.login_modal import (
    login_modal,              # Full modal with trigger
    login_button_trigger,     # Just login button
    register_button_trigger,  # Just register button
    user_menu,                # Smart login/user menu
    LoginModalState,          # State management
)

# Auth state
from lmrex.state.auth_state import AuthState

# Direct auth functions
import reflex_local_auth
```

---

### Common Patterns

```python
# Open modal programmatically
on_click=LoginModalState.open_modal("login")
on_click=LoginModalState.open_modal("register")

# Close modal
on_click=LoginModalState.close_modal

# Check if logged in
rx.cond(AuthState.is_logged_in, logged_in_component, logged_out_component)

# Show username
rx.text(AuthState.user_email)

# Logout
on_click=AuthState.logout_and_redirect
```

---

## Testing Your Integration

1. **Click login button** - Modal opens
2. **Try registration** - Create account, auto-login
3. **Try login** - Login with credentials
4. **Check navbar** - Shows user menu when logged in
5. **Click logout** - Logs out and redirects
6. **Try protected page** - Redirects to login if not authenticated

---

**All examples are copy-paste ready!** 
**See LOGIN_MODAL_INTEGRATION.md for complete documentation.**
