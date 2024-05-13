from StretagyDesignPattern.Stretegy.strategy import Strategy


class Vehicle:
    def __init__(self,  strategy_obj: Strategy):
        self._strategy = strategy_obj

    def perform_operation(self, data):

        print(f"Calling Strategy Obj of: {self._strategy}")
        result = self._strategy.do_algorithm(data)
        print(f"Result: {result}")

