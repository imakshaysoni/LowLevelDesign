from abc import ABC, abstractmethod
from ObserverDesignPattern.Subscriber.subscriber import Subscriber


class Publisher(ABC):

    @abstractmethod
    def subscribe(self, obj: Subscriber):
        pass

    @abstractmethod
    def unsubscribe(self, obj: Subscriber):
        pass

    @abstractmethod
    def notify(self):
        pass


class IphonePublisher(Publisher):

    subscriber_list = list()
    _stock_count = 0

    def subscribe(self, obj: Subscriber):
        self.subscriber_list.append(obj)
        print(f"{obj} is subscriber to IphoneSubscriber")

    def unsubscribe(self, obj: Subscriber):
        self.subscriber_list.remove(obj)
        print(f"{obj} is unsubscribed to IphoneSubscriber")

    def notify(self):
        for obj in self.subscriber_list:
            obj.update("Iphone Stock Updated")

    def update_stock(self, new_stock: int):
        if self._stock_count == 0:
            self.notify()
        self._stock_count = new_stock


class FridgePublisher(Publisher):
    subscriber_list = list()
    _stock_count = 0

    def subscribe(self, obj: Subscriber):
        self.subscriber_list.append(obj)
        print(f"{obj} is subscriber to FridgeSubscriber")

    def unsubscribe(self, obj: Subscriber):
        self.subscriber_list.remove(obj)
        print(f"{obj} is unsubscribed to FridgeSubscriber")

    def notify(self):
        for obj in self.subscriber_list:
            obj.update("Fridge Stock Updated")

    def update_stock(self, new_stock: int):
        if self._stock_count == 0:
            self.notify()
        self._stock_count = new_stock
