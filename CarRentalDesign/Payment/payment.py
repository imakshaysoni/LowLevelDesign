from LowLevelDesign.CarRentalDesign.Bill.bill import Bill


class Payment:

    def __init__(self):
        pass

    def process_payment(self, bill: Bill):
        bill.is_paid = True
        print("Payment Completed.")