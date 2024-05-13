from enum import Enum


class VehicleTypes(Enum):
    two_wheeler = "TwoWheeler"
    four_wheeler = "FourWheeler"


payment_mapper = {1: "cash", 2: "card", 3: "upi"}
vehicle_type_mapper = {1: "two_wheeler", 2: "four_wheeler"}
