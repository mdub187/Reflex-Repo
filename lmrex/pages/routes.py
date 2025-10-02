import reflex as rx


def index():
    return rx.text("")


def about():
    return rx.text("About Page")


def custom():
    return rx.text("Custom Route")


app = rx.App()

app.add_page(index)
app.add_page(about)
app.add_page(custom, route="/custom-route")
