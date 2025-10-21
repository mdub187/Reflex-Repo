# lmrex/logic/user_store.py
"""
User store helpers for creating/verifying users and managing tokens.

This module provides a small, secure helper layer on top of SQLModel-based
`User` model for common user operations used by the demo application.

Features:
- Create user (password hashing)
- Authenticate user (password verify)
- Create / store / clear tokens (store hashed token in DB)
- Lookup user by email, id, or token

Security notes:
- Passwords are hashed with bcrypt (if available). If bcrypt is not installed,
  the module will fall back to PBKDF2-HMAC (sha256) with a reasonable iteration
  count. For production, always prefer a modern KDF such as bcrypt or argon2.
- Raw tokens are never stored in the DB; only their SHA-256 hash is stored.
  If the DB is leaked, raw tokens remain secret.
- Add token expiry or revocation metadata to the model in production.
"""

from __future__ import annotations

import hashlib
import secrets
import time
from typing import Optional

try:
    import bcrypt  # type: ignore

    _HAS_BCRYPT = True
except Exception:
    _HAS_BCRYPT = False

from sqlmodel import Session, select
from lmrex.models.user_model import User, NewUser
from lmrex.db import get_engine


# -----------------------
# Password hashing helpers
# -----------------------
def _hash_password_bcrypt(password: str) -> str:
    """Hash a password using bcrypt and return a UTF-8 decoded hash."""
    raw = password.encode("utf-8")
    hashed = bcrypt.hashpw(raw, bcrypt.gensalt())
    return hashed.decode("utf-8")


def _verify_password_bcrypt(password: str, hashed: str) -> bool:
    """Verify a bcrypt-hashed password."""
    try:
        return bcrypt.checkpw(password.encode("utf-8"), hashed.encode("utf-8"))
    except Exception:
        return False


def _hash_password_pbkdf2(password: str, salt: Optional[bytes] = None) -> str:
    """
    PBKDF2-HMAC-SHA256 fallback for environments where bcrypt is unavailable.

    The returned string is formatted as: iterations$salt_hex$hash_hex
    """
    iterations = 200_000
    salt = salt or secrets.token_bytes(16)
    dk = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, iterations)
    return f"{iterations}${salt.hex()}${dk.hex()}"


def _verify_password_pbkdf2(password: str, stored: str) -> bool:
    try:
        parts = stored.split("$")
        if len(parts) != 3:
            return False
        iterations = int(parts[0])
        salt = bytes.fromhex(parts[1])
        expected = parts[2]
        dk = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, iterations)
        return dk.hex() == expected
    except Exception:
        return False


def hash_password(password: str) -> str:
    """
    Hash a plaintext password using the best available KDF.

    Returns:
        A string representing the hashed password.
    """
    if _HAS_BCRYPT:
        return _hash_password_bcrypt(password)
    else:
        # PBKDF2 fallback
        return _hash_password_pbkdf2(password)


def verify_password(password: str, hashed: str) -> bool:
    """
    Verify a plaintext password against a stored hash.
    """
    if _HAS_BCRYPT:
        return _verify_password_bcrypt(password, hashed)
    else:
        return _verify_password_pbkdf2(password, hashed)


# -----------------------
# Token helpers
# -----------------------
def _hash_token(token: str) -> str:
    """
    Hash a token using SHA-256 for safe storage.
    """
    return hashlib.sha256(token.encode("utf-8")).hexdigest()


def generate_token(length: int = 32) -> str:
    """
    Generate a secure random token suitable for session use.
    """
    # token_urlsafe uses ~1.3x entropy per character length, but it's fine for demo tokens.
    return secrets.token_urlsafe(length)


# -----------------------
# DB-backed user helpers
# -----------------------
def create_user(name: str, email: str, password: str) -> User:
    """
    Create a new user with hashed password. Returns the created User model.

    Note: This does not check for duplicate emails; callers should enforce uniqueness
    if desired.
    """
    engine = get_engine()
    hashed = hash_password(password)
    user = User(name=name or "", email=email or "", password=hashed, token="")
    with Session(engine) as session:
        session.add(user)
        session.commit()
        session.refresh(user)
        return user


def get_user_by_email(email: str) -> Optional[User]:
    """Return the first user matching the given email or None."""
    engine = get_engine()
    with Session(engine) as session:
        stmt = select(User).where(User.email == email)
        result = session.exec(stmt).first()
        return result


def get_user_by_id(user_id: int) -> Optional[User]:
    """Return a user by primary key id or None."""
    engine = get_engine()
    with Session(engine) as session:
        user = session.get(User, user_id)
        return user


def authenticate_user(email: str, password: str) -> Optional[User]:
    """
    Authenticate a user by email and password.

    Returns the User on success, otherwise None.
    """
    user = get_user_by_email(email)
    if not user:
        return None
    if verify_password(password, user.password):
        return user
    return None


def set_user_token(user_id: int, raw_token: Optional[str]) -> Optional[User]:
    """
    Set (or clear) a user's token in the DB.

    - If `raw_token` is provided, stores its SHA-256 hash in the user's `token` field.
    - If `raw_token` is None or empty, clears the token.
    Returns the updated User or None if the user wasn't found.
    """
    engine = get_engine()
    with Session(engine) as session:
        user = session.get(User, user_id)
        if not user:
            return None
        if raw_token:
            user.token = _hash_token(raw_token)
        else:
            user.token = ""
        session.add(user)
        session.commit()
        session.refresh(user)
        return user


def generate_and_set_token(user_id: int, length: int = 32) -> Optional[str]:
    """
    Generate a new secure token, store its hash on the user row, and return the raw token.

    Returns None if the user does not exist.
    """
    raw = generate_token(length)
    updated = set_user_token(user_id, raw)
    if updated is None:
        return None
    return raw


def get_user_by_token(raw_token: str) -> Optional[User]:
    """
    Look up a user by a raw token by hashing the raw token and searching the DB.
    Returns the matching User or None.
    """
    if not raw_token:
        return None
    hashed = _hash_token(raw_token)
    engine = get_engine()
    with Session(engine) as session:
        stmt = select(User).where(User.token == hashed)
        return session.exec(stmt).first()


def clear_user_token(user_id: int) -> Optional[User]:
    """Clear a user's token and return the updated user object."""
    return set_user_token(user_id, None)


# -----------------------
# Convenience / utility
# -----------------------
def ensure_user_exists(email: str, name: str = "", password: str = "password") -> User:
    """
    Ensure a user with the given email exists. If not, create one using the
    provided name/password. Returns the existing or newly-created User.
    """
    existing = get_user_by_email(email)
    if existing:
        return existing
    return create_user(name=name or email.split("@")[0], email=email, password=password)


# Small demonstration helper (not used by server code path directly):
def demo_create_user_and_token(email: str = "demo@example.com") -> tuple[User, str]:
    """
    Create a demo user (or use existing) and generate a token for it.
    Returns (User, raw_token).
    """
    user = ensure_user_exists(email=email, name="Demo User", password="demo")
    token = generate_and_set_token(user.id)
    # token may be None if user creation failed unexpectedly; ensure we return a string
    return user, token or ""


# End of file
