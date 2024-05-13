from ParkingSpot.four_wheeler_parking_spot import FourWheelerParkingSpot
from ParkingSpot.two_wheelar_parking_spot import TwoWheelerParkingSpot
from ParkingSpotManager.two_wheeler_parking_spot_manager import TwoWheelerParkingSpotManager
from ParkingSpotManager.four_wheeler_parking_space_manager import FourWheelerParkingSpotManager


def run_initial_configuration():
    print("Initial Configuration Running")

    # Create 10 Parking Spots for Two Wheeler
    for i in range(2):
        parking_spot = TwoWheelerParkingSpot()
        TwoWheelerParkingSpotManager.add_parking_space(parking_spot)

    # Create 5 Parking Spots for Two Wheeler
    for i in range(2):
        parking_spot = FourWheelerParkingSpot()
        FourWheelerParkingSpotManager.add_parking_space(parking_spot)