from abc import ABC, abstractmethod
'''
產品
'''
class Product(ABC):
    @abstractmethod
    def describe(self):
        pass
'''
生產產品的工廠
'''
class Factory(ABC):
    @abstractmethod
    def getProduct(self, Product):
        pass
class FrenchFries(Product):
    def __init__(self, state="有鹽巴"):
        self.state = state
        
    def describe(self):
        print(f"我是{self.state}的薯條")
        

class FrenchFriesFactory(Factory):
    def getProduct(self):
        return FrenchFries()
    
    def getProductWithState(self, state):
        return FrenchFries(state)
    

def main():
    friesFac = FrenchFriesFactory()
    fries = friesFac.getProduct()
    fries.describe()
    myfries = friesFac.getProductWithState("無鹽巴的")
    myfries.describe()

if __name__ == "__main__":
    main()