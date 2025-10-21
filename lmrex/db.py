# Reflex_pylot/lmrex/db.py
"""
Database engine and session helpers.

Provides:
- `get_engine(database_url=None, echo=False)`: create/return a SQLAlchemy engine
  configured for SQLModel usage. Respects `DATABASE_URL` env var when not passed.
- `init_db(engine=None)`: create database tables for SQLModel models.
- `get_session()`: generator context providing a SQLModel `Session` for use with
  `with` or as a dependency (yields a session and ensures close/cleanup).

Notes:
- For local development the default DATABASE_URL is `sqlite:///./data/app.db`.
  The helper will create the `./data` directory if necessary.
- In production you should use an external DB and a proper migration tool
  (Alembic) instead of `SQLModel.metadata.create_all`.
"""

from __future__ import annotations

import os
import pathlib
from typing import Generator, Optional

from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker


DEFAULT_SQLITE_PATH = "./data/app.db"
DEFAULT_DATABASE_URL = f"sqlite:///{DEFAULT_SQLITE_PATH}"


def _ensure_sqlite_parent_dir(database_url: str) -> None:
    """
    Ensure the parent directory for a local sqlite file exists.

    This is a no-op for non-sqlite URLs.
    """
    if not database_url.startswith("sqlite:///"):
        return

    # Extract local file path from URL: sqlite:///./data/app.db -> ./data/app.db
    path = database_url.replace("sqlite:///", "", 1)
    parent = pathlib.Path(path).resolve().parent
    if not parent.exists():
        parent.mkdir(parents=True, exist_ok=True)


def get_engine(database_url: Optional[str] = None, echo: bool = False) -> Engine:
    """
    Create and return a SQLAlchemy Engine configured for SQLModel.

    - `database_url`: optional DB URL. If not provided, uses `DATABASE_URL`
      env var or the default sqlite file.
    - `echo`: whether SQLAlchemy should log SQL statements (useful in dev).
    """
    database_url = (
        database_url
        or os.getenv("DATABASE_URL")
        or os.getenv("DATABASE_URL", DEFAULT_DATABASE_URL)
    )

    # If using a local sqlite file, ensure its directory exists.
    _ensure_sqlite_parent_dir(database_url)

    # SQLite requires a special connect_args for thread check when used in web apps.
    connect_args = {}
    if database_url.startswith("sqlite:///"):
        connect_args = {"check_same_thread": False}

    engine = create_engine(database_url, echo=echo, connect_args=connect_args)
    return engine


# Create a module-level default engine lazily if callers prefer to reuse it.
_default_engine: Optional[Engine] = None


def get_default_engine(echo: bool = False) -> Engine:
    """
    Return a cached default engine for the project. Creates it on first call.
    """
    global _default_engine
    if _default_engine is None:
        _default_engine = get_engine(echo=echo)
    return _default_engine


def init_db(engine: Optional[Engine] = None) -> Engine:
    """
    Initialize database tables using SQLModel.metadata.create_all.

    WARNING: For production use Alembic migrations instead of create_all.
    """
    engine = engine or get_default_engine()
    SQLModel.metadata.create_all(engine)
    return engine


# Helper: sessionmaker configured to produce SQLModel Session instances.
# We keep expire_on_commit=False to avoid unexpected attribute expiry after commit
# in typical web app usage.
def _get_session_factory(engine: Optional[Engine] = None):
    engine = engine or get_default_engine()
    return sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=Session)


def get_session(engine: Optional[Engine] = None) -> Generator[Session, None, None]:
    """
    Generator that yields a SQLModel `Session`. Use like:

    from lmrex.db import get_session
    for session in get_session():
        # use session

    or as a dependency-style helper in frameworks that accept generator deps.

    Example usage:
        with next(get_session()) as session:
            # use session

    Prefer the context manager pattern in your code:
        engine = get_engine()
        SessionLocal = _get_session_factory(engine)
        with SessionLocal() as session:
            ...

    The generator will close the session when it completes.
    """
    SessionLocal = _get_session_factory(engine)
    session: Session = SessionLocal()
    try:
        yield session
        # Commit could be done here if desired; keep explicit commit control in caller.
    finally:
        session.close()
