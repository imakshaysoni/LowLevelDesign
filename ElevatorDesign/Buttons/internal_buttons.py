from ElevatorDesign.Dispatchers.internal_dispatcher import InternalDispatcher


class InternalButtons:

    def __init__(self, id):
        self.available_buttons = {1, 2, 3, 4, 5, 6, 7}
        self.elevator_id = id
        self.internal_dispatcher = InternalDispatcher()

    def press_button(self, floor_button):
        self.internal_dispatcher.submit_request(self.elevator_id, floor_button)
