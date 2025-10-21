# ./lmrex/logic/auth.py

import os
from dataclasses import dataclass
import logging
from typing import Any, Optional

import httpx
from clerk_backend_api import Clerk
from clerk_backend_api.security import authenticate_request
from clerk_backend_api.security.types import AuthenticateRequestOptions


# Minimal, cleaned user representation returned by `get_user_from_token`.
@dataclass
class UserInfo:
    id: Optional[str] = None
    email: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    raw: Any = None


def is_signed_in(request: httpx.Request) -> bool:
    """
    Determine whether the incoming HTTP request is authenticated via Clerk.

    This function is defensive: it returns False when the Clerk secret key is
    not configured or when any verification step fails. It prefers using the
    SDK client's `authenticate_request` method and falls back to the helper
    function imported from `clerk_backend_api.security`.
    """
    secret_key = os.getenv("CLERK_SECRET_KEY")
    if not secret_key:
        logging.warning(
            "CLERK_SECRET_KEY not set; treating request as unauthenticated."
        )
        return False

    try:
        with Clerk(bearer_auth=secret_key) as sdk:
            try:
                request_state = sdk.authenticate_request(
                    request, AuthenticateRequestOptions(authorized_parties=["https://"])
                )
            except Exception:
                # Fallback: if the SDK instance doesn't expose `authenticate_request`
                # use the helper function imported from the security module.
                request_state = authenticate_request(
                    request, AuthenticateRequestOptions(authorized_parties=["https://"])
                )

        return bool(getattr(request_state, "is_signed_in", False))
    except Exception as exc:
        logging.exception("Error while checking sign-in status: %s", exc)
        return False


def get_user_from_token(token: str) -> Optional[UserInfo]:
    """
    Verify the provided Clerk token and return a cleaned `UserInfo` object.

    Behavior:
    - If `token` is falsy, returns None.
    - Uses the Clerk SDK to verify the token (prefer `clients.verify`).
    - If verification yields a user id, fetches the user with `users.get`.
    - Returns a `UserInfo` instance populated with a few common fields and the
      raw object from the Clerk SDK for callers that need more data.
    - All SDK calls are wrapped in robust exception handling so callers always
      receive either a `UserInfo` or `None`.
    """
    if not token:
        return None

    secret_key = os.getenv("CLERK_SECRET_KEY")
    if not secret_key:
        # Development behavior:
        # - Only use demo-token fallback when ALLOW_DEMO_TOKENS is explicitly enabled.
        # - This prevents accidental acceptance of demo tokens in environments
        #   where Clerk isn't configured (e.g., CI / production).
        allow_demo = os.getenv("ALLOW_DEMO_TOKENS", "false").strip().lower() in (
            "1",
            "true",
            "yes",
            "y",
        )
        if allow_demo and isinstance(token, str) and token.startswith("demo"):
            logging.warning(
                "CLERK_SECRET_KEY not set; ALLOW_DEMO_TOKENS enabled — using development fallback for demo token."
            )
            # Provide a minimal UserInfo for local/dev flows.
            demo_id = "demo-admin" if token == "demo-admin-token" else "demo-user"
            demo_email = (
                "admin@example.com"
                if token == "demo-admin-token"
                else "demo@example.com"
            )
            user_info = UserInfo(
                id=demo_id,
                email=demo_email,
                first_name="Demo",
                last_name="User",
                raw={"demo_token": token, "is_admin": token == "demo-admin-token"},
            )
            return user_info
        # If demo fallback is not allowed, log a clear message and return None.
        if not allow_demo:
            logging.warning(
                "CLERK_SECRET_KEY not set and ALLOW_DEMO_TOKENS not enabled; cannot verify token."
            )
        else:
            logging.warning("CLERK_SECRET_KEY not set; cannot verify token.")
        return None

    try:
        with Clerk(bearer_auth=secret_key) as sdk:
            verify_res = None
            try:
                # Preferred verification path (validates JWT/token and returns claims)
                verify_res = sdk.clients.verify(request={"token": token})
            except Exception:
                # If `clients.verify` is not available or fails, we'll try other strategies below.
                logging.debug(
                    "clients.verify failed or is unavailable; attempting alternative resolution."
                )

            user_id = None
            # Try to extract a user id in a few common ways
            if verify_res is not None:
                user_id = getattr(verify_res, "user_id", None)
                if user_id is None and isinstance(verify_res, dict):
                    user_id = verify_res.get("user_id") or verify_res.get("sub")
                if user_id is None:
                    user_id = getattr(verify_res, "sub", None)

            # Fallback: token might be a session id; try to fetch the session
            if user_id is None:
                try:
                    session = sdk.sessions.get(session_id=token)
                    user_id = getattr(session, "user_id", None) or getattr(
                        session, "user", None
                    )
                except Exception:
                    logging.debug("sessions.get did not resolve a user for the token.")

            if not user_id:
                logging.warning("Unable to verify token or determine user id.")
                return None

            # Fetch the user object from Clerk
            try:
                user = sdk.users.get(user_id=user_id)
            except Exception as exc:
                logging.exception("Failed to fetch user for id %s: %s", user_id, exc)
                return None

            if not user:
                logging.warning("No user returned for id %s", user_id)
                return None

            # Normalize a few common fields into UserInfo (defensive extraction)
            user_info = UserInfo(id=getattr(user, "id", None))
            email = None

            # Common shapes:
            # - `user.email_addresses` may be a list of objects/dicts
            # - `user.primary_email_address` or `user.email` may exist
            try:
                if hasattr(user, "email_addresses"):
                    emails = getattr(user, "email_addresses")
                    if isinstance(emails, (list, tuple)) and emails:
                        first = emails[0]
                        if isinstance(first, dict):
                            email = first.get("email") or first.get("email_address")
                        else:
                            email = getattr(first, "email_address", None) or getattr(
                                first, "email", None
                            )
            except Exception:
                email = None

            if not email:
                email = getattr(user, "primary_email_address", None) or getattr(
                    user, "email", None
                )

            user_info.email = email
            user_info.first_name = getattr(user, "first_name", None) or getattr(
                user, "given_name", None
            )
            user_info.last_name = getattr(user, "last_name", None) or getattr(
                user, "family_name", None
            )
            user_info.raw = user
            return user_info

    except Exception as exc:
        logging.exception("Unexpected error while verifying token: %s", exc)
        return None
