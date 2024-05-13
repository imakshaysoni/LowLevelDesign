from ParkingLotDesignPatternImplementation.PricingStrategy.pricing_strategy import PricingStrategy


class MinutePricingStrategy(PricingStrategy):

    def price(self):
        print("Minute Pricing Strategy Applied")
        return 10
