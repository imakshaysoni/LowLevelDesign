from FactoryDesignPattern.Factory.factory import Factory

user_input = input("Enter Vehicle Type: ")
vehicle_obj = Factory.get_vehicle(user_input)
vehicle_obj.run_vehicle()

