class CoffeeMachine:
    NO_COIN = 0
    HAS_COIN = 1
    BREW_IN_PROGRESS = 2

    def __init__(self):
        self.state = self.NO_COIN

    def insert_coin(self):
        if self.state == self.NO_COIN:
            print("Coin inserted.")
            self.state = self.HAS_COIN
        elif self.state == self.HAS_COIN:
            print("Coin already inserted.")
        elif self.state == self.BREW_IN_PROGRESS:
            print("Cannot insert coin while brewing.")

    def select_coffee(self):
        if self.state == self.NO_COIN:
            print("Please insert coin first.")
        elif self.state == self.HAS_COIN:
            print("Coffee selected.")
            self.state = self.BREW_IN_PROGRESS
        elif self.state == self.BREW_IN_PROGRESS:
            print("Already brewing coffee.")

    def brew_coffee(self):
        if self.state == self.NO_COIN:
            print("Please insert coin first.")
        elif self.state == self.HAS_COIN:
            print("Please select coffee first.")
        elif self.state == self.BREW_IN_PROGRESS:
            print("Brewing coffee...")
            self.state = self.NO_COIN

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
