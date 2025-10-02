import reflex as rx

rx.menu.root(
    rx.menu.trigger(rx.icon("menu", size=30)),
    rx.menu.content(
        rx.menu.item("Home"),
        rx.menu.item("About"),
        rx.menu.item("Pricing"),
        rx.menu.item("Contact"),
    ),
)
