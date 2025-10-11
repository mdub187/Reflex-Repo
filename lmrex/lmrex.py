# ## Root level lmrex.py

from lmrex.routes.routes import add_routes

app = add_routes()

if __name__ == "__main__":
    app.run()
