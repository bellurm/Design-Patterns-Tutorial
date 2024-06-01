# ÖRNEK 1
from abc import ABC, abstractmethod

class Handler(ABC):
    def __init__(self, successor=None):
        self._successor = successor

    @abstractmethod
    def handle(self, request):
        pass

class ConcreteHandler1(Handler):
    def handle(self, request):
        if request == "Request1":
            return f"ConcreteHandler1 handled {request}"
        elif self._successor:
            return self._successor.handle(request)
        else:
            return "No handler could handle the request"

class ConcreteHandler2(Handler):
    def handle(self, request):
        if request == "Request2":
            return f"ConcreteHandler2 handled {request}"
        elif self._successor:
            return self._successor.handle(request)
        else:
            return "No handler could handle the request"

class ConcreteHandler3(Handler):
    def handle(self, request):
        if request == "Request3":
            return f"ConcreteHandler3 handled {request}"
        elif self._successor:
            return self._successor.handle(request)
        else:
            return "No handler could handle the request"

# Zinciri oluşturma
handler_chain = ConcreteHandler1(
                    ConcreteHandler2(
                        ConcreteHandler3()))

# İstekleri işleme
print(handler_chain.handle("Request1"))
print(handler_chain.handle("Request2"))
print(handler_chain.handle("Request3"))
print(handler_chain.handle("Request4"))

print("#"*70)

# ÖRNEK 2
class SupportRequest:
    def __init__(self, level, message):
        self.level = level
        self.message = message

class Handler(ABC):
    def __init__(self, successor=None):
        self._successor = successor

    @abstractmethod
    def handle(self, request):
        pass

class LowLevelSupport(Handler):
    def handle(self, request):
        if request.level == "low":
            return f"LowLevelSupport: Handling request '{request.message}'"
        elif self._successor:
            return self._successor.handle(request)
        else:
            return f"No handler could handle the request '{request.message}'"

class MidLevelSupport(Handler):
    def handle(self, request):
        if request.level == "mid":
            return f"MidLevelSupport: Handling request '{request.message}'"
        elif self._successor:
            return self._successor.handle(request)
        else:
            return f"No handler could handle the request '{request.message}'"

class HighLevelSupport(Handler):
    def handle(self, request):
        if request.level == "high":
            return f"HighLevelSupport: Handling request '{request.message}'"
        elif self._successor:
            return self._successor.handle(request)
        else:
            return f"No handler could handle the request '{request.message}'"

# Zinciri oluşturma
support_chain = LowLevelSupport(
                    MidLevelSupport(
                        HighLevelSupport()))

# İstekleri işleme
requests = [
    SupportRequest("low", "Password reset request"),
    SupportRequest("mid", "Unable to connect to VPN"),
    SupportRequest("high", "System outage"),
    SupportRequest("critical", "Data breach")
]

for request in requests:
    print(support_chain.handle(request))
    