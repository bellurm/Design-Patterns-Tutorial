# ÖRNEK 1
from abc import ABC, abstractmethod

# Command Arayüzü
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# Receiver Sınıfı
class Light:
    def turn_on(self):
        print("Light is on")

    def turn_off(self):
        print("Light is off")

# ConcreteCommand Sınıfları
class LightOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.turn_on()

class LightOffCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.turn_off()

# Invoker Sınıfı
class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command: Command):
        self.command = command

    def press_button(self):
        if self.command:
            self.command.execute()

# Kullanım
light = Light()
light_on = LightOnCommand(light)
light_off = LightOffCommand(light)

remote = RemoteControl()
remote.set_command(light_on)
remote.press_button()  # Çıktı: Light is on

remote.set_command(light_off)
remote.press_button()  # Çıktı: Light is off

print("#"*70)

# ÖRNEK 2
from abc import ABC, abstractmethod

# Command Arayüzü
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# Receiver Sınıfı
class Kitchen:
    def prepare_pasta(self):
        print("Pasta hazırlanıyor")

    def prepare_salad(self):
        print("Salata hazırlanıyor")

# ConcreteCommand Sınıfları
class PastaOrder(Command):
    def __init__(self, kitchen: Kitchen):
        self.kitchen = kitchen

    def execute(self):
        self.kitchen.prepare_pasta()

class SaladOrder(Command):
    def __init__(self, kitchen: Kitchen):
        self.kitchen = kitchen

    def execute(self):
        self.kitchen.prepare_salad()

# Invoker Sınıfı
class Waiter:
    def __init__(self):
        self.order = None

    def set_order(self, order: Command):
        self.order = order

    def place_order(self):
        if self.order:
            self.order.execute()

# Kullanım
kitchen = Kitchen()
pasta_order = PastaOrder(kitchen)
salad_order = SaladOrder(kitchen)

waiter = Waiter()
waiter.set_order(pasta_order)
waiter.place_order()  # Çıktı: Pasta hazırlanıyor

waiter.set_order(salad_order)
waiter.place_order()  # Çıktı: Salata hazırlanıyor
