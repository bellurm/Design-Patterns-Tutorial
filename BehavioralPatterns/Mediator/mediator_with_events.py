# Event Mediator
class EventMediator:
    def __init__(self):
        self._events = {}

    def subscribe(self, event_type, listener):
        if event_type not in self._events:
            self._events[event_type] = []
        self._events[event_type].append(listener)

    def unsubscribe(self, event_type, listener):
        if event_type in self._events:
            self._events[event_type].remove(listener)

    def publish(self, event_type, *args, **kwargs):
        if event_type in self._events:
            for listener in self._events[event_type]:
                listener(*args, **kwargs)

# Publisher ve Subscriber
class User:
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator

    def send_message(self, message):
        print(f"{self.name} sends: {message}")
        self.mediator.publish("message", self.name, message)

    def receive_message(self, sender_name, message):
        if sender_name != self.name:
            print(f"{self.name} receives from {sender_name}: {message}")

def user_message_listener(user, sender_name, message):
    user.receive_message(sender_name, message)

# Kullanım
if __name__ == "__main__":
    mediator = EventMediator()

    user1 = User("John", mediator)
    user2 = User("Jane", mediator)
    user3 = User("Alice", mediator)

    mediator.subscribe("message", lambda sender_name, message: user1.receive_message(sender_name, message))
    mediator.subscribe("message", lambda sender_name, message: user2.receive_message(sender_name, message))
    mediator.subscribe("message", lambda sender_name, message: user3.receive_message(sender_name, message))

    user1.send_message("Hello everyone!")
    user2.send_message("Hi John!")
    user3.send_message("Hey folks!")
