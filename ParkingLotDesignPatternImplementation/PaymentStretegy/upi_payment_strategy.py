from ParkingLotDesignPatternImplementation.PaymentStretegy.payment_strategy import Payment


class UpiPayment(Payment):

    def record_payment(self, price):
        print(f"{price} UPI Payment Received")
