import reflex as rx

config = rx.Config(
    app_name="shell",
    disable_plugins="reflex.plugins.sitemap.SitemapPlugin",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)
