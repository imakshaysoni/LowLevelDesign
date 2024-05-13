from Vehicle.vehicle import Vehicle
from Stretegy.strategyExtendedClasses import SortedReverseStrategy, SortedStrategy, SimpleReturnStrategy

if __name__=="__main__":
    data = [1, 0, 6, 2, 5, 4, 9, 10, 32, 9, 12]
    vehicle_obj = Vehicle(SortedStrategy())
    vehicle_obj.perform_operation(data)

    print("Another Strategy")
    vehicle_obj2 = Vehicle(SortedReverseStrategy())
    vehicle_obj2.perform_operation(data)

    print("Adding Another Strategy")
    vehicle_obj3 = Vehicle(SimpleReturnStrategy())
    vehicle_obj3.perform_operation(data)
