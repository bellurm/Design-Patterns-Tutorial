# Abstract Products (Soyut Ürünler)
from abc import ABC, abstractmethod

class Engine(ABC):
    @abstractmethod
    def get_description(self) -> str:
        pass

class Seat(ABC):
    @abstractmethod
    def get_description(self) -> str:
        pass

# Concrete Products (Somut Ürünler)
class ToyotaEngine(Engine):
    def get_description(self) -> str:
        return "Toyota Engine"

class ToyotaSeat(Seat):
    def get_description(self) -> str:
        return "Toyota Seat"

class FordEngine(Engine):
    def get_description(self) -> str:
        return "Ford Engine"

class FordSeat(Seat):
    def get_description(self) -> str:
        return "Ford Seat"

# Abstract Factory (Soyut Fabrika)
class CarFactory(ABC):
    @abstractmethod
    def create_engine(self) -> Engine:
        pass

    @abstractmethod
    def create_seat(self) -> Seat:
        pass

# Concrete Factories (Somut Fabrikalar)
class ToyotaFactory(CarFactory):
    def create_engine(self) -> Engine:
        return ToyotaEngine()

    def create_seat(self) -> Seat:
        return ToyotaSeat()

class FordFactory(CarFactory):
    def create_engine(self) -> Engine:
        return FordEngine()

    def create_seat(self) -> Seat:
        return FordSeat()

# Client Code (İstemci Kodu)
def client_code(factory: CarFactory) -> None:
    engine = factory.create_engine()
    seat = factory.create_seat()
    print(f"Engine: {engine.get_description()}")
    print(f"Seat: {seat.get_description()}")

if __name__ == "__main__":
    print("Client: Testing client code with ToyotaFactory:")
    client_code(ToyotaFactory())
    print("\n")

    print("Client: Testing client code with FordFactory:")
    client_code(FordFactory())
