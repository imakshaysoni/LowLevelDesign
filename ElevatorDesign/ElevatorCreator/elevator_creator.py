from ElevatorDesign.ElevatorCar.elevator_car import ElevatorCar
from ElevatorDesign.ElevatorController.elevator_controller import ElevatorController


class ElevatorCreator:
    elevator_controller_list: [ElevatorController]

    @classmethod
    def create_elevators(cls):
        # Creating Elevator 1
        elevator1 = ElevatorCar()
        controller1 = ElevatorController(elevator1)

        # Creating Elevator 2
        elevator2 = ElevatorCar()
        controller2 = ElevatorController(elevator2)

        cls.elevator_controller_list.append(controller1)
        cls.elevator_controller_list.append(controller2)