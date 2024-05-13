from abc import  ABC, abstractmethod


class CostComputation(ABC):

    @abstractmethod
    def price(self):
        pass
