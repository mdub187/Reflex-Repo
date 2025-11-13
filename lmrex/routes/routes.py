# ./routes/routes.py
import reflex as rx

from lmrex.ui.about import about
from lmrex.ui.account import account
from lmrex.ui.contact import contact
from lmrex.ui.gallery import gallery
from lmrex.ui.gallery_music import gallery_music

# from lmrex.ui.gallery_pictures import gallery_pictures
# from lmrex.ui.gallery_video import gallery_video
from lmrex.ui.index import index
from lmrex.ui.login import login, user_login
from lmrex.ui.responsive_utils import apply_responsive_styles

app = rx.App()


def add_routes(self):
    # Register your pages with their components
    app.add_page(index, route="/")
    app.add_page(about, route="/about")
    app.add_page(contact, route="/contact")
    # app.add_page(login())

    # ✅ now these point to callable components
    app.add_page(gallery, route="/gallery")
    app.add_page(gallery_music, route="/gallery/music")

    app.add_page(user_login, route="/login/protected")
    app.add_page(account, route="/login/protected/account")

    apply_responsive_styles(*())

    app._compile()
    return app, add_routes
