from ElevatorDesign.ElevatorCar.elevator_car import ElevatorCar


class ElevatorController:
    _id = 0

    def __init__(self, elevator_obj: ElevatorCar):
        ElevatorController._id += 1
        self.id = ElevatorController._id
        self.elevator = elevator_obj

    def submit_request(self, floor, direction):
        # Actual Logic Implemented Here
        print(f"Moving to Floor {floor} and in direction {direction}")

    def control(self):
        pass
