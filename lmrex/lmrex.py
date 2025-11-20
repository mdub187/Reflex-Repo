# ## Root level lmrex.py

# import sys

from lmrex.routes.routes import add_routes

# responsive_styles = apply_responsive_styles()

# path = "/Users/mdub/Documents/Dev End/User Python/Reflex_pylot/lmrex"
# print(path)
# sys.path.append(path)


# sys.path.append(".")
# sys.path.append("lmrex")


# print(sys.path)
app = add_routes()

# app()
# add_routes(app)


if __name__ == "__main__":
    app.run()
    # print("Hello, World!")
