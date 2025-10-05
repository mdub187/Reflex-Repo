# Entry point rxconfig.py

import reflex as rx


class Config(rx.Config):
    # app_name = ("lmrex",)
    app_module_import = "./lmrex/lmrex.py"
    styles = [
        "styles.css",
        "./styles/styles.css",
    ]  # make sure you actually have a styles.css file
    plugins = [
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]


config = Config(app_name="lmrex")
