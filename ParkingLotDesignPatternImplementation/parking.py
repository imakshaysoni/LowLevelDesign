from EntryGate.entrance import Entrance
from ExitGate.exit import Exit
from ParkingLotDesignPatternImplementation.ParkingSpot.four_wheeler_parking_spot import FourWheelerParkingSpot
from ParkingLotDesignPatternImplementation.ParkingSpot.two_wheelar_parking_spot import TwoWheelerParkingSpot
from ParkingLotDesignPatternImplementation.ParkingSpotManager.four_wheeler_parking_space_manager import \
    FourWheelerParkingSpotManager
from ParkingLotDesignPatternImplementation.Ticket.ticket import Ticket
from ParkingLotDesignPatternImplementation.ParkingSpotManager.two_wheeler_parking_spot_manager import \
    TwoWheelerParkingSpotManager
from ParkingLotDesignPatternImplementation.Vehicle.enums import payment_mapper, vehicle_type_mapper
from Vehicle.vehicle import Vehicle

if __name__ == "__main__":
    print("This application is designed by Akshay Soni, "
          "In this mall, we have only 1 parking for 'Four Wheeler' and 2 parking slot for 'Two Wheeler.")
    # Initial Configuration
    # run_initial_configuration()
    for i in range(2):
        parking_spot = TwoWheelerParkingSpot()
        TwoWheelerParkingSpotManager.add_parking_space(parking_spot)

    # Create 5 Parking Spots for Two Wheeler
    for i in range(1):
        parking_spot = FourWheelerParkingSpot()
        FourWheelerParkingSpotManager.add_parking_space(parking_spot)

    while True:
        print("Welcome to Akshay Super Mall.")
        action = int(input("Please select Below Option: \n"
                           "1. Entry\n"
                           "2. Exit\n"
                           "3. Leave Application\n"))
        if action == 1:
            type = int(input("Please provide vehicle type\n"
                             "1. Two_wheeler\n"
                             "2. Four_wheeler \n"))
            vehicle_no = int(input("Please provide your vehicle number"))
            vehicle_obj = Vehicle(vehicle_no, vehicle_type_mapper[type])
            entrance_obj = Entrance(vehicle_obj)
            ticket_obj = entrance_obj.park_vehicle()
            if not isinstance(ticket_obj, Ticket):
                print(ticket_obj)
                continue

            print(f"\nPlease find you ticket details:\n"
                  f"VehicleNo: {ticket_obj.vehicle_obj.vehicle_no}\n"
                  f"Entry Time: {ticket_obj.entry_time}\n"
                  f"ParkingSpot: {ticket_obj.parking_spot.id}\n"
                  f"Ticket Number: {ticket_obj.id}\n")

        elif action == 2:
            vehicle_id = int(input("Enter Vehicle Number\n"))
            print("It's time to leave mall.")
            payment_method = int(input("Please provide the payment method\n"
                                       "1. Cash\n"
                                       "2. Card\n"
                                       "3. UPI\n "))
            exit_obj = Exit(vehicle_id, payment_mapper[payment_method])
            exit_obj.exit()
        else:
            print("Thanks for using application")
            break
