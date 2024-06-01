from abc import ABC, abstractmethod

class Message:
    def __init__(self, content, priority):
        self.content = content
        self.priority = priority

class Handler(ABC):
    def __init__(self, successor=None):
        self._successor = successor

    @abstractmethod
    def handle(self, message):
        pass

class LowPriorityHandler(Handler):
    def handle(self, message):
        if message.priority == "low":
            return f"LowPriorityHandler: Handling message '{message.content}'"
        elif self._successor:
            return self._successor.handle(message)
        else:
            return f"No handler could handle the message '{message.content}'"

class HighPriorityHandler(Handler):
    def handle(self, message):
        if message.priority == "high":
            return f"HighPriorityHandler: Handling message '{message.content}'"
        elif self._successor:
            return self._successor.handle(message)
        else:
            return f"No handler could handle the message '{message.content}'"

# Zinciri oluşturma
broker_chain = LowPriorityHandler(HighPriorityHandler())

# Mesajları işleme
messages = [
    Message("This is a low priority message", "low"),
    Message("This is a high priority message", "high"),
    Message("This is an unknown priority message", "unknown")
]

for msg in messages:
    print(broker_chain.handle(msg))