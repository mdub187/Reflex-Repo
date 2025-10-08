# ## Root level lmrex.py
# # lmrex/lmrex.py

# import sys
# import os
# # Keep this statement in case you need path declarations.
# # sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# import reflex as rx
# from .ui.index import index
# from .ui.about import about
# from .ui.gallery import gallery
# from .ui.contact import contact
# # from .components.user_login import State
# # from .components.user_login import form_data as user_login
# from .components.navbar import navbar
# from .nav import navlinks


# # app = routes
# app = rx.App()
# app.add_page(index, route="/")
# app.add_page(about, route="/about")
# app.add_page(gallery, route="/gallery")
# app.add_page(contact, route="/contact")

# if __name__ == "__main__":
#     print("Hello, World!")
#     print(navlinks())
# """mine"""
#
# """garfs"""
from lmrex.routes.routes import add_routes

app = add_routes()

if __name__ == "__main__":
    app.run()
