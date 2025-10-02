import reflex as rx
from rxconfig import config
from .components import heading, input, menu, navbar
# config = config.styles

# styles = [
# ".rt-ContainerInner rt-Flex": {
#     "display": "100%",
# ".rt-ContainerInner": {
#     "display": "contents",
#     "width": "100%",
#     "body": {"display": "contents"},
# ]
# "breakpoints": ["30em", "48em", "62em", "80em"],
# "stylesheets": config,
# Default Reflex breakpoints

# styles.append({"style": {"width": "100%", "body": {"display": "contents"}}})
# print(styles)


# class State(rx.State):
#     """The app state."""

#     label: str = "Be"
#     label_arr: list[str] = ["Be", "Alright"]

#     def change_label(self):
#         if self.label == self.label_arr[0]:
#             self.label = self.label_arr[1]
#         else:
#             self.label = self.label_arr[0]
#             # add a for or while loop here iterating through an entire sentence as described in the label_arr
#             # for i in range(len(self.label_arr)):
#             #     self.label_arr[i] = self.label_arr[i].upper()
#             # self.label_arr = [label.upper() for label in self.label_arr]

#     def handle_input_change(self, value: str):
#         self.label = value


def base_page() -> rx.Component:
    return rx.box(
        rx.vstack(
            # config.styles,
            rx.box(
                # display="contents",
                # justify_self="none",
            ),
            # rx.text("This is the base page"),
            # rx.color_mode.button(position="bottom-right", id="my_light_mode"),
            # vwh="100%",
        ),
    )


print(base_page())


def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium", display="contents"), href=url
    )


def navbar() -> rx.Component:
    return rx.container(
        rx.box(),
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="../music-notes-minus-thin.svg",
                        width="2.25em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading("Web App Example", size="7", weight="bold"),
                    # align_items="center",
                    # justify="start",
                    width="100%",
                ),
                rx.hstack(
                    navbar_link("Home", "/#"),
                    navbar_link(
                        "About", "/#"
                    ),  # adding a link ... replace the "/#" with a https://+{link}
                    navbar_link("Pricing", "/#"),
                    navbar_link("Contact", "/#"),
                    # justify="end",
                    spacing="5",
                ),
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="'../music-notes-minus-thin.svg'",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading("Dumbass Shit", size="6", weight="bold"),
                    align_items="center",
                ),
                rx.menu,
                # rx.menu.root(
                #     rx.menu.trigger(rx.icon("menu", size=30)),
                #     rx.menu.content(
                #         rx.menu.item("Home"),
                #         rx.menu.item("About"),
                #         rx.menu.item("Pricing"),
                #         rx.menu.item("Contact"),
                #     ),
                # justify="content",
                # ),
                # justify="between",
                # align_items="center",
                # width="100%",
            ),
            # max_width="890px",
        ),
        bg=rx.color("accent", 3),
        # padding="1em",
        justify_self="normal",
        # position="dynamic",
        top="0px",
        z_index="5",
        # width="100%",
    )


print(navbar())


def index() -> rx.Component:
    return rx.box(
        rx.flex(),
        navbar(),
        rx.heading(),
        rx.vstack(
            # rx.heading(State.label, size="9"),
            rx.text(
                "This gon' b alright ...",
                rx.code({"./"}),
                size="5",
            ),
            rx.input(input),
            #     placeholder="type some shit",
            #     on_change=State.handle_input_change,
            # ),
            rx.button(),
            # "Lizzard", on_click=State.change_label),
            #     spacing="5",
            #     justify_self="none",
            #     min_height="85vh",
            # ),
            rx.color_mode.button(),
            # position="bottom-center", width="100%"),
            # justify_self="normal",
            # padding_top="1em",
            # display="contents",
        ),
    )


# <div class="rt-Container rt-r-size-3 css-8hu8q1"><div class="rt-ContainerInner"><div class="rt-Flex"></div><div class="rt-Container rt-r-size-3 css-v7vd4t"><div class="rt-ContainerInner"><div class="rt-Box css-1v8fzbk"><div class="rt-Flex rt-r-fd-row rt-r-ai-start rt-r-gap-3 rx-Stack"><div class="rt-Flex rt-r-fd-row rt-r-ai-start rt-r-gap-3 rx-Stack css-8atqhb"><img class="css-1jjl46k" src="../music-notes-minus-thin.svg"><h1 class="rt-Heading rt-r-size-7 rt-r-weight-bold">Dumbass Shit</h1></div><div class="rt-Flex rt-r-fd-row rt-r-ai-start rt-r-gap-5 rx-Stack"><a data-accent-color="" class="rt-Text rt-reset rt-Link rt-underline-auto css-1macts" href="/" data-discover="true"><p class="rt-Text rt-r-size-4 rt-r-weight-medium css-1obf64m">Home</p></a><a data-accent-color="" class="rt-Text rt-reset rt-Link rt-underline-auto css-1macts" href="/" data-discover="true"><p class="rt-Text rt-r-size-4 rt-r-weight-medium css-1obf64m">About</p></a><a data-accent-color="" class="rt-Text rt-reset rt-Link rt-underline-auto css-1macts" href="/" data-discover="true"><p class="rt-Text rt-r-size-4 rt-r-weight-medium css-1obf64m">Pricing</p></a><a data-accent-color="" class="rt-Text rt-reset rt-Link rt-underline-auto css-1macts" href="/" data-discover="true"><p class="rt-Text rt-r-size-4 rt-r-weight-medium css-1obf64m">Contact</p></a></div></div></div><div class="rt-Box css-1c1vcs0"><div class="rt-Flex rt-r-fd-row rt-r-ai-start rt-r-gap-3 rx-Stack"><div class="rt-Flex rt-r-fd-row rt-r-ai-start rt-r-gap-3 rx-Stack css-zcxndt"><img class="css-142dh2u" src="'../music-notes-minus-thin.svg'"><h1 class="rt-Heading rt-r-size-6 rt-r-weight-bold">Dumbass Shit</h1></div><svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-menu" type="button" id="radix-«r0»" aria-haspopup="menu" aria-expanded="false" data-state="closed"><path d="M4 5h16"></path><path... [truncated]

app = rx.App()
app.add_page(index)

# app.add_page(base_page)
