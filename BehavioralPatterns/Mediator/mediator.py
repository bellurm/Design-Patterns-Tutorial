from abc import ABC, abstractmethod

# Mediator arayüzü
class ChatRoomMediator(ABC):
    @abstractmethod
    def show_message(self, user, message):
        pass

# Concrete Mediator
class ChatRoom(ChatRoomMediator):
    def show_message(self, user, message):
        print(f"[{user.name}]: {message}")

# Colleague sınıfı
class User:
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator

    def send_message(self, message):
        self.mediator.show_message(self, message)

# Kullanım
mediator = ChatRoom()
user1 = User("John", mediator)
user2 = User("Jane", mediator)

user1.send_message("Hello, Jane!")
user2.send_message("Hi, John! How are you?")
