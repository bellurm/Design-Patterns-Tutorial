# Interface Segregation Principle (ISP), bir sınıfın kullanmadığı metodları içeren büyük arayüzlerden ziyade,
# daha spesifik ve küçük arayüzlerin tercih edilmesi gerektiğini savunur.
# Bu, sınıfların yalnızca ihtiyaç duydukları fonksiyonlara bağlı olmasını sağlar ve gereksiz bağımlılıkları azaltır.
# Örneğin, bir yazıcı arayüzü oluştururken, "Baskı Yap" ve "Tarama Yap" gibi farklı işlevleri ayrı arayüzlere ayırmalısınız,
# böylece tarama yapmayan bir yazıcı, gereksiz yere "Tarama Yap" metodunu implement etmek zorunda kalmaz.

# ÖRNEK 1
from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print_document(self, document):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan_document(self):
        pass

class MultiFunctionPrinter(Printer, Scanner):
    def print_document(self, document):
        print(f"Printing: {document}")

    def scan_document(self):
        print("Scanning document")

class SimplePrinter(Printer):
    def print_document(self, document):
        print(f"Printing: {document}")


# ÖRNEK 2
from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print_document(self, document):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan_document(self):
        pass

class Fax(ABC):
    @abstractmethod
    def send_fax(self, document):
        pass

class MultiFunctionMachine(Printer, Scanner, Fax):
    def print_document(self, document):
        print(f"Printing: {document}")

    def scan_document(self):
        print("Scanning document")

    def send_fax(self, document):
        print(f"Sending fax: {document}")

class SimplePrinter(Printer):
    def print_document(self, document):
        print(f"Printing: {document}")


# ÖRNEK 3
from abc import ABC, abstractmethod

class Authenticator(ABC):
    @abstractmethod
    def authenticate(self, username, password):
        pass

class OTPAuthenticator(ABC):
    @abstractmethod
    def send_otp(self, phone_number):
        pass

    @abstractmethod
    def verify_otp(self, phone_number, otp):
        pass

class BasicAuthenticator(Authenticator):
    def authenticate(self, username, password):
        # Basic username and password authentication
        print(f"Authenticating {username} with password.")

class TwoFactorAuthenticator(Authenticator, OTPAuthenticator):
    def authenticate(self, username, password):
        # Authenticate with username and password
        print(f"Authenticating {username} with password.")

    def send_otp(self, phone_number):
        # Send OTP to phone number
        print(f"Sending OTP to {phone_number}")

    def verify_otp(self, phone_number, otp):
        # Verify OTP
        print(f"Verifying OTP for {phone_number}")
