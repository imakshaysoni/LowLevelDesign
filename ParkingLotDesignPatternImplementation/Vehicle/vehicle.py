from ParkingLotDesignPatternImplementation.Vehicle.enums import VehicleTypes


class Vehicle:
    def __init__(self, vehicle_no, vehicle_type):
        self.vehicle_no = vehicle_no
        if vehicle_type == "two_wheeler":
            self.vehicle_type = VehicleTypes.two_wheeler.value
        elif vehicle_type == "four_wheeler":
            self.vehicle_type = VehicleTypes.four_wheeler.value
