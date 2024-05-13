from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def record_payment(self, price):
        pass
