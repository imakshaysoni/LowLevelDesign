from ParkingLotDesignPatternImplementation.PaymentStretegy.upi_payment_strategy import UpiPayment
from ParkingLotDesignPatternImplementation.PaymentStretegy.card_payment_strategy import CardPayment
from ParkingLotDesignPatternImplementation.PaymentStretegy.cash_payment_strategy import CashPayment


class PaymentFactory:

    @staticmethod
    def get_payment_method_obj(payment_method):
        if payment_method == "upi":
            return UpiPayment()
        elif payment_method == "card":
            return CardPayment()
        elif payment_method == "cash":
            return CashPayment()