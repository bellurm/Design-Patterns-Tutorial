# ÖRNEK 1
from abc import ABC, abstractmethod

class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass

class ConcreteProductA(Product):
    def operation(self) -> str:
        return "Result of ConcreteProductA"

class ConcreteProductB(Product):
    def operation(self) -> str:
        return "Result of ConcreteProductB"

class Creator(ABC):
    @abstractmethod
    def factory_method(self) -> Product:
        pass

    def some_operation(self) -> str:
        product = self.factory_method()
        result = f"Creator: The same creator's code has just worked with {product.operation()}"
        return result

class ConcreteCreatorA(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductA()

class ConcreteCreatorB(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductB()

def client_code(creator: Creator) -> None:
    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.some_operation()}")

if __name__ == "__main__":
    print("App: Launched with ConcreteCreatorA.")
    client_code(ConcreteCreatorA())
    print("\n")

    print("App: Launched with ConcreteCreatorB.")
    client_code(ConcreteCreatorB())


# ÖRNEK 2
from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def deliver(self) -> str:
        pass

class Car(Transport):
    def deliver(self) -> str:
        return "Delivering by Car"

class Bike(Transport):
    def deliver(self) -> str:
        return "Delivering by Bike"

class Bus(Transport):
    def deliver(self) -> str:
        return "Delivering by Bus"

class TransportFactory(ABC):
    @abstractmethod
    def create_transport(self) -> Transport:
        pass

class CarFactory(TransportFactory):
    def create_transport(self) -> Transport:
        return Car()

class BikeFactory(TransportFactory):
    def create_transport(self) -> Transport:
        return Bike()

class BusFactory(TransportFactory):
    def create_transport(self) -> Transport:
        return Bus()

def client_code(factory: TransportFactory) -> None:
    transport = factory.create_transport()
    print(f"Client: Using transport method - {transport.deliver()}")

if __name__ == "__main__":
    print("App: Launched with CarFactory.")
    client_code(CarFactory())
    print("\n")

    print("App: Launched with BikeFactory.")
    client_code(BikeFactory())
    print("\n")

    print("App: Launched with BusFactory.")
    client_code(BusFactory())

# ÖRNEK 3
from abc import ABC, abstractmethod

# Food Interface
class Food(ABC):
    @abstractmethod
    def prepare(self) -> str:
        pass

# Concrete Food Classes
class Pizza(Food):
    def prepare(self) -> str:
        return "Preparing Pizza"

class Burger(Food):
    def prepare(self) -> str:
        return "Preparing Burger"

class Salad(Food):
    def prepare(self) -> str:
        return "Preparing Salad"

# FoodFactory Interface
class FoodFactory(ABC):
    @abstractmethod
    def create_food(self) -> Food:
        pass

# Concrete Food Factories
class PizzaFactory(FoodFactory):
    def create_food(self) -> Food:
        return Pizza()

class BurgerFactory(FoodFactory):
    def create_food(self) -> Food:
        return Burger()

class SaladFactory(FoodFactory):
    def create_food(self) -> Food:
        return Salad()

# Client Code
def client_code(factory: FoodFactory) -> None:
    food = factory.create_food()
    print(f"Client: {food.prepare()}")

if __name__ == "__main__":
    print("App: Launched with PizzaFactory.")
    client_code(PizzaFactory())
    print("\n")

    print("App: Launched with BurgerFactory.")
    client_code(BurgerFactory())
    print("\n")

    print("App: Launched with SaladFactory.")
    client_code(SaladFactory())



# ÖRNEK 4
from abc import ABC, abstractmethod
from unittest import TestCase

class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class PersonFactory(ABC):
    @abstractmethod
    def create_person(self, name) -> Person:
        pass

class IncrementalIdPersonFactory(PersonFactory):
    id = 0

    def create_person(self, name) -> Person:
        person = Person(IncrementalIdPersonFactory.id, name)
        IncrementalIdPersonFactory.id += 1
        return person

class Evaluate(TestCase):
    def test_exercise(self):
        pf = IncrementalIdPersonFactory()
        
        p1 = pf.create_person('Chris')
        self.assertEqual(p1.name, 'Chris')
        self.assertEqual(p1.id, 0)

        p2 = pf.create_person('Sarah')
        self.assertEqual(p2.id, 1)

if __name__ == "__main__":
    import unittest
    unittest.main()
