from abc import ABC, abstractmethod


class PricingStrategy(ABC):

    @abstractmethod
    def price(self):
        pass
