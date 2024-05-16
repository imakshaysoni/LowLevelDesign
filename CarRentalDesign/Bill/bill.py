from LowLevelDesign.CarRentalDesign.Reservation.reservation import Reservation


class Bill:
    def __init__(self, reservation: Reservation):
        self.reservation = reservation
        self.is_paid = False

    def generate_bill(self):
        print(f"Generating Bill, Cost: {self.reservation.vehicle.cost}")
