class Product:
    def __init__(self, name, stock):
        self.name = name
        self.__stock = stock

    def sell(self, quantity):
        if quantity <= 0 or quantity > self.__stock:
            return False
        self.__stock -= quantity
        return True

    def restock(self, quantity):
        if quantity > 0:
            self.__stock += quantity

    def available(self):
        return self.__stock

product = Product("Notebook", 20)
print("Sold:", product.sell(3))
product.restock(5)
print(product.name, product.available())
