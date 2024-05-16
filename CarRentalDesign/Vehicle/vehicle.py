from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def __init__(self):
        self.cost = None


class Bike(Vehicle):
    def __init__(self, name, number, model):
        self.name = name
        self.model = model
        self.number = number
        self.status = "ACTIVE"
        self.type = "Bike"
        self.cost = 1000


class Car(Vehicle):
    def __init__(self, name, number, model):
        self.name = name
        self.model = model
        self.number = number
        self.status = "ACTIVE"
        self.type = "Car"
        self.cost = 2000
