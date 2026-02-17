# 🔐 Authentication Setup Guide

Complete guide for setting up token-based authentication in your Reflex app using `reflex-local-auth`.

---

## 📋 Overview

Your app now has a complete authentication system with:
-User registration with secure password hashing
-Login/logout with session token management
-Protected routes (Account page)
-Database-backed user storage
-Automatic token validation
-Navbar shows login status

---

## 🚀 Quick Start

### 1. **Initialize the Database**

The authentication system needs database tables. Run this command:

```bash
cd /Users/mdub/Documents/Git\ Repos/Reflex/Reflex-Repo

# Create/migrate the database
reflex db migrate
```

This creates the necessary tables:
- `localuser` - Stores user accounts
- `localauthsession` - Manages session tokens

### 2. **Start the Application**

```bash
./start_reflex.sh
```

### 3. **Test the Authentication**

1. **Navigate to Login Page**: http://localhost:3000/Login
2. **Create an Account**:
   - Click the "Register" tab
   - Enter a username (e.g., `testuser`)
   - Enter a password (e.g., `password123`)
   - Click "Register"
3. **Login**:
   - Switch to "Login" tab
   - Enter your username and password
   - Click "Login"
4. **Access Protected Page**:
   - After login, you'll be redirected to `/Account`
   - Or click "Account" in the navbar
5. **Logout**:
   - Click the logout button in navbar or on Account page

---

## 📁 Files Modified

### Core Authentication Files

1. **`lmrex/state/auth_state.py`** - Authentication state management
   - `AuthState` - Main auth state extending `reflex_local_auth.LocalAuthState`
   - `ProtectedState` - For protected pages with auto-redirect
   - Token management handled automatically

2. **`lmrex/ui/login.py`** - Login/Registration UI
   - Login form with username/password
   - Registration form
   - Status indicators
   - Built using `reflex_local_auth` components

3. **`lmrex/ui/account.py`** - Protected account page
   - Shows user information
   - Displays protected content
   - Requires authentication (auto-redirects if not logged in)

4. **`lmrex/components/navbar.py`** - Navigation with auth status
   - Shows logged-in username
   - Conditional Login/Logout buttons
   - Account link when authenticated

5. **`lmrex/middleware/auth_logic.py`** - Authentication utilities
   - Helper functions for future customization
   - Password hashing (handled by reflex-local-auth)

---

## 🔑 How Authentication Works

### Token Flow

1. **Registration**:
   ```
   User fills form → Password hashed → User saved to DB → Auto login → Token created
   ```

2. **Login**:
   ```
   User enters credentials → Password verified → Session token generated → Token stored in browser
   ```

3. **Protected Pages**:
   ```
   Page loads → Token validated → User data loaded → Page renders
   If no token → Redirect to /Login
   ```

4. **Logout**:
   ```
   Logout clicked → Token cleared → Session deleted → Redirect to /Home
   ```

### Database Schema

**`localuser` table**:
```sql
id              INTEGER PRIMARY KEY
username        TEXT UNIQUE NOT NULL
password_hash   TEXT NOT NULL
enabled         BOOLEAN DEFAULT TRUE
```

<!--**`localauthsession` table**:
```sql
id              INTEGER PRIMARY KEY
user_id         INTEGER FOREIGN KEY → localuser.id
session_id      TEXT UNIQUE NOT NULL
expiration      DATETIME NOT NULL
```-->

---

## 🛠️ Customization

### Change Session Expiration

Edit `rxconfig.py`:
```python
config = rx.Config(
    # ... existing config
    redis_token_expiration=7200,  # 2 hours in seconds (default: 3600)
)
```

### Add User Roles/Permissions

Extend the `AuthState` in `lmrex/state/auth_state.py`:

```python
class AuthState(reflex_local_auth.LocalAuthState):
    # Add custom fields
    user_role: str = "user"
    
    @rx.var
    def is_admin(self) -> bool:
        """Check if user has admin role"""
        return self.user_role == "admin"
    
    @rx.event
    def load_user_role(self):
        """Load user role from database"""
        if self.authenticated_user:
            # Custom logic to fetch role
            self.user_role = "admin"  # or fetch from DB
```

### Add Email to Users

Modify `lmrex/models/user_model.py`:

```python
class LocalUser(SQLModel, table=True, extend_existing=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    password_hash: str
    enabled: bool = True
    email: Optional[str] = None  # Add email field
```

Then run migration:
```bash
reflex db makemigrations --message "add email to users"
reflex db migrate
```

### Protect More Pages

Use `ProtectedState` in any page that needs authentication:

```python
# lmrex/ui/my_protected_page.py
import reflex as rx
from lmrex.state.auth_state import ProtectedState

def my_protected_page() -> rx.Component:
    return rx.box(
        rx.text("This is protected!"),
        rx.text(ProtectedState.protected_data),
        on_mount=ProtectedState.on_load,  # Checks auth and redirects if needed
    )
```

---

## 🧪 Testing

### Manual Testing

1. **Registration**:
   - Go to http://localhost:3000/Login
   - Register tab → Create account with `user1` / `pass123`
   - Should auto-login and redirect to Account page

2. **Login**:
   - Logout
   - Login tab → Enter `user1` / `pass123`
   - Should redirect to Account page
   - Navbar should show username

3. **Protected Page Access**:
   - Without login: Visit http://localhost:3000/Account
   - Should redirect to login page
   - After login: Can access Account page

4. **Session Persistence**:
   - Login
   - Refresh page
   - Should stay logged in (token in browser)

5. **Logout**:
   - Click logout in navbar or Account page
   - Should redirect to Home
   - Navbar should show "Login" button

### Database Testing

Check users in database:

<!--```bash
# Using sqlite3
sqlite3 reflex.db

# List all users
SELECT * FROM localuser;

# List active sessions
SELECT * FROM localauthsession;

# Exit
.exit
```-->

### Programmatic Testing

Run the test suite (if you add tests):

```bash
pytest lmrex/tests/test_auth_state.py -v
```

---

## 🐛 Troubleshooting

### Issue: "Table localuser doesn't exist"

**Solution**:
```bash
reflex db migrate
```

### Issue: "Can't login after registration"

**Symptoms**: Registration succeeds but login fails

**Solution**:
- Check database was created: `ls -la reflex.db`
- Run migration: `reflex db migrate`
- Check user exists:
  ```bash
  sqlite3 reflex.db "SELECT * FROM localuser;"
  ```

### Issue: "Token not persisting"

**Symptoms**: Login works but refresh logs you out

**Solution**:
- Check browser cookies are enabled
- Check `redis_token_expiration` in rxconfig.py
- Clear browser cache and try again

### Issue: "Protected page doesn't redirect"

**Symptoms**: Can access Account page without logging in

**Solution**:
- Make sure page uses `ProtectedState`
- Add `on_mount=ProtectedState.on_load` to the page component
- Check that page is using the correct state

### Issue: "Password not hashing"

**Symptoms**: Can see plain passwords in database

**Solution**:
- Ensure using `reflex_local_auth.register_form()` 
- Never use custom registration without hashing
- Check reflex-local-auth version: `pip list | grep reflex-local-auth`

---

## 🔒 Security Best Practices

### DO 
1. **Use HTTPS in production** - Never send passwords over HTTP
2. **Set strong session expiration** - Default 1 hour is good
3. **Validate user input** - Check username/password requirements
4. **Use environment variables** - For database URLs and secrets
5. **Enable CORS properly** - Only allow trusted origins
6. **Log authentication events** - Track logins/logouts for security
7. **Implement rate limiting** - Prevent brute force attacks
8. **Regular security updates** - Keep reflex and dependencies updated

### DON'T 
1. **Don't store passwords in plain text** - Always hash (done automatically)
2. **Don't expose session tokens** - They're managed securely
3. **Don't share database files** - Add `*.db` to .gitignore (already done)
4. **Don't use weak passwords** - Enforce password requirements
5. **Don't trust client-side validation** - Always validate on backend
6. **Don't log sensitive data** - No passwords or tokens in logs
7. **Don't use default credentials** - In production, use strong passwords

---

## 📊 Database Management

### View Users

```bash
sqlite3 reflex.db "SELECT id, username, enabled FROM localuser;"
```

### Create Admin User Manually

```bash
sqlite3 reflex.db
```

```sql
-- First, you need the hashed password
-- Use Python to generate it:
```

```python
from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
hashed = pwd_context.hash("admin_password_123")
print(hashed)
```

```sql
-- Then insert into database
INSERT INTO localuser (username, password_hash, enabled) 
VALUES ('admin', '<hashed_password_here>', 1);
```

### Reset User Password

```python
# In Python shell or a script
from passlib.context import CryptContext
import sqlite3

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
new_password_hash = pwd_context.hash("new_password")

conn = sqlite3.connect('reflex.db')
cursor = conn.cursor()
cursor.execute(
    "UPDATE localuser SET password_hash = ? WHERE username = ?",
    (new_password_hash, "username_here")
)
conn.commit()
conn.close()
```

### Clear All Sessions (Force Logout All Users)

<!--```bash
sqlite3 reflex.db "DELETE FROM localauthsession;"
```

### Delete User

```bash
sqlite3 reflex.db "DELETE FROM localuser WHERE username = 'testuser';"
```-->

---

## 🎯 Next Steps

### Recommended Enhancements

1. **Email Verification**
   - Add email field to user model
   - Send verification emails
   - Verify before allowing login

2. **Password Reset**
   - Generate reset tokens
   - Send reset emails
   - Create password reset page

3. **Two-Factor Authentication (2FA)**
   - Add TOTP support
   - Use libraries like `pyotp`

4. **OAuth Integration**
   - Add Google/GitHub login
   - Use `authlib` or similar

5. **User Profile**
   - Create profile edit page
   - Allow username/email changes
   - Add avatar upload

6. **Admin Panel**
   - Create admin-only pages
   - User management interface
   - View/edit/delete users

7. **Audit Logging**
   - Log all auth events
   - Track login attempts
   - Monitor suspicious activity

8. **Rate Limiting**
   - Limit login attempts
   - Prevent brute force
   - Use Redis for tracking

---

## 📚 Reference

### reflex-local-auth Documentation
- GitHub: https://github.com/reflex-dev/reflex-local-auth
- PyPI: https://pypi.org/project/reflex-local-auth/

### Key Components Used

```python
# From reflex-local-auth
reflex_local_auth.LocalAuthState          # Base auth state
reflex_local_auth.LoginState             # Login handler
reflex_local_auth.login_form()           # Login UI
reflex_local_auth.register_form()        # Registration UI
```

### State Variables Available

```python
# In AuthState (extends LocalAuthState)
self.is_authenticated      # bool - Is user logged in?
self.authenticated_user    # User object or None
self.authenticated_user.username   # Username
self.authenticated_user.id         # User ID
self.authenticated_user.enabled    # Account enabled?
```

### Event Handlers

```python
# Login/Logout
AuthState.on_submit_login         # Handle login form
AuthState.on_submit_register      # Handle registration
AuthState.do_logout()             # Logout user
AuthState.logout_and_redirect()   # Logout + redirect

# Custom events
AuthState.check_login_redirect()  # Check if logged in
ProtectedState.load_user_data()   # Load protected data
ProtectedState.on_load()          # Page load check
```

---

##Checklist

Before deploying to production:

- [ ] Run database migrations
- [ ] Test registration flow
- [ ] Test login flow  
- [ ] Test logout flow
- [ ] Test protected page access
- [ ] Test session persistence
- [ ] Enable HTTPS
- [ ] Set secure CORS origins
- [ ] Configure session expiration
- [ ] Add rate limiting
- [ ] Enable audit logging
- [ ] Set up monitoring
- [ ] Back up database regularly
- [ ] Document admin procedures
- [ ] Test password reset (if implemented)
- [ ] Security audit completed

---

**Created**: 2025-02-12  
**Last Updated**: 2025-02-12  
**Reflex Version**: 0.8.26  
**reflex-local-auth Version**: 0.4.0
