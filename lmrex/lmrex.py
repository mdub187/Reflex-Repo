import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from .imports import rx
from .pages.index import index
from .pages.about import about
# from .pages.gallery import gallery
# Add the project root to the python path

app = rx.App()
app.add_page(index, route="/index")
app.add_page(about, route="/about")
# app.add_page(gallery, route="/gallery")
