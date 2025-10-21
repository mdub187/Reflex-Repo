# ./routes/routes.py

"""this is garfs"""

import reflex as rx

# Import your UI pages
from lmrex.ui.index import index
from lmrex.ui.about import about
from lmrex.ui.gallery import gallery
from lmrex.ui.contact import contact
from lmrex.ui.login import user_login
from lmrex.ui.account import account
from lmrex.ui.login import secret

app = rx.App()


def add_routes():
    # Register your pages with their components
    app.add_page(index, route="/")
    app.add_page(about, route="/about")
    app.add_page(gallery, route="/gallery")
    app.add_page(contact, route="/contact")
    app.add_page(user_login, route="/login")
    app.add_page(account, route="/login/account")
    app.add_page(secret, route="/secret")

    return app
