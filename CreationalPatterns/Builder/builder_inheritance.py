class Vehicle:
    def __init__(self):
        self.type = None
        self.engine = None
        self.wheels = None
        self.color = None

    def __str__(self):
        return f"{self.color} {self.type} with {self.engine} engine and {self.wheels} wheels."

class VehicleBuilder:
    def __init__(self):
        self.vehicle = Vehicle()

    def set_type(self, type):
        self.vehicle.type = type
        return self

    def set_engine(self, engine):
        self.vehicle.engine = engine
        return self

    def set_wheels(self, wheels):
        self.vehicle.wheels = wheels
        return self

    def set_color(self, color):
        self.vehicle.color = color
        return self

    def build(self):
        return self.vehicle

class CarBuilder(VehicleBuilder):
    def __init__(self):
        super().__init__()
        self.set_type("Car")

    def set_car_doors(self, doors):
        self.vehicle.doors = doors
        return self

class MotorcycleBuilder(VehicleBuilder):
    def __init__(self):
        super().__init__()
        self.set_type("Motorcycle")

    def set_handlebar_type(self, handlebar_type):
        self.vehicle.handlebar_type = handlebar_type
        return self

# Kullanım
car_builder = CarBuilder()
car = (car_builder
       .set_engine("V8")
       .set_wheels(4)
       .set_color("Red")
       .set_car_doors(4)
       .build())

motorcycle_builder = MotorcycleBuilder()
motorcycle = (motorcycle_builder
              .set_engine("500cc")
              .set_wheels(2)
              .set_color("Black")
              .set_handlebar_type("Sport")
              .build())

print(car)
print(motorcycle)
