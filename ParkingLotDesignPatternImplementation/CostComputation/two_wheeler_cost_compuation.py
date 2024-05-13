from ParkingLotDesignPatternImplementation.CostComputation.cost_computation import CostComputation


class TwoWheelerCostComputation(CostComputation):

    def __init__(self, pricing_strategy):
        self.pricing_strategy = pricing_strategy

    def price(self):
        return self.pricing_strategy.price()
