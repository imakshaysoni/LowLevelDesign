from ParkingLotDesignPatternImplementation.PaymentStretegy.payment_strategy import Payment


class CardPayment(Payment):

    def record_payment(self, price):
        print(f"{price} Card Payment Received")
