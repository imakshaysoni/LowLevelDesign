from ParkingLotDesignPatternImplementation.ParkingStretegy.parking_stretegy import ParkingStrategy


class NearToEntranceAndElevatorParkingStrategy(ParkingStrategy):

    def find_parking_space(self, cls):
        print(f"Near To Entrance And Elevator Parking Strategy Applied:")
        for spot_obj in cls.parking_spot_list:
            if spot_obj.isEmpty:
                return spot_obj
        return None
