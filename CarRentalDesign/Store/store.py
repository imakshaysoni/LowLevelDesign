from LowLevelDesign.CarRentalDesign.Vehicle.vehicle_inventory_management import (
    VehicleInventoryManager,
)
from LowLevelDesign.CarRentalDesign.User.user import User
from LowLevelDesign.CarRentalDesign.Reservation.reservation import Reservation


class Store:
    def __init__(self, location):
        self.vehicle_inventory = VehicleInventoryManager()
        self.location = location
        self.reservation_list = []

    def create_reservation(self, user: User, vehicle_type):
        veh = self.vehicle_inventory.get_vehicle(vehicle_type)
        if veh is None:
            return None
        reservation = Reservation(veh, user)
        self.reservation_list.append(reservation)
        return reservation

    def add_vehicle(self, name, number, model, type):
        return self.vehicle_inventory.add_vehicle(name, number, model, type)
