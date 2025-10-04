import sys
import os

# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import reflex as rx
from .ui.index import index
from .ui.about import about
from .ui.gallery import gallery
from .components.navbar import navbar
from .nav import navlinks
from .template import pages


app = rx.App()
app.add_page(index, route="/")
app.add_page(about, route="/about")
app.add_page(gallery, route="/gallery")
if __name__ == "__main__":
    # app.compile()
    print("Hello, World!")
    print(app)
    print(navlinks())
# from .pages.gallery import gallery
# Add the project root to the python path
