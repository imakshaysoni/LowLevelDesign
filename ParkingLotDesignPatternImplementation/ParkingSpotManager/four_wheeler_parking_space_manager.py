from ParkingLotDesignPatternImplementation.ParkingSpotManager.parking_spot_manager import ParkingSpotManager
from ParkingLotDesignPatternImplementation.ParkingSpot.four_wheeler_parking_spot import FourWheelerParkingSpot
from ParkingLotDesignPatternImplementation.ParkingSpot.parking_spot import ParkingSpot


class FourWheelerParkingSpotManager(ParkingSpotManager):
    parking_spot_list = list()

    def __init__(self, parking_strategy):
        super().__init__(parking_strategy)

    def find_parking_space(self):
        print(f"Finding parking Space for your two wheeler")
        return self.parking_strategy.find_parking_space(FourWheelerParkingSpotManager)

    @staticmethod
    def add_parking_space(parking_spot_obj):
        FourWheelerParkingSpotManager.parking_spot_list.append(parking_spot_obj)

    @staticmethod
    def remove_parking_space(parking_spot_obj):
        if parking_spot_obj in FourWheelerParkingSpotManager.parking_spot_list:
            FourWheelerParkingSpotManager.parking_spot_list.remove(parking_spot_obj)
