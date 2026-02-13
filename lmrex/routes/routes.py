# ./routes/routes.py

import reflex as rx

from lmrex.ui.about import about
from lmrex.ui.contact import contact
from lmrex.ui.gallery import gallery
from lmrex.ui.index import index
from lmrex.ui.login import login
# from lmrex.ui.login import user_login
from lmrex.ui.account import account_page
from lmrex.ui.login import login

# from lmrex.ui.gallery_music import music
# from lmrex.ui.gallery_pictures import pictures
# from lmrex.ui.gallery_video import videos
# Import your UI pages

app = rx.App()
# index = "/Home"
def add_routes():
    # Register your pages with their components
    app.add_page(index, route="/Home")
    app.add_page(about, route="/About")
    app.add_page(gallery, route="/Gallery")
    app.add_page(contact, route="/Contact")
    app.add_page(login, route="/Login")
    app.add_page(account_page, route="/Account")
    # app.add_page(pictures, route="/gallery/pictures")
    # app.add_page(videos, route="/gallery/videos")
    # app.add_page(music, route="/gallery/music")
    app._compile()
    return app
