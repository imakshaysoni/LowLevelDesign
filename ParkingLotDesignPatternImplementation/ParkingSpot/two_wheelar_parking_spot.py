from ParkingLotDesignPatternImplementation.ParkingSpot.parking_spot import ParkingSpot
from ParkingLotDesignPatternImplementation.Vehicle.vehicle import Vehicle


class TwoWheelerParkingSpot(ParkingSpot):

    def park_vehicle(self, vehicle_obj):
        self.vehicle_obj = vehicle_obj
        self.isEmpty = False

    def remove_vehicle(self, vehicle_obj: Vehicle):
        print(f"Vehicle {vehicle_obj.vehicle_no} is removed from parking spot {self.id}")
        self.vehicle_obj = None
        self.isEmpty = True
