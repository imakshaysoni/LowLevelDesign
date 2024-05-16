from LowLevelDesign.CarRentalDesign.Vehicle.vehicle import Vehicle
from LowLevelDesign.CarRentalDesign.User.user import User


class Reservation:
    _id = 1

    def __init__(self, veh: Vehicle, user: User):
        self.id = Reservation._id
        self.status = "SCHEDULED"
        self.fromDate = "12th"
        self.toDate = "14th"
        self.fromTimeStamp = "4:00 AM"
        self.toTimeStamp = "12:00"
        self.vehicle = veh
        self.user = user
        Reservation._id += 1
