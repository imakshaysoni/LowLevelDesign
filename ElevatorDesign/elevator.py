from ElevatorDesign.ElevatorCreator.elevator_creator import ElevatorCreator
from ElevatorDesign.Building.building import Buildings
from ElevatorDesign.Floor.floors import Floors
from ElevatorDesign.enums import Direction

if __name__ == "__main__":
    ElevatorCreator.create_elevators()
    floor_lists = [Floors]

    floor1 = Floors()
    floor2 = Floors()
    floor3 = Floors()
    floor4 = Floors()
    floor5 = Floors()
    floor6 = Floors()
    floor7 = Floors()

    floor_lists.append(floor1)
    floor_lists.append(floor2)
    floor_lists.append(floor3)
    floor_lists.append(floor4)
    floor_lists.append(floor5)
    floor_lists.append(floor6)
    floor_lists.append(floor7)

    vaidehi_rivera = Buildings(floor_lists)

    floor7.press_button(Direction.UP)

