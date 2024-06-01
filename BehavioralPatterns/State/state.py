# ÖRNEK 1
from abc import ABC, abstractmethod

# State arayüzü
class State(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

# ConcreteState sınıfları
class PositiveBalanceState(State):
    def __init__(self, account):
        self.account = account

    def deposit(self, amount):
        self.account.balance += amount
        print(f"Deposited {amount}. Balance is now {self.account.balance}.")

    def withdraw(self, amount):
        if self.account.balance >= amount:
            self.account.balance -= amount
            print(f"Withdrew {amount}. Balance is now {self.account.balance}.")
            if self.account.balance < 0:
                self.account.state = self.account.overdrawn_state
        else:
            print("Insufficient funds. Withdrawal denied.")

class OverdrawnState(State):
    def __init__(self, account):
        self.account = account

    def deposit(self, amount):
        self.account.balance += amount
        print(f"Deposited {amount}. Balance is now {self.account.balance}.")
        if self.account.balance >= 0:
            self.account.state = self.account.positive_balance_state

    def withdraw(self, amount):
        print("Account overdrawn. Withdrawal denied.")

class FrozenState(State):
    def __init__(self, account):
        self.account = account

    def deposit(self, amount):
        print("Account frozen. Deposit denied.")

    def withdraw(self, amount):
        print("Account frozen. Withdrawal denied.")

# Context sınıfı
class Account:
    def __init__(self):
        self.positive_balance_state = PositiveBalanceState(self)
        self.overdrawn_state = OverdrawnState(self)
        self.frozen_state = FrozenState(self)

        self.state = self.positive_balance_state
        self.balance = 0

    def deposit(self, amount):
        self.state.deposit(amount)

    def withdraw(self, amount):
        self.state.withdraw(amount)

    def freeze_account(self):
        self.state = self.frozen_state
        print("Account has been frozen.")

    def unfreeze_account(self):
        if self.balance >= 0:
            self.state = self.positive_balance_state
        else:
            self.state = self.overdrawn_state
        print("Account has been unfrozen.")

# Kullanım
account = Account()
account.deposit(100)
account.withdraw(50)
account.withdraw(60)
account.deposit(20)
account.freeze_account()
account.deposit(30)
account.unfreeze_account()
account.withdraw(10)

print("#"*70)

# ÖRNEK 2
from abc import ABC, abstractmethod

# State arayüzü
class CoffeeMachineState(ABC):
    @abstractmethod
    def insert_coin(self, machine):
        pass

    @abstractmethod
    def select_coffee(self, machine):
        pass

    @abstractmethod
    def brew_coffee(self, machine):
        pass

# ConcreteState sınıfları
class NoCoinState(CoffeeMachineState):
    def insert_coin(self, machine):
        print("Coin inserted.")
        machine.state = machine.has_coin_state

    def select_coffee(self, machine):
        print("Please insert coin first.")

    def brew_coffee(self, machine):
        print("Please insert coin first.")

class HasCoinState(CoffeeMachineState):
    def insert_coin(self, machine):
        print("Coin already inserted.")

    def select_coffee(self, machine):
        print("Coffee selected.")
        machine.state = machine.brew_in_progress_state

    def brew_coffee(self, machine):
        print("Please select coffee first.")

class BrewInProgressState(CoffeeMachineState):
    def insert_coin(self, machine):
        print("Cannot insert coin while brewing.")

    def select_coffee(self, machine):
        print("Already brewing coffee.")

    def brew_coffee(self, machine):
        print("Brewing coffee...")
        machine.state = machine.no_coin_state  # Process is finished, back to NoCoinState

# Context sınıfı
class CoffeeMachine:
    def __init__(self):
        self.no_coin_state = NoCoinState()
        self.has_coin_state = HasCoinState()
        self.brew_in_progress_state = BrewInProgressState()

        self.state = self.no_coin_state

    def insert_coin(self):
        self.state.insert_coin(self)

    def select_coffee(self):
        self.state.select_coffee(self)

    def brew_coffee(self):
        self.state.brew_coffee(self)

# Kullanım
coffee_machine = CoffeeMachine()
coffee_machine.select_coffee()  # Output: Please insert coin first.
coffee_machine.brew_coffee()    # Output: Please insert coin first.

coffee_machine.insert_coin()    # Output: Coin inserted.
coffee_machine.select_coffee()  # Output: Coffee selected.

coffee_machine.insert_coin()    # Output: Cannot insert coin while brewing.
coffee_machine.select_coffee()  # Output: Already brewing coffee.
coffee_machine.brew_coffee()    # Output: Brewing coffee...

coffee_machine.insert_coin()    # Output: Coin inserted.
