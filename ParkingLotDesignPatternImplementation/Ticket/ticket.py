from ParkingLotDesignPatternImplementation.Vehicle.vehicle import Vehicle
from ParkingLotDesignPatternImplementation.ParkingSpot.parking_spot import ParkingSpot


class Ticket:
    _id = 0
    _ticket_stack = []

    def __init__(self, entry_time, vehicle_obj: Vehicle, parking_spot_obj: ParkingSpot):
        Ticket._id += 1
        self.id = Ticket._id
        self.entry_time = entry_time
        self.vehicle_obj = vehicle_obj
        self.parking_spot = parking_spot_obj

    def generate_ticket(self):
        print(f"Generating Ticket......")
        Ticket._ticket_stack.append(self)

    @staticmethod
    def get_tickets_list():
        return Ticket._ticket_stack

    @staticmethod
    def remove_ticket(ticket_obj):
        Ticket._ticket_stack.remove(ticket_obj)
