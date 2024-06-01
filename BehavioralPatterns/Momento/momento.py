# ÖRNEK 1
# Originator Sınıfı
class Editor:
    def __init__(self):
        self._content = ""

    def type(self, words):
        self._content += words

    def get_content(self):
        return self._content

    def save(self):
        return Memento(self._content)

    def restore(self, memento):
        self._content = memento.get_content()

# Momento Sınıfı
class Memento:
    def __init__(self, content):
        self._content = content

    def get_content(self):
        return self._content

# Caretaker Sınıfı
class EditorHistory:
    def __init__(self):
        self._history = []

    def save(self, memento):
        self._history.append(memento)

    def undo(self):
        if not self._history:
            return None
        return self._history.pop()

# Kullanım
if __name__ == "__main__":
    editor = Editor()
    history = EditorHistory()

    editor.type("This is the first sentence.")
    history.save(editor.save())

    editor.type(" This is the second sentence.")
    history.save(editor.save())

    editor.type(" And this is the third sentence.")
    print(f"Current Content: {editor.get_content()}")

    editor.restore(history.undo())
    print(f"After undo: {editor.get_content()}")

    editor.restore(history.undo())
    print(f"After second undo: {editor.get_content()}")

print("#"*70)

# ÖRNEK 2
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        print(f"{self.owner} deposits ${amount}")
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            print(f"{self.owner} withdraws ${amount}")
            self.balance -= amount
        else:
            print(f"{self.owner} cannot withdraw ${amount}. Insufficient funds.")

    def get_balance(self):
        return self.balance

    def save(self):
        return BankAccountMemento(self.owner, self.balance)

    def restore(self, memento):
        self.owner = memento.owner
        self.balance = memento.balance

class BankAccountMemento:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

class BankAccountHistory:
    def __init__(self):
        self.history = []

    def save(self, memento):
        self.history.append(memento)

    def undo(self):
        if self.history:
            return self.history.pop()
        else:
            return None
        
if __name__ == "__main__":
    account = BankAccount("John Doe", 1000)
    history = BankAccountHistory()

    print(f"Initial Balance: ${account.get_balance()}")

    account.deposit(500)
    history.save(account.save())
    print(f"After deposit: ${account.get_balance()}")

    account.withdraw(200)
    history.save(account.save())
    print(f"After withdrawal: ${account.get_balance()}")

    account.withdraw(1500)
    print(f"After attempted withdrawal: ${account.get_balance()}")

    memento = history.undo()
    if memento:
        account.restore(memento)
        print(f"After undo: ${account.get_balance()}")
