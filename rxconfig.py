import reflex as rx


class Config(rx.Config):
    app_name = "lmrex"
    styles = [
        "styles.css",
        "./styles/styles.css",
    ]  # make sure you actually have a styles.css file
    plugins = [
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]


config = Config(app_name="lmrex")
