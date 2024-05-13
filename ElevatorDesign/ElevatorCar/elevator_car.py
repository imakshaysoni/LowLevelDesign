# Elevator Car is a dump object, it will do nothing except moving
from ElevatorDesign.Buttons.internal_buttons import InternalButtons
from ElevatorDesign.Display.display import Display
from ElevatorDesign.enums import Direction, Status


class ElevatorCar:
    _id = 0
    _current_floor = 0

    def __init__(self):
        ElevatorCar._id += 1
        self.id = ElevatorCar._id
        self.display = Display()
        self.internal_button = InternalButtons()
        self.direction = Direction.UP
        self.elevator_state = Status.IDLE

    def move(self, direction):
        pass
