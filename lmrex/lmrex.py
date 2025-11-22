from lmrex.routes.routes import add_routes, app
from lmrex.ui.responsive_utils import apply_responsive_styles

# Build the app once
add_routes()

if __name__ == "__main__":
    apply_responsive_styles()
    print("Hello, World!")
