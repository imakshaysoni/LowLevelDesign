from ParkingLotDesignPatternImplementation.ParkingSpot.parking_spot import ParkingSpot
from ParkingLotDesignPatternImplementation.Vehicle.vehicle import Vehicle


class FourWheelerParkingSpot(ParkingSpot):

    def park_vehicle(self, vehicle_obj: Vehicle):
        self.vehicle_obj = vehicle_obj
        self.isEmpty = False
        print(f"Vehicle {self.vehicle_obj.vehicle_no} is parked at {self.id}")

    def remove_vehicle(self, vehicle_obj):
        print(f"Vehicle {vehicle_obj.vehicle_no} is removed from parking spot {self.id}")
        self.vehicle_obj = None
        self.isEmpty = True

