from abc import ABC, abstractmethod
from enum import Enum
class Istrategy(ABC):
    @abstractmethod
    def calculate(self,a, b):
        pass
    
class add(Istrategy):
    def calculate(self,a, b):
        return a + b
    
class minus(Istrategy):
    def calculate(self,a, b):
        return a - b
    
class multiple(Istrategy):
    def calculate(self,a, b):
        return a * b
class DoType(Enum):
    ADD = 'add'
    MINUS = 'minus'
    DIVIDE = 'divide'
    MULTIPLY = 'multiply'
class divide(Istrategy):
    def calculate(self,a, b):
        return a / b
    
    
class Calculator(ABC):
    def __init__(self, strategy):
        self.now = 0
        self.strategy = strategy
        
    def execute(self,a,b):
        return self.strategy.calculate(a, b)
    
    def reset(self):
        self.now = 0
        
    def set_strategy(self, do_type: DoType):
        strategy_map = {
            DoType.ADD: add(),
            DoType.MINUS: minus(),
            DoType.DIVIDE: divide(),
            DoType.MULTIPLY: multiple()
        }
        self.strategy = strategy_map[do_type]

# Example usage
calculator = Calculator(add())
print(calculator.execute(3, 2))  # Output: 5

calculator.set_strategy(DoType.MINUS)
print(calculator.execute(3, 2))  # Output: 1

calculator.set_strategy(DoType.MULTIPLY)
print(calculator.execute(3, 2))  # Output: 6

calculator.set_strategy(DoType.DIVIDE)
print(calculator.execute(6, 2))  # Output: 3


