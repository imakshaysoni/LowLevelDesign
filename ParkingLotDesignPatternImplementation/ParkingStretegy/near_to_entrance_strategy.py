from ParkingLotDesignPatternImplementation.ParkingStretegy.parking_stretegy import ParkingStrategy


class NearToEntranceParkingStrategy(ParkingStrategy):

    def find_parking_space(self, cls):
        print("Near To Entrance Parking Strategy Applied")
        for spot_obj in cls.parking_spot_list:
            if spot_obj.isEmpty:
                return spot_obj
        return None
