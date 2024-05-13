from abc import  ABC, abstractmethod


class ParkingStrategy(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def find_parking_space(self, cls):
        pass
