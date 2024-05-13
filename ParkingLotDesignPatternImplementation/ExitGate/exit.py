from ParkingLotDesignPatternImplementation.Ticket.ticket import Ticket
from ParkingLotDesignPatternImplementation.CostComputationFactory.cost_computation_factory import CostComputationFactory
from ParkingLotDesignPatternImplementation.PaymentFactory.payment_factory import PaymentFactory


class Exit:

    def __init__(self, vehicle_id, payment_method: str):
        self.ticket_obj = None
        self.vehicle_id = vehicle_id
        self.payment_method = self._get_payment_method_obj(payment_method)
        self.price = None

    def _get_payment_method_obj(self, payment_method):
        payment_method_obj = PaymentFactory.get_payment_method_obj(payment_method)
        return payment_method_obj

    def _cost_calculation(self):
        cost_computation_obj = CostComputationFactory.get_cost_computation_obj(self.ticket_obj.vehicle_obj)
        self.price = cost_computation_obj.price()
        print(f"Price: {self.price}")

    def _make_payment(self):
        self.payment_method.record_payment(self.price)

    def _remove_vehicle(self):
        self.ticket_obj.parking_spot.remove_vehicle(self.ticket_obj.vehicle_obj)

    def _vehicle_present(self):
        ticket_stack = Ticket.get_tickets_list()
        print(f"Vehicle Present in parking: {len(ticket_stack)}")
        for ticket_obj in ticket_stack:
            if ticket_obj.vehicle_obj.vehicle_no == self.vehicle_id:
                Ticket.remove_ticket(ticket_obj)
                self.ticket_obj = ticket_obj
                return True
            else:
                return False

    def exit(self):
        if self._vehicle_present() is False:
            print("Vehicle Not present in parking")
            return
        self._cost_calculation()
        self._make_payment()
        self._remove_vehicle()
        print("Exit, Please come again.")
