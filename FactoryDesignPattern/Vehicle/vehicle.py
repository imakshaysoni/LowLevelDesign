from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def run_vehicle(self):
        pass
