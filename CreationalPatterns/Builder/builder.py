# ÖRNEK 1
class Pizza:
    def __init__(self):
        self.dough = None
        self.sauce = None
        self.cheese = None
        self.toppings = []

    def __str__(self):
        return f"Pizza with {self.dough} dough, {self.sauce} sauce, {self.cheese} cheese, and toppings: {', '.join(self.toppings)}."

class PizzaBuilder:
    def __init__(self):
        self.reset()

    def reset(self):
        self.pizza = Pizza()

    def set_dough(self, dough):
        self.pizza.dough = dough
        return self

    def set_sauce(self, sauce):
        self.pizza.sauce = sauce
        return self

    def set_cheese(self, cheese):
        self.pizza.cheese = cheese
        return self

    def add_topping(self, topping):
        self.pizza.toppings.append(topping)
        return self

    def build(self):
        built_pizza = self.pizza
        self.reset()  # Reset builder for next build
        return built_pizza

# Kullanım
builder = PizzaBuilder()

pizza1 = (builder
          .set_dough("Thin Crust")
          .set_sauce("Tomato")
          .set_cheese("Mozzarella")
          .add_topping("Pepperoni")
          .add_topping("Mushrooms")
          .build())

pizza2 = (builder
          .set_dough("Thick Crust")
          .set_sauce("BBQ")
          .set_cheese("Cheddar")
          .add_topping("Chicken")
          .add_topping("Onions")
          .add_topping("Bell Peppers")
          .build())

print(pizza1)
print(pizza2)


# ÖRNEK 2
class Car:
    def __init__(self):
        self.engine = None
        self.wheels = None
        self.color = None

    def __str__(self):
        return f"Car with {self.engine} engine, {self.wheels} wheels and {self.color} color."

class CarBuilder:
    def __init__(self):
        self.reset()

    def reset(self):
        self.car = Car()
    
    def set_engine(self, engine):
        self.car.engine = engine
        return self

    def set_wheels(self, wheels):
        self.car.wheels = wheels
        return self

    def set_color(self, color):
        self.car.color = color
        return self

    def build(self):
        built_car = self.car
        self.reset()
        return built_car

builder = CarBuilder()
car1 = (builder
       .set_engine("V8")
       .set_wheels(4)
       .set_color("Red")
       .build())

car2 = (builder
       .set_engine("V6")
       .set_wheels(4)
       .set_color("Black")
       .build()
       )

print(car1)
print(car2)


# ÖRNEK 3
class Computer:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None
        self.gpu = None

    def __str__(self):
        return f"Computer with {self.cpu} CPU, {self.ram} RAM, {self.storage} Storage, and {self.gpu} GPU."

class ComputerBuilder:
    def __init__(self):
        self.reset()

    def reset(self):
        self.computer = Computer()

    def set_cpu(self, cpu):
        self.computer.cpu = cpu
        return self

    def set_ram(self, ram):
        self.computer.ram = ram
        return self

    def set_storage(self, storage):
        self.computer.storage = storage
        return self

    def set_gpu(self, gpu):
        self.computer.gpu = gpu
        return self

    def build(self):
        built_computer = self.computer
        self.reset()
        return built_computer

builder = ComputerBuilder()

computer1 = (builder
             .set_cpu("Intel i7")
             .set_ram("16GB")
             .set_storage("1TB SSD")
             .set_gpu("NVIDIA GTX 3080")
             .build())

computer2 = (builder
             .set_cpu("AMD Ryzen 9")
             .set_ram("32GB")
             .set_storage("2TB SSD")
             .set_gpu("NVIDIA RTX 3090")
             .build())

print(computer1)
print(computer2)
