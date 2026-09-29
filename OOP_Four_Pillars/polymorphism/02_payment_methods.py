class CardPayment:
    def __init__(self, last_four):
        self.last_four = last_four

    def pay(self, amount):
        return f"Card {self.last_four} paid Rs {amount}"

class CashPayment:
    def __init__(self, cashier):
        self.cashier = cashier

    def pay(self, amount):
        return f"Cashier {self.cashier} received Rs {amount}"

def checkout(method, amount):
    print(method.pay(amount))

checkout(CardPayment("1234"), 1500)
checkout(CashPayment("Ali"), 800)
