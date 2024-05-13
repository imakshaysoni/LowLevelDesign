from abc import abstractmethod, ABC
from ParkingLotDesignPatternImplementation.Vehicle.vehicle import Vehicle


class ParkingSpot(ABC):
    _id = 0

    def __init__(self):
        self.vehicle_obj = None
        ParkingSpot._id += 1
        self.id = ParkingSpot._id
        self.isEmpty = True
        self.price = 0

    @abstractmethod
    def park_vehicle(self, vehicle: Vehicle):
        pass

    @abstractmethod
    def remove_vehicle(self, vehicle: Vehicle):
        pass
