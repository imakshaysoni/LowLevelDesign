# Entry Point for Car Rental System Designfrom LowLevelDesign.CarRentalDesign.VehicleRentalSystem.rental_system import (    VehicleRentalSystem,)from LowLevelDesign.CarRentalDesign.Bill.bill import Billfrom LowLevelDesign.CarRentalDesign.Payment.payment import Paymentvrs = VehicleRentalSystem()  # Vehicle Rent System# store details# storeLocation = Pune, Delhipune_store = vrs.create_store("pune")delhi_store = vrs.create_store("delhi")# insert vehicle to storespune_store.add_vehicle("Yamaha FZA", "MH12SN5295", "FZS", "Bike")pune_store.add_vehicle("Swift", "MH09CH9449", "Desire", "Car")delhi_store.add_vehicle("BMW", "MP09CH4608", "GSR", "Bike")# Create User: First Visituser1 = vrs.create_user("Akshay", "FZIPS2001H")store = vrs.get_store("delhi")print(store.location)reservation = store.create_reservation(user1, vehicle_type="Bike")if not reservation:    print("No Vehicle Available")else:    bill = Bill(reservation)    bill.generate_bill()    # Make Payment    payment = Payment()    payment.process_payment(bill)