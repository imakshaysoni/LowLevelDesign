from ElevatorDesign.ElevatorController.elevator_controller import ElevatorController


class ExternalButtonDispatcher:
    _elevator_controller_list: [ElevatorController]

    def __init__(self):
        pass

    def submit_request(self, floor, direction):
        for elevator_controller in ExternalButtonDispatcher._elevator_controller_list:
            elevator_controller.submit_request(floor, direction)
