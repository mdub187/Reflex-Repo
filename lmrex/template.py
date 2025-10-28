# ## root level template.py
# # /lmrex/template.py

# from typing import Callable
# import reflex as rx


# from .components.menu import menu
# from .components.navbar import navbar
# from .components.footer import footer
# from .components.color_mode import color_mode
# from .components.heading import header
# from .components.user_login import user_login
# from .components.debug.debug_modal import debug_modal


# # from .components.heading import heading
# class State(rx.State):
#     label: str = "LMREX"


# class Template(rx.Component):
#     def __init__(self):
#         super().__init__()
#         self.state = State()
#         # return (self)


# def template(child: rx.Component, args, **kwargs) -> rx.Component:
#     # print([type(x) for x in args])
#     if not isinstance(child, rx.Component):
#         child = rx.heading("Invalid child", size="9")
#     return rx.container(
#         child,
#         # rx.flex(),
#         # args,
#         print("Debug: user_login component included in template"),  # Debug log
#         user_login(),  # Include the user_login component
#         debug_modal(),  # Include the debug_modal component for testing
#         navbar(),
#         # color_mode(),
#         # rx.heading(
#         #     State.label,
#         #     size="9",
#         #     style={
#         #         "background_color": "#667eea",
#         #         "color": "white",
#         #         "border_radius": "8px",
#         #         "padding": "0.75rem 2rem",
#         #         "margin_top": "1rem",
#         #     },
#         # ),
#         # min_height="50vh",
#         # footer(),
#         # color_mode(),
#         print("Debug: Template rendering completed"),  # Debug log
#     )
#     return template


# if __name__ == "__main__":
#     print(template)
