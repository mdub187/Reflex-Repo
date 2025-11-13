# lmrex/lmrex.py

from lmrex.routes.routes import add_routes, app
from lmrex.ui.responsive_utils import apply_responsive_styles

# Apply global responsive styles
apply_responsive_styles()

# Add all routes to the app
add_routes(app)

if __name__ == "__main__":
    # Optional: run Reflex dev server
    app.run()  # or reflex.run() if using CLI-style
    print("Hello, World! App is running...")
