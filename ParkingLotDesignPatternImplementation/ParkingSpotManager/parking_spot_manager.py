from abc import ABC, abstractmethod
from ParkingLotDesignPatternImplementation.ParkingSpot.parking_spot import ParkingSpot


class ParkingSpotManager(ABC):

    def __init__(self, parking_strategy):
        self.parking_strategy = parking_strategy

    @abstractmethod
    def find_parking_space(self):
        pass

    @staticmethod
    @abstractmethod
    def add_parking_space(parking_spot_obj: ParkingSpot):
        pass

    @staticmethod
    @abstractmethod
    def remove_parking_space(parking_spot_obj: ParkingSpot):
        pass
