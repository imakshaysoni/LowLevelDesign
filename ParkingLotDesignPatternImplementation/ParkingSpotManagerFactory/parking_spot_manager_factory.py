from ParkingLotDesignPatternImplementation.ParkingStretegy.near_to_entrance_and_elevator import \
    NearToEntranceAndElevatorParkingStrategy
from ParkingLotDesignPatternImplementation.ParkingStretegy.near_to_entrance_strategy import \
    NearToEntranceParkingStrategy
from ParkingLotDesignPatternImplementation.Vehicle.vehicle import Vehicle
from ParkingLotDesignPatternImplementation.ParkingSpotManager.two_wheeler_parking_spot_manager import TwoWheelerParkingSpotManager
from ParkingLotDesignPatternImplementation.ParkingSpotManager.four_wheeler_parking_space_manager import FourWheelerParkingSpotManager


class ParkingSpotManagerFactory:

    def __init__(self):
        pass

    @staticmethod
    def get_parking_spot_manager(vehicle_obj: Vehicle):
        if vehicle_obj.vehicle_type == "TwoWheeler":
            return TwoWheelerParkingSpotManager(NearToEntranceParkingStrategy())
        elif vehicle_obj.vehicle_type == "FourWheeler":
            return FourWheelerParkingSpotManager(NearToEntranceAndElevatorParkingStrategy())
        else:
            return "Invalid Vehicle Type"
