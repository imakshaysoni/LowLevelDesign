from ParkingLotDesignPatternImplementation.ParkingSpotManager.parking_spot_manager import ParkingSpotManager
from ParkingLotDesignPatternImplementation.ParkingSpot.two_wheelar_parking_spot import TwoWheelerParkingSpot


class TwoWheelerParkingSpotManager(ParkingSpotManager):
    parking_spot_list = []

    def __init__(self, parking_strategy):
        super().__init__(parking_strategy)

    def find_parking_space(self):
        print(f"Finding parking Space for your two wheeler")
        return self.parking_strategy.find_parking_space(TwoWheelerParkingSpotManager)

    @staticmethod
    def add_parking_space(parking_spot_obj):
        TwoWheelerParkingSpotManager.parking_spot_list.append(parking_spot_obj)

    @staticmethod
    def remove_parking_space(parking_spot_obj):
        if parking_spot_obj in TwoWheelerParkingSpotManager.parking_spot_list:
            TwoWheelerParkingSpotManager.parking_spot_list.remove(parking_spot_obj)
