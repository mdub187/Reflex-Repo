#!/usr/bin/env python3
"""
lmrex/init_db.py

Initialize the SQLModel database and create a demo user + token for local development.

Usage:
    python -m lmrex.init_db
    python lmrex/init_db.py

Options:
    --email EMAIL     Email for the demo user (default: demo@example.com)
    --password PASS   Password for the demo user (default: demo)

What this script does:
 - Calls the project's DB initialization helper to create tables.
 - Ensures a demo user exists and generates a demo token for that user.
 - Prints the raw demo token to stdout so you can paste it into the client (or set it
   in localStorage) for testing protected routes.

Security:
 - This script is intended for local development only. Do NOT run in production
   unless you understand the consequences and have configured a secure DATABASE_URL
   and proper migrations.
"""

from __future__ import annotations

import argparse
import sys
import textwrap

# Import project helpers. These modules should exist in the lmrex package.
# The script intentionally relies on the project's existing DB and user_store helpers.
try:
    from lmrex.db import init_db as project_init_db
    from lmrex.logic.user_store import demo_create_user_and_token
except Exception as exc:  # pragma: no cover - helpful debug output if imports fail
    print(
        "Failed to import project helpers. Make sure you run this from the project root.",
        file=sys.stderr,
    )
    print("Error:", repr(exc), file=sys.stderr)
    sys.exit(2)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Initialize DB and create a demo user + token for local development."
    )
    parser.add_argument("--email", default="demo@example.com", help="Demo user email")
    parser.add_argument(
        "--password",
        default="demo",
        help="Demo user password (used only if user must be created)",
    )
    args = parser.parse_args(argv)

    # Initialize DB (creates tables)
    print("Initializing database (creating tables if needed)...")
    try:
        engine = project_init_db()
    except Exception as exc:  # pragma: no cover
        print("Database initialization failed:", file=sys.stderr)
        print(repr(exc), file=sys.stderr)
        return 2

    print("Database initialized.")

    # Ensure demo user exists and generate a token
    print(f"Ensuring demo user exists and generating a token for {args.email}...")
    try:
        user, token = demo_create_user_and_token(email=args.email)
    except Exception as exc:  # pragma: no cover
        print("Failed to create demo user or token:", file=sys.stderr)
        print(repr(exc), file=sys.stderr)
        return 3

    if not token:
        print("Failed to generate a demo token.", file=sys.stderr)
        return 4

    # Print helpful output
    print()
    print("Demo user created / ensured:")
    print(f"  id:    {getattr(user, 'id', '<unknown>')}")
    print(f"  email: {getattr(user, 'email', args.email)}")
    print()
    print(
        "Raw demo token (copy this into your client's localStorage or use it in requests):"
    )
    print()
    print(textwrap.indent(token, "  "))
    print()
    print(
        "IMPORTANT: This token is for local development only. Do NOT use in production."
    )
    print()
    print("You can enable the lightweight demo-token fallback in the app by setting:")
    print("  export ALLOW_DEMO_TOKENS=true")
    print("and ensuring CLERK_SECRET_KEY is not set (for demo flows).")
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
