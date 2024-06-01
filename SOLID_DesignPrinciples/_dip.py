# Dependency Inversion Principle (DIP), yüksek seviye modüllerin (iş mantığını içeren) düşük seviye modüllere (uygulama detayları) bağımlı olmaması gerektiğini,
# bunun yerine her ikisinin de soyutlamalara bağımlı olması gerektiğini belirtir.
# Bu, sistem bileşenlerinin birbirine sıkı sıkıya bağımlı olmasını engelleyerek esnekliği artırır.
# Örneğin, bir raporlama modülü doğrudan bir veritabanı sınıfına bağımlı olmak yerine, bir veri erişim arayüzüne bağımlı olmalıdır.
# Böylece, veritabanı sınıfını değiştirmek gerektiğinde sadece arayüzü implement eden yeni bir sınıf yazmanız yeterli olur.

# ÖRNEK 1
from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def save(self, data):
        pass

class MySQLDatabase(Database):
    def save(self, data):
        print("Saving data to MySQL database")

class MongoDBDatabase(Database):
    def save(self, data):
        print("Saving data to MongoDB database")

class DataService:
    def __init__(self, database: Database):
        self.database = database

    def save_data(self, data):
        self.database.save(data)


# ÖRNEK 2
from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log(self, message):
        pass

class FileLogger(Logger):
    def log(self, message):
        print(f"Logging to a file: {message}")

class DatabaseLogger(Logger):
    def log(self, message):
        print(f"Logging to a database: {message}")

class Application:
    def __init__(self, logger: Logger):
        self.logger = logger

    def run(self):
        self.logger.log("Application has started.")
        # Application logic
        self.logger.log("Application has finished.")


# ÖRNEK 3
from abc import ABC, abstractmethod

class MessageSender(ABC):
    @abstractmethod
    def send_message(self, recipient, message):
        pass

class EmailSender(MessageSender):
    def send_message(self, recipient, message):
        print(f"Sending email to {recipient}: {message}")

class SMSSender(MessageSender):
    def send_message(self, recipient, message):
        print(f"Sending SMS to {recipient}: {message}")

class NotificationService:
    def __init__(self, sender: MessageSender):
        self.sender = sender

    def notify(self, recipient, message):
        self.sender.send_message(recipient, message)
