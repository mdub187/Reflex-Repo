# ## Root level lmrex.py

# import sys

from lmrex.routes.routes import add_routes, app
from lmrex.ui.responsive_utils import apply_responsive_styles

responsive_styles = apply_responsive_styles()


app()
add_routes(app)


if __name__ == "__main__":
    apply_responsive_styles()
    print(add_routes)
    print("Hello, World!")
