# ./routes/routes.py

"""this is garfs"""

import reflex as rx

from lmrex.ui.about import about
from lmrex.ui.account import account
from lmrex.ui.contact import contact
from lmrex.ui.gallery import gallery

# from lmrex.ui.gallery_music import music
# from lmrex.ui.gallery_pictures import pictures
# from lmrex.ui.gallery_video import videos
# Import your UI pages
from lmrex.ui.index import index
from lmrex.ui.login import user_login

app = rx.App()


def add_routes():
    # Register your pages with their components
    app.add_page(index, route="/")
    app.add_page(about, route="/about")
    app.add_page(gallery, route="/gallery")
    app.add_page(contact, route="/contact")
    app.add_page(user_login, route="/login")
    # app.add_page(protected_page, route="/protected")
    app.add_page(account, route="/protected/account")
    # app.add_page(pictures, route="/gallery/pictures")
    # app.add_page(videos, route="/gallery/videos")
    # app.add_page(music, route="/gallery/music")
    return app
