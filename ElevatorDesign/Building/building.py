from ElevatorDesign.Floor.floors import Floors


class Buildings:
    _floors: list[Floors]

    def __init__(self, floor_list):
        Buildings._floors.extend(floor_list)

    def add_floor(self, floor: Floors):
        Buildings._floors.append(floor)

    def remove_floor(self, floor: Floors):
        Buildings._floors.remove(floor)

    def get_floor_list(self):
        return Buildings._floors
