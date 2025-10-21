# ./lmrex/components/navbar.py
import reflex as rx
from .user_login import user_login

# Optional: small FastAPI demo endpoint to verify tokens.
# Placed here for convenience per request; you may want to move this
# to a dedicated server module (e.g., `server/auth.py`) in production.
from fastapi import APIRouter, Request, HTTPException
from lmrex.logic.auth import get_user_from_token, is_signed_in

api_router = APIRouter()


def navbar_link(text, url) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium", display="contents"), href=url
    )


def navbar() -> rx.Component:
    return rx.container(
        rx.box(),
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/music-notes-minus-thin.svg",
                        width="2.25em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading("We Gon", size="7", weight="bold"),
                    width="100%",
                ),
                rx.hstack(
                    rx.link("home", href="/"),
                    rx.link("about", href="/About"),
                    rx.link("gallery", href="/Gallery"),
                    rx.link("contact", href="/Contact"),
                    rx.link("secret", href="/secret"),
                    rx.link(user_login(), create_account=True, spacing="5"),
                ),
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/music-notes-minus-thin.svg",
                        width="1.5em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading("B alright", size="7", weight="bold"),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(rx.icon("menu", size=30)),
                    rx.menu.content(
                        rx.menu.item("Home"),
                        rx.menu.item("About"),
                        rx.menu.item("Gallery"),
                        rx.menu.item("Contact"),
                        rx.menu.item("Secret"),
                        rx.menu.item("Login"),  # could hook modal here too
                    ),
                ),
            ),
        ),
        bg=rx.color("accent", 3),
        top="2px",
        z_index="5",
    )


# --- Small FastAPI demo endpoint to verify a Clerk token (server-side) ---
# This endpoint verifies a token using the existing `get_user_from_token`.
# It returns 401 if missing/invalid, or basic user info when valid.
@api_router.get("/api/verify-token")
async def verify_token(request: Request):
    # Try Authorization header first, then a cookie fallback.
    auth_header = request.headers.get("Authorization")
    token = None
    if auth_header and auth_header.startswith("Bearer "):
        token = auth_header.split(" ", 1)[1]
    else:
        # You could also pass a token via a cookie named 'auth_token'
        token = request.cookies.get("auth_token")

    if not token:
        raise HTTPException(status_code=401, detail="Missing token")

    user = get_user_from_token(token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")

    return {"ok": True, "user": {"id": user.id, "email": user.email}}
