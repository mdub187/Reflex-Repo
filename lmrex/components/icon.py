import reflex as rx


class State(rx.State):
    def icon(self) -> rx.Component:
        return
        rx.image(
            src="'../music-notes-minus-thin.svg'",
            width="2em",
            height="auto",
            border_radius="25%",
        )


if __name__ == "__main__":
    print(rx.image)
