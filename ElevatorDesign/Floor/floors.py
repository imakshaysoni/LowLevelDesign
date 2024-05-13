from ElevatorDesign.Buttons.external_buttons import ExternalButtons


class Floors:
    _id = 0

    def __init__(self):
        Floors._id += 1
        self.id = Floors._id
        self.external_button = ExternalButtons()

    def press_button(self, direction):
        self.external_button.press_button(direction)
