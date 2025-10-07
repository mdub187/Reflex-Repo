# lmrex/routes/routes.py

import reflex as rx
# from ..components.user_login import UserLogin, State
# def routes(self):
#     HOME_ROUTE = "/index"
#     ABOUT_ROUTE = "/about"
#     GALLERY_ROUTE = "/gallery"
#     CONTACT_ROUTE = "/contact"
#     return routes(self)
# app = routes


app = rx.App()


def routes():
    index = [app.add_page(route="/")];
    about = [app.add_page(route="/about")],
    gallery = [app.add_page(route="/gallery")],
    contact = [app.add_page(route="/contact")],
    # login = [app.UserLogin(State)]
