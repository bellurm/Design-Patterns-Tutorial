class Pizza:
    def __init__(self):
        self.ingredients = []

    def add_cheese(self):
        self.ingredients.append("cheese")
        return self

    def add_tomato(self):
        self.ingredients.append("tomato")
        return self

    def add_pepperoni(self):
        self.ingredients.append("pepperoni")
        return self

    def add_olives(self):
        self.ingredients.append("olives")
        return self

    def __str__(self):
        return f"Pizza with {' '.join(self.ingredients)}"

# Method chaining kullanarak pizza oluşturma
pizza = Pizza().add_cheese().add_tomato().add_pepperoni().add_olives()
print(pizza)