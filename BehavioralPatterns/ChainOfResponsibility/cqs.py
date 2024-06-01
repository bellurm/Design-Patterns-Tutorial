class Account:
    def __init__(self, initial_balance=0):
        self._balance = initial_balance

    # Command: Balance'ı günceller
    def deposit(self, amount):
        self._balance += amount

    # Command: Balance'ı günceller
    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            raise ValueError("Insufficient funds")

    # Query: Balance'ı döner
    def get_balance(self):
        return self._balance

# Kullanım
account = Account(100)
account.deposit(50)
account.withdraw(30)
print(account.get_balance())  # Output: 120