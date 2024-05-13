from FactoryDesignPattern.VechicleTypes.car import Car
from FactoryDesignPattern.VechicleTypes.bike import Bike
from FactoryDesignPattern.VechicleTypes.bus import Bus


class Factory:

    @staticmethod
    def get_vehicle(type):
        if type == "car":
            return Car()
        elif type == "bike":
            return Bike()
        elif type == "bus":
            return Bus()
        else:
            raise ValueError(f"Invalid animal type: {type}")







