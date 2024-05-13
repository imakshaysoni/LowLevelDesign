from ParkingLotDesignPatternImplementation.Vehicle.vehicle import Vehicle
from ParkingLotDesignPatternImplementation.ParkingSpotManagerFactory.parking_spot_manager_factory import ParkingSpotManagerFactory
from ParkingLotDesignPatternImplementation.Ticket.ticket import Ticket
from datetime import  datetime


class Entrance:
    def __init__(self, vehicle_obj: Vehicle):
        self.entry_time = datetime.now()
        self.vehicle_obj = vehicle_obj
        self.parking_spot_manager_factory_obj = ParkingSpotManagerFactory()

    def _get_parking_manager(self):
        parking_spot_manager_obj = self.parking_spot_manager_factory_obj.get_parking_spot_manager(self.vehicle_obj)
        return parking_spot_manager_obj

    def _generate_ticket(self, parking_spot_obj):
        ticket_obj = Ticket(self.entry_time, self.vehicle_obj, parking_spot_obj)
        ticket_obj.generate_ticket()
        return ticket_obj

    def park_vehicle(self):
        parking_spot_manager_obj = self._get_parking_manager()
        parking_spot_obj = parking_spot_manager_obj.find_parking_space()
        if parking_spot_obj is None:
            return "No Parking Space Available, Please come later."
        parking_spot_obj.park_vehicle(self.vehicle_obj)

        ticket_obj = self._generate_ticket(parking_spot_obj)
        return ticket_obj
