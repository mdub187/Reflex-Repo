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
            # add a for or while loop here iterating through an entire sentence as described in the label_arr
            # for i in range(len(self.label_arr)):
            #     self.label_arr[i] = self.label_arr[i].upper()
            # self.label_arr = [label.upper() for label in self.label_arr]

    def handle_input_change(self, value: str):
        self.label = value
