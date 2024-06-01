import threading
import queue
import time
from abc import ABC, abstractmethod

# Mediator Arayüzü ve Somut Mediator
class ChatRoomMediator(ABC):
    @abstractmethod
    def show_message(self, user, message):
        pass

class ChatRoom(ChatRoomMediator):
    def __init__(self):
        self.users = []
        self.message_queue = queue.Queue()

    def add_user(self, user):
        self.users.append(user)

    def show_message(self, user, message):
        for u in self.users:
            if u != user:
                u.receive_message(user, message)

    def run(self):
        while True:
            if not self.message_queue.empty():
                user, message = self.message_queue.get()
                self.show_message(user, message)
            time.sleep(0.1)

    def send_message(self, user, message):
        self.message_queue.put((user, message))

# Kullanıcı Sınıfı
class User:
    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator
        self.mediator.add_user(self)

    def send_message(self, message):
        print(f"{self.name} sends: {message}")
        self.mediator.send_message(self, message)

    def receive_message(self, sender, message):
        print(f"{self.name} receives from {sender.name}: {message}")

# Chat
def user_input(user):
    while True:
        message = input(f"{user.name}: ")
        user.send_message(message)

if __name__ == "__main__":
    mediator = ChatRoom()

    user1 = User("John", mediator)
    user2 = User("Jane", mediator)
    user3 = User("Alice", mediator)

    mediator_thread = threading.Thread(target=mediator.run)
    mediator_thread.daemon = True
    mediator_thread.start()

    user1_thread = threading.Thread(target=user_input, args=(user1,))
    user2_thread = threading.Thread(target=user_input, args=(user2,))
    user3_thread = threading.Thread(target=user_input, args=(user3,))

    user1_thread.start()
    user2_thread.start()
    user3_thread.start()

    user1_thread.join()
    user2_thread.join()
    user3_thread.join()
