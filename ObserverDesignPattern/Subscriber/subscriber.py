from abc import ABC, abstractmethod


class Subscriber(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self, message: str) -> None:
        """
        Receive update from subject.
        """
        pass


class EmailSubscriber(Subscriber):

    def update(self, message: str):
        print(f"EmailAlert: {message}")


class MobileSubscriber(Subscriber):

    def update(self, message: str) -> None:
        print(f"MobileAlert: {message}")
