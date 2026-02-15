# 🔐 Authentication System - Quick Start Guide

**Status**: ✅ **READY TO USE**  
**Last Updated**: 2025-02-12  
**Database**: ✅ Migrated and ready

---

## ✨ What's Working Now

Your Reflex app now has **complete token-based authentication**:

- ✅ User registration with secure password hashing (bcrypt)
- ✅ Login/logout with session token management
- ✅ Protected routes (Account page requires login)
- ✅ Database tables created (`localuser`, `localauthsession`)
- ✅ Navbar shows login status dynamically
- ✅ Automatic redirect to login for protected pages
- ✅ Session persistence across page refreshes

---

## 🚀 How to Use (3 Steps)

### 1. **Start the App**

```bash
cd /Users/mdub/Documents/Git\ Repos/Reflex/Reflex-Repo
./start_reflex.sh
```

### 2. **Create an Account**

1. Open http://localhost:3000/Login
2. Click the **"Register"** tab
3. Enter a username (e.g., `yourname`)
4. Enter a password (e.g., `securepass123`)
5. Confirm the password
6. Click **"Register"**
7. You'll be automatically logged in!

### 3. **Access Protected Pages**

- After login, click **"Account"** in the navbar
- Or visit http://localhost:3000/Account directly
- You'll see your user information and protected content

---

## 🎯 Testing the System

### Test 1: Registration Flow
```
Navigate to /Login → Register tab → Create account
✅ Should auto-login and show "You're Logged In!" badge
✅ Navbar should show your username
✅ "Account" button appears in navbar
```

### Test 2: Login Flow
```
Logout → Login tab → Enter credentials
✅ Should redirect to Account page
✅ User info displayed correctly
```

### Test 3: Protected Page Access
```
Logout → Try to visit /Account directly
✅ Should redirect to /Login
✅ After login, access granted
```

### Test 4: Session Persistence
```
Login → Refresh the page
✅ Should stay logged in
✅ Token persists in browser
```

### Test 5: Logout
```
Click logout button (navbar or Account page)
✅ Redirects to /Home
✅ Navbar shows "Login" button again
✅ Cannot access /Account anymore
```

---

## 📊 What's in the Database

### Check Users
```bash
sqlite3 reflex.db "SELECT id, username, enabled FROM localuser;"
```

### Check Active Sessions
```bash
# sqlite3 reflex.db "SELECT user_id, session_id, expiration FROM localauthsession;"
```

### View All Tables
```bash
# sqlite3 reflex.db ".tables"
# Output: alembic_version  localauthsession  localuser
```

---

## 🗂️ File Structure

### Authentication Files

```
lmrex/
├── state/
│   └── auth_state.py          # AuthState & ProtectedState
├── ui/
│   ├── login.py               # Login/Register page
│   └── account.py             # Protected account page
├── middleware/
│   └── auth_logic.py          # Auth utilities
└── components/
    └── navbar.py              # Navbar with auth status

Database:
└── reflex.db                  # SQLite database
    ├── localuser              # User accounts
    └── localauthsession       # Session tokens
```

---

## 🔑 Key Components

### AuthState (lmrex/state/auth_state.py)

Main authentication state that extends `reflex_local_auth.LocalAuthState`:

**Available Properties:**
- `AuthState.is_logged_in` - Boolean: is user authenticated?
- `AuthState.user_email` - String: username of logged-in user
- `AuthState.user_info` - Dict: user details (id, username, enabled)
- `AuthState.authenticated_user` - User object from database

**Event Handlers:**
- `AuthState.logout_and_redirect()` - Logout and go to /Home
- `AuthState.check_login_redirect()` - Check if logged in, go to /Account

### ProtectedState (lmrex/state/auth_state.py)

For protected pages that require authentication:

```python
# In any protected page
from lmrex.state.auth_state import ProtectedState

def my_protected_page():
    return rx.box(
        rx.text(ProtectedState.protected_data),
        on_mount=ProtectedState.on_load,  # Auto-redirect if not logged in
    )
```

### Login Page (lmrex/ui/login.py)

Uses `reflex_local_auth`'s built-in login and registration pages:
- Tab 1: Login form
- Tab 2: Registration form
- Status indicator showing current login state

### Account Page (lmrex/ui/account.py)

Protected page showing:
- User information (username, ID, status)
- Protected content
- Account actions (home, gallery, logout)
- Security information

---

## 🛠️ Customization Examples

### Add More Protected Pages

```python
# lmrex/ui/my_page.py
import reflex as rx
from lmrex.state.auth_state import ProtectedState

def my_protected_page() -> rx.Component:
    return rx.box(
        rx.heading("Members Only!"),
        rx.text(f"Welcome {ProtectedState.user_email}"),
        on_mount=ProtectedState.on_load,  # Protects the page
    )
```

Then add to routes:
```python
# lmrex/routes/routes.py
from lmrex.ui.my_page import my_protected_page

app.add_page(my_protected_page, route="/Members")
```

### Add Email to Users

1. Modify the model:
```python
# lmrex/models/user_model.py
class LocalUser(SQLModel, table=True, extend_existing=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    password_hash: str
    enabled: bool = True
    email: Optional[str] = None  # NEW FIELD
```

2. Run migration:
```bash
reflex db makemigrations --message "add email field"
reflex db migrate
```

### Change Session Expiration

Edit `rxconfig.py`:
```python
config = rx.Config(
    # ... existing config
    redis_token_expiration=7200,  # 2 hours (default: 3600)
)
```

---

## 🐛 Troubleshooting

### "Can't access Account page"
**Solution**: Make sure you're logged in. Click "Login" in navbar.

### "Registration not working"
**Check**:
1. Database exists: `ls -la reflex.db`
2. Tables exist: `sqlite3 reflex.db ".tables"`
3. App is running: Check http://localhost:3000

### "Token not persisting"
**Solutions**:
- Enable browser cookies
- Clear browser cache and try again
- Check session expiration setting

### "Navbar not updating"
**Solution**: 
- Refresh the page
- Make sure `AuthState` is imported in navbar.py
- Check console for errors (F12)

### "Password forgotten"
**Reset manually**:
```python
from passlib.context import CryptContext
import sqlite3

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
new_hash = pwd_context.hash("new_password")

conn = sqlite3.connect('reflex.db')
cursor = conn.cursor()
cursor.execute(
    "UPDATE localuser SET password_hash = ? WHERE username = ?",
    (new_hash, "username")
)
conn.commit()
conn.close()
```

---

## 🔒 Security Features

### What's Secure 
1. **Password Hashing**: Uses bcrypt (industry standard)
2. **Session Tokens**: Unique, secure session IDs
3. **Token Expiration**: Sessions expire automatically
4. **SQL Injection Protection**: SQLModel/SQLAlchemy prevents injection
5. **CORS Configuration**: Only localhost allowed in development

### Production Checklist 
Before deploying to production:

- [ ] Enable HTTPS (never use HTTP for auth)
- [ ] Set strong session expiration (1-2 hours)
- [ ] Update CORS to production domain only
- [ ] Use environment variables for database URL
- [ ] Enable rate limiting on login endpoint
- [ ] Add logging for auth events
- [ ] Implement password reset flow
- [ ] Add email verification (optional)
- [ ] Set up regular database backups
- [ ] Security audit completed

---

## 📈 Next Steps

### Recommended Enhancements

1. **Email Verification**
   - Add email field to users
   - Send verification emails
   - Require verification before full access

2. **Password Reset**
   - Generate reset tokens
   - Email reset links
   - Create password reset page

3. **User Roles**
   - Add role field (admin, user, moderator)
   - Create role-based access control
   - Admin-only pages

4. **Profile Management**
   - Edit username/email
   - Change password
   - Upload avatar

5. **Two-Factor Authentication**
   - Add TOTP support
   - Use libraries like `pyotp`

6. **OAuth Integration**
   - Google/GitHub login
   - Social authentication

---

## 📚 Quick Reference

### Common Commands

```bash
# Start app
./start_reflex.sh

# Check database
sqlite3 reflex.db ".tables"

# View users
sqlite3 reflex.db "SELECT * FROM localuser;"

# View sessions
# sqlite3 reflex.db "SELECT * FROM localauthsession;"

# Clear all sessions (force logout everyone)
# sqlite3 reflex.db "DELETE FROM localauthsession;"

# Run migrations
reflex db migrate

# Create new migration
reflex db makemigrations --message "description"
```

### URLs

- **Login**: http://localhost:3000/Login
- **Account**: http://localhost:3000/Account (protected)
- **Home**: http://localhost:3000/Home
- **Backend API**: http://localhost:8000

### State Variables

```python
# In any component
AuthState.is_logged_in          # bool
AuthState.user_email            # str
AuthState.user_info             # dict
AuthState.authenticated_user    # User object or None
```

### Event Handlers

```python
# In components
on_click=AuthState.logout_and_redirect
on_click=AuthState.check_login_redirect
on_mount=ProtectedState.on_load
```

---

## 💡 Tips

### Development Tips

1. **Testing**: Create multiple test accounts to verify functionality
2. **Debugging**: Check browser console (F12) for errors
3. **Database**: Use DB Browser for SQLite for visual database management
4. **Logs**: Run with `reflex run --loglevel debug` for detailed logs

### Common Patterns

**Check if user is logged in:**
```python
rx.cond(
    AuthState.is_logged_in,
    rx.text(f"Hello {AuthState.user_email}"),
    rx.text("Please log in"),
)
```

**Conditional navigation:**
```python
rx.button(
    "Members Area",
    on_click=rx.cond(
        AuthState.is_logged_in,
        rx.redirect("/Members"),
        rx.redirect("/Login"),
    ),
)
```

**Show different content for logged-in users:**
```python
rx.cond(
    AuthState.is_logged_in,
    protected_content(),
    public_content(),
)
```

---

## ✅ Success Checklist

Your authentication is working if:

- [x] Database has `localuser` and `localauthsession` tables
- [x] Can register new account
- [x] Can login with credentials
- [x] Navbar shows username when logged in
- [x] Account page accessible after login
- [x] Account page redirects to login when logged out
- [x] Session persists after page refresh
- [x] Logout clears session and redirects

**If all checked: Your authentication system is fully functional!** 
---

## 📞 Resources

- **reflex-local-auth**: https://github.com/reflex-dev/reflex-local-auth
- **Reflex Docs**: https://reflex.dev/docs/
- **Full Setup Guide**: See `AUTH_SETUP_GUIDE.md` for detailed documentation
- **Troubleshooting**: See `TROUBLESHOOTING.md` for common issues

---

**Created**: 2025-02-12  
**Your authentication system is ready to use!**
