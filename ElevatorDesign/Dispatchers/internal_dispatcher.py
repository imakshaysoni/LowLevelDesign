

class InternalDispatcher:
    _elevator_controller_list: [ElevatorCreator.elevator_controller_list]

    def __init__(self):
        pass

    def submit_request(self, elevator_id, floor_button, direction):
        elevator_controller_obj = self._elevator_controller_object(elevator_id)
        elevator_controller_obj.submit_request(floor_button, direction)

    def _elevator_controller_object(self, elevator_id):
        for elevator_controller in InternalDispatcher._elevator_controller_list:
            if elevator_controller.elevator.id == elevator_id:
                return elevator_controller
