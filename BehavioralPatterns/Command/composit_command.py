# ÖRNEK 1
from abc import ABC, abstractmethod
from typing import List

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

# Composite Command Sınıfı
class CompositeCommand(Command):
    def __init__(self):
        self.commands: List[Command] = []

    def add_command(self, command: Command):
        self.commands.append(command)

    def execute(self):
        for command in self.commands:
            command.execute()

# Kullanım
light = Light()
light_on = LightOnCommand(light)
light_off = LightOffCommand(light)

composite_command = CompositeCommand()
composite_command.add_command(light_on)
composite_command.add_command(light_off)

# Tüm komutlar tek bir komut gibi çalıştırılır
composite_command.execute()
# Çıktı:
# Light is on
# Light is off

print("#"*70)

# ÖRNEK 2

from abc import ABC, abstractmethod
from typing import List

# Command Arayüzü
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# Receiver Sınıfı
class FileProcessor:
    def open_file(self):
        print("Dosya açılıyor")

    def close_file(self):
        print("Dosya kapatılıyor")

# Composite Command Sınıfı
class CompositeCommand(Command):
    def __init__(self):
        self.commands: List[Command] = []

    def add_command(self, command: Command):
        self.commands.append(command)

    def execute(self):
        for command in self.commands:
            command.execute()

# ConcreteCommand Sınıfları
class OpenAndCloseFile(CompositeCommand):
    def __init__(self, file_processor: FileProcessor):
        super().__init__()
        self.file_processor = file_processor
        self.add_command(OpenFile(file_processor))
        self.add_command(CloseFile(file_processor))

class OpenFile(Command):
    def __init__(self, file_processor: FileProcessor):
        self.file_processor = file_processor

    def execute(self):
        self.file_processor.open_file()

class CloseFile(Command):
    def __init__(self, file_processor: FileProcessor):
        self.file_processor = file_processor

    def execute(self):
        self.file_processor.close_file()

# Kullanım
file_processor = FileProcessor()
open_and_close_command = OpenAndCloseFile(file_processor)

open_and_close_command.execute()
# Çıktı:
# Dosya açılıyor
# Dosya kapatılıyor
