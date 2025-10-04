import reflex as rx


class State(rx.State):
    """The app state."""

    label: str = "Be"
    label_arr: list[str] = ["Be", "Alright"]

    def change_label(self):
        if self.label == self.label_arr[0]:
            self.label = self.label_arr[1]
        else:
            self.label = self.label_arr[0]

    def handle_input_change(self, value: str):
        self.label = value
