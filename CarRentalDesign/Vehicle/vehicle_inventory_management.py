from LowLevelDesign.CarRentalDesign.Vehicle.vehicle import Bike, Car, Vehicle


class VehicleInventoryManager:
    def __init__(self):
        self.vehicle_list = []

    def add_vehicle(self, name, number, model, type):
        if type == "Car":
            vehicle_obj = Car(name, number, model)
        elif type == "Bike":
            vehicle_obj = Bike(name, number, model)
        self.vehicle_list.append(vehicle_obj)

    def remove_vehicle(self, v: Vehicle):
        self.vehicle_list.remove(v)

    def get_vehicle(self, vehicle_type):
        for vehicle in self.vehicle_list:
            if vehicle.type == vehicle_type:
                self.vehicle_list.remove(vehicle)
                return vehicle
        return None
