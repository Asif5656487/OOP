class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def show_balance(self):
        return self.__balance

account = BankAccount("Abdullah", 1000)
account.deposit(500)
account.withdraw(200)
print(account.owner, account.show_balance())
