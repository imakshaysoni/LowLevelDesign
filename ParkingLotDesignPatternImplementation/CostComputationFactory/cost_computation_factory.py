from ParkingLotDesignPatternImplementation.CostComputation.two_wheeler_cost_compuation import TwoWheelerCostComputation
from ParkingLotDesignPatternImplementation.CostComputation.four_wheeler_cost_computation import FourWheelerCostComputation
from ParkingLotDesignPatternImplementation.PricingStrategy.hourly_pricing_strategy import HourlyPricingStrategy
from ParkingLotDesignPatternImplementation.PricingStrategy.minute_pricing_strategy import MinutePricingStrategy


class CostComputationFactory:

    @staticmethod
    def get_cost_computation_obj(vehicle_obj):
        if vehicle_obj.vehicle_type == "TwoWheeler":
            return TwoWheelerCostComputation(MinutePricingStrategy())
        elif vehicle_obj.vehicle_type == "FourWheeler":
            return FourWheelerCostComputation(HourlyPricingStrategy())
