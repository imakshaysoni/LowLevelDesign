from ParkingLotDesignPatternImplementation.PricingStrategy.pricing_strategy import PricingStrategy


class HourlyPricingStrategy(PricingStrategy):

    def price(self):
        print("Hourly Pricing Strategy Applied")
        return 50
