# Interface Segregation Principle (ISP), yazılım tasarımında, bir arayüzün kullanıcılara ihtiyaçlarına göre bölünmesi gerektiğini belirten bir prensiptir.
# Bu prensip, bir arayüzü, onu kullanan sınıfların ihtiyaçlarına uygun daha küçük ve spesifik arayüzler haline getirmeyi önerir.
# Yani, bir arayüzde bulunan tüm metotlar, onu kullanan sınıflar tarafından kullanılmak zorunda olmamalıdır.

# ISP'nin temel fikri, kullanıcıların ihtiyaç duymadığı metotların ve davranışların zorunlu olmamasıdır.
# Bu, gereksiz bağımlılıkların azaltılmasına ve sınıflar arasındaki kavramsal bütünlüğün artırılmasına yardımcı olur. 
# Ayrıca, bir arayüzün değişikliklere karşı daha esnek hale gelmesini sağlar, çünkü arayüz, yalnızca onu kullanacak sınıfların ihtiyaçlarına göre tasarlanır.

# İşte Interface Segregation Principle'ın bazı anahtar noktaları:

# Geniş Arayüzlerden Kaçınma: Bir arayüz, onu kullanan sınıfların tüm ihtiyaçlarını karşılamaya çalışmak yerine, daha küçük ve spesifik arayüzler haline getirilmelidir.
# Bu, sınıfların yalnızca ihtiyaç duydukları metotları uygulamalarını sağlar.

# Birden Fazla Arayüz Kullanımı: Sınıflar, ihtiyaç duydukları davranışları sağlamak için birden fazla arayüzü uygulayabilirler.
# Böylece, her arayüz belirli bir sorumluluğu temsil eder ve sınıflar ihtiyaçlarına göre uygun arayüzleri seçebilirler.

# Değişikliklere Karşı Esneklik: Arayüzler, onları uygulayan sınıfların ihtiyaçlarına göre düzenlenir.
# Bu da, bir arayüzün değişmesi durumunda sadece ilgili sınıfların etkilenmesini sağlar ve diğerlerini etkilemez.

# ISP'nin amacı, sınıflar arasındaki bağımlılıkları azaltmak ve sınıfların esnekliğini artırmaktır.
# Bu sayede, yazılım daha bakımı kolay, genişletilebilir ve yeniden kullanılabilir hale gelir.

# Geniş arayüz
class Vehicle:
    def start(self):
        pass

    def stop(self):
        pass

    def accelerate(self):
        pass

    def fly(self):
        pass

# Spesifik arayüzler
class RoadVehicle:
    def start(self):
        pass

    def stop(self):
        pass

    def accelerate(self):
        pass

class AirVehicle:
    def start(self):
        pass

    def stop(self):
        pass

    def fly(self):
        pass


class Car(RoadVehicle):
    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")

    def accelerate(self):
        print("Car accelerated")

class Airplane(AirVehicle):
    def start(self):
        print("Airplane started")

    def stop(self):
        print("Airplane stopped")

    def fly(self):
        print("Airplane flying")
############################################################################################################################################################################################################
############################################################################################################################################################################################################
############################################################################################################################################################################################################
############################################################################################################################################################################################################
############################################################################################################################################################################################################
############################################################################################################################################################################################################
############################################################################################################################################################################################################
############################################################################################################################################################################################################
############################################################################################################################################################################################################
############################################################################################################################################################################################################
############################################################################################################################################################################################################
from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print(self, document): pass

class Scanner(ABC):
    @abstractmethod
    def scan(self, document): pass

class MyPrinter(Printer):
    def print(self, document):
        print(document)

class Photocopier(Printer, Scanner):
    def print(self, document):
        print(document)

    def scan(self, document):
        pass  # something meaningful

class MultiFunctionDevice(Printer, Scanner):
    @abstractmethod
    def print(self, document): pass

    @abstractmethod
    def scan(self, document): pass

class MultiFunctionMachine(MultiFunctionDevice):
    def __init__(self, printer, scanner):
        self.printer = printer
        self.scanner = scanner

    def print(self, document):
        self.printer.print(document)

    def scan(self, document):
        self.scanner.scan(document)

printer = MyPrinter()
printer.print(123)

photocopier = Photocopier()
photocopier.print(123)
photocopier.scan(123)

multi_function_machine = MultiFunctionMachine(MyPrinter(), Photocopier())
multi_function_machine.print(123)
multi_function_machine.scan(123)
