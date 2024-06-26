from StrategyPattern import Istrategy
import math
class BusStrategy(Istrategy):
    def calculate(self, km):
        count = 0
        if(km <= 10):
            count = 1
        elif(km > 10):
            count = 2
        
        return count * 15

class MRTStrategy(Istrategy):
    def calculate(self, km):
        result = 0
        if(km <= 0):
            return result
        if(km <= 10):
            result = 20
        
        if(km > 10):
            count = math.ceil((km - 10)/5)
            return 20 + 5 * count

class PriceCalculator:
    def __init__(self, strategy=None):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def calculate(self, km, strategy=None):
        if strategy is not None:
            self.strategy = strategy
        if self.strategy is None:
            raise ValueError("Strategy must be set before calculation.")
        return self.strategy.calculate(km)