# Logginge Proxy ile bir nesneye yapılan tüm işlemleri log dosyasına yazan
from abc import ABC, abstractmethod

# Subject
class Service(ABC):
    @abstractmethod
    def execute(self):
        pass

# RealSubject
class RealService(Service):
    def execute(self):
        print("Executing service")

# Proxy
class LoggingProxy(Service):
    def __init__(self, service):
        self.service = service

    def execute(self):
        print("Logging: Service is about to be executed")
        self.service.execute()
        print("Logging: Service has been executed")

# Client
def main():
    service = RealService()
    logging_proxy = LoggingProxy(service)
    logging_proxy.execute()

if __name__ == "__main__":
    main()
