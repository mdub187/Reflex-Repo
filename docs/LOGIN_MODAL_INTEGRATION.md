# 🔐 Login Modal Integration Guide

Complete guide for integrating the login modal with your authentication system.

---

##What's Been Done

Your login modal is now **fully integrated** with the reflex-local-auth authentication system!

### Components Created

1. **`lmrex/components/login_modal.py`** - Main login modal component
2. **`lmrex/components/user_login.py`** - Updated wrapper
3. **`lmrex/components/navbar.py`** - Updated with modal integration

### Features

-Modal dialog with login and registration forms
-Integrated with reflex-local-auth for secure authentication
-Real-time login status indicator
-Automatic redirect to Account page after login
-User menu dropdown when logged in
-Tab switching between login and register
-Reusable components for any page

---

## 🚀 Quick Start

### Basic Usage

The login modal is now in your navbar automatically. Just click "Login" to open it!

### Manual Usage in Your Pages

```python
# In any page or component
import reflex as rx
from lmrex.components.login_modal import login_modal

def my_page():
    return rx.box(
        rx.heading("Welcome"),
        login_modal(),  # Adds login modal to page
    )
```

---

## 🎯 Available Components

### 1. `login_modal()`

Full modal with trigger button, login and register forms.

```python
from lmrex.components.login_modal import login_modal

# Use in any component
login_modal()
```

**What it includes:**
- Trigger button ("Login")
- Modal dialog
- Login form (tab 1)
- Registration form (tab 2)
- Status indicator
- Close button

---

### 2. `login_button_trigger()`

Standalone login button that opens the modal.

```python
from lmrex.components.login_modal import login_button_trigger

# Place anywhere
login_button_trigger()
```

**Use case:** When you want just a login button without the full modal structure.

---

### 3. `register_button_trigger()`

Standalone registration button that opens the modal on the register tab.

```python
from lmrex.components.login_modal import register_button_trigger

# Place anywhere
register_button_trigger()
```

**Use case:** Landing pages or signup prompts.

---

### 4. `user_menu()`

Smart component that shows:
- Login button (when logged out)
- User menu dropdown (when logged in)

```python
from lmrex.components.login_modal import user_menu

# In navbar or header
user_menu()
```

**Features:**
- Shows username when logged in
- Dropdown with Account and Logout options
- Automatically switches based on auth status

---

## 📝 Integration Examples

### Example 1: Landing Page with Login

```python
# lmrex/ui/landing.py
import reflex as rx
from lmrex.components.login_modal import login_button_trigger, register_button_trigger

def landing_page():
    return rx.box(
        rx.vstack(
            rx.heading("Welcome to Our App", size="9"),
            rx.text("Get started today!"),
            rx.hstack(
                login_button_trigger(),
                register_button_trigger(),
                spacing="4",
            ),
            spacing="6",
            align="center",
        ),
        padding="4rem",
    )
```

---

### Example 2: Protected Content Prompt

```python
# Show login prompt for protected content
import reflex as rx
from lmrex.state.auth_state import AuthState
from lmrex.components.login_modal import login_button_trigger

def protected_content():
    return rx.cond(
        AuthState.is_logged_in,
        # Logged in - show content
        rx.box(
            rx.heading("Secret Content"),
            rx.text("This is only for members!"),
        ),
        # Not logged in - show login prompt
        rx.card(
            rx.vstack(
                rx.icon("lock", size=40),
                rx.heading("Login Required", size="6"),
                rx.text("Please log in to view this content"),
                login_button_trigger(),
                spacing="3",
                align="center",
            ),
            padding="3rem",
        ),
    )
```

---

### Example 3: Custom Navbar Integration

```python
# Custom navbar with login modal
import reflex as rx
from lmrex.components.login_modal import user_menu
from lmrex.state.auth_state import AuthState

def my_navbar():
    return rx.hstack(
        rx.heading("My App"),
        rx.spacer(),
        rx.hstack(
            rx.link("Home", href="/"),
            rx.link("About", href="/about"),
            # Conditional menu
            rx.cond(
                AuthState.is_logged_in,
                rx.link("Dashboard", href="/dashboard"),
            ),
            user_menu(),  # Login button or user menu
            spacing="4",
        ),
        padding="1rem",
        width="100%",
    )
```

---

### Example 4: Inline Login Form

```python
# Embed login directly in a page (no modal)
import reflex as rx
import reflex_local_auth

def inline_login():
    return rx.card(
        rx.vstack(
            rx.heading("Sign In", size="6"),
            rx.form(
                rx.vstack(
                    rx.input(
                        placeholder="Username",
                        name="username",
                        required=True,
                    ),
                    rx.input(
                        placeholder="Password",
                        name="password",
                        type="password",
                        required=True,
                    ),
                    rx.button(
                        "Login",
                        type="submit",
                        width="100%",
                    ),
                    spacing="3",
                    width="100%",
                ),
                on_submit=reflex_local_auth.LoginState.on_submit,
            ),
            spacing="4",
        ),
        max_width="400px",
    )
```

---

## 🎨 Customization

### Change Modal Appearance

Edit `lmrex/components/login_modal.py`:

```python
# Change button style
rx.dialog.trigger(
    rx.button(
        rx.icon("log-in", size=16),
        "Login",
        variant="solid",          # Change variant
        color_scheme="purple",    # Change color
        size="3",                 # Change size
        on_click=LoginModalState.open_modal("login"),
    ),
)

# Change modal size
rx.dialog.content(
    # ... content
    max_width="500px",  # Make modal wider
)
```

---

### Add Custom Fields

Add email field to registration:

```python
# In login_modal.py, register form
rx.input(
    placeholder="Email",
    name="email",
    type="email",
    required=True,
    size="3",
),
```

Then update your user model to store email (see AUTH_SETUP_GUIDE.md).

---

### Custom Redirect After Login

```python
# Edit the form submission to redirect
rx.form(
    # ... form fields
    on_submit=[
        reflex_local_auth.LoginState.on_submit,
        rx.redirect("/dashboard"),  # Custom redirect
    ],
)
```

---

### Add Social Login Buttons

```python
# In login_modal.py, add to login tab
rx.vstack(
    # ... existing form
    rx.divider(),
    rx.text("Or continue with", size="2"),
    rx.hstack(
        rx.button(
            rx.icon("github", size=16),
            "GitHub",
            on_click=handle_github_login,
            variant="soft",
        ),
        rx.button(
            rx.icon("google", size=16),
            "Google",
            on_click=handle_google_login,
            variant="soft",
        ),
        spacing="2",
    ),
)
```

---

## 🔧 State Management

### LoginModalState

The modal has its own state for UI management:

```python
class LoginModalState(rx.State):
    show_modal: bool = False        # Is modal open?
    active_tab: str = "login"       # Current tab
    
    # Events
    toggle_modal()                  # Open/close toggle
    open_modal(tab="login")         # Open with specific tab
    close_modal()                   # Close modal
    switch_to_register()            # Switch to register tab
    switch_to_login()               # Switch to login tab
```

**Usage:**

```python
# Open modal programmatically
rx.button(
    "Sign Up Now",
    on_click=LoginModalState.open_modal("register"),
)

# Close modal after action
rx.button(
    "Cancel",
    on_click=LoginModalState.close_modal,
)
```

---

### AuthState Integration

The modal uses `AuthState` for authentication:

```python
from lmrex.state.auth_state import AuthState

# Check if logged in
AuthState.is_logged_in

# Get username
AuthState.user_email

# Logout
AuthState.logout_and_redirect()
```

---

## 🎯 Complete Integration Flow

### 1. User Clicks Login Button
```
User → Click "Login" → LoginModalState.open_modal() → Modal opens
```

### 2. User Submits Login Form
```
User → Fill form → Click "Sign In" → reflex_local_auth.LoginState.on_submit
→ Validate credentials → Create session token → Update AuthState
→ Modal shows "Logged in as username"
```

### 3. User Navigates to Account
```
User → Click "Go to Account" → rx.redirect("/Account") 
→ ProtectedState.on_load() → Check authentication → Load user data
```

### 4. User Logs Out
```
User → Click "Logout" → AuthState.logout_and_redirect()
→ Clear session token → Delete from database → Redirect to /Home
```

---

## 📊 Component Hierarchy

```
navbar()
├── user_menu()
│   ├── [If logged out] login_button_trigger()
│   │   └── Opens: login_modal()
│   └── [If logged in] rx.menu.root()
│       ├── Account link
│       └── Logout button

login_modal()
├── rx.dialog.root()
│   ├── rx.dialog.trigger() (Login button)
│   └── rx.dialog.content()
│       ├── Tabs (Login/Register)
│       ├── Login Form → reflex_local_auth.LoginState.on_submit
│       ├── Register Form → reflex_local_auth.RegistrationState.on_submit
│       └── Status indicator (if logged in)
```

---

## 🐛 Troubleshooting

### Modal doesn't open

**Check:**
1. Is `LoginModalState` imported correctly?
2. Is the component using `LoginModalState.open_modal()`?
3. Check browser console for errors (F12)

**Solution:**
```python
# Make sure you're using the correct import
from lmrex.components.login_modal import login_modal, LoginModalState

# Use the event handler
rx.button("Login", on_click=LoginModalState.open_modal("login"))
```

---

### Login form doesn't submit

**Check:**
1. Are form fields using correct `name` attributes?
2. Is `on_submit` connected to `reflex_local_auth.LoginState.on_submit`?
3. Are required fields filled?

**Solution:**
```python
# Correct form structure
rx.form(
    rx.input(name="username", required=True),  # Must have name!
    rx.input(name="password", type="password", required=True),
    rx.button("Login", type="submit"),  # Must be type="submit"
    on_submit=reflex_local_auth.LoginState.on_submit,
)
```

---

### Login succeeds but modal doesn't show status

**Check:**
1. Is `AuthState` imported?
2. Is the status conditional rendering correctly?
3. Refresh the page after login

**Solution:**
```python
# Add status indicator
rx.cond(
    AuthState.is_logged_in,
    rx.badge(f"Logged in as {AuthState.user_email}"),
)
```

---

### Multiple modals interfering

**Issue:** Multiple `login_modal()` instances on same page

**Solution:** Use only one instance, or use `login_button_trigger()`:
```python
# Instead of multiple login_modal()
# Use:
login_button_trigger()  # Just the trigger button
```

---

## 🔐 Security Best Practices

### 1. Never Store Passwords in State

✅ **Correct:** Forms submit directly to `reflex_local_auth`
```python
on_submit=reflex_local_auth.LoginState.on_submit
```

 **Wrong:** Storing password in custom state
```python
# Don't do this!
password: str = ""  # Never store passwords!
```

---

### 2. Use HTTPS in Production

```python
# In production rxconfig.py
config = rx.Config(
    deploy_url="https://yourdomain.com",  # Use HTTPS!
)
```

---

### 3. Validate on Backend

The forms use `reflex_local_auth` which handles:
-Password hashing (bcrypt)
-SQL injection prevention
-Session token generation
-Token validation

You don't need to add extra validation for basic auth.

---

## 📚 Related Documentation

- **`AUTH_QUICK_START.md`** - Authentication system basics
- **`AUTH_SETUP_GUIDE.md`** - Complete auth documentation
- **`lmrex/components/login_modal.py`** - Source code
- **`lmrex/state/auth_state.py`** - Authentication state

---

##Testing Checklist

Test your login modal integration:

- [ ] Click "Login" button - modal opens
- [ ] Switch between Login and Register tabs
- [ ] Register new account - auto-login works
- [ ] Login with existing account - works
- [ ] Status shows "Logged in as username"
- [ ] Click "Go to Account" - redirects correctly
- [ ] Logout - redirects to home, modal closes
- [ ] Navbar shows user menu when logged in
- [ ] Mobile menu shows login modal
- [ ] Can close modal with X or Cancel button

---

## Summary

Your login modal is now fully integrated with authentication!

**Key Components:**
- `login_modal()` - Full modal with forms
- `user_menu()` - Smart login/user menu
- `login_button_trigger()` - Standalone button
- `register_button_trigger()` - Signup button

**In Your Navbar:**
- Desktop: Shows user_menu() with dropdown
- Mobile: Shows login in hamburger menu

**Authentication Flow:**
- Modal → Form submit → reflex-local-auth → Database → Session token → Logged in

**Everything is working and ready to use!** 
---

**Created**: 2025-02-12  
**Status**:Fully Integrated  
**Framework**: Reflex 0.8.26  
**Auth**: reflex-local-auth 0.4.0
