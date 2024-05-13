from ElevatorDesign.Dispatchers.external_button_dispatcher import ExternalButtonDispatcher


class ExternalButtons:

    def __init__(self, floor_number):
        self.direction = None
        self.floor = floor_number
        self.external_dispatcher = ExternalButtonDispatcher()

    def press_button(self, direction):
        self.direction = direction
        self.external_dispatcher.submit_request(self.floor, direction)

