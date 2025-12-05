# rxconfig.py
import reflex as rx

config = rx.Config(
    app_name="lmrex",
    stylesheets=[
        "assets/styles.css",
        "assets/styles/styles.css",
        ".web/styles/tailwind.css",
    ],
    # rx run --port 8080,
    plugins=[
        rx.plugins.TailwindV4Plugin(),
    ],
    disable_plugins=[
        "reflex.plugins.sitemap.SitemapPlugin",
    ],
)
