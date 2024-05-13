from StretagyDesignPattern.Stretegy.strategy import Strategy
from typing import List


class SortedStrategy(Strategy):
    def do_algorithm(self, data: List) -> List:
        return sorted(data)


class SortedReverseStrategy(Strategy):
    def do_algorithm(self, data: List) -> List:
        data = sorted(data)
        data.reverse()
        return data


class SimpleReturnStrategy(Strategy):
    def do_algorithm(self, data: List):
        return data
