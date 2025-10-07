# rxconfig.py
import reflex as rx

config = rx.Config(
    app_name="lmrex",
    styles=[
        "styles.css",
        "./styles/styles.css",
    ],
    plugins=[
        rx.plugins.TailwindV4Plugin(),
    ],
    disable_plugins=[
        "reflex.plugins.sitemap.SitemapPlugin",
    ],
)
