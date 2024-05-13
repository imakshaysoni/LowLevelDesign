from ParkingLotDesignPatternImplementation.PaymentStretegy.payment_strategy import Payment


class CashPayment(Payment):

    def record_payment(self, price):
        print(f"{price} Cash Payment Received")
