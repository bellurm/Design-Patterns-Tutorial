# Protection Proxy ile belirli rollere sahip kullanıcıların erişimini denetlemek
from abc import ABC, abstractmethod

# Subject
class Document(ABC):
    @abstractmethod
    def display(self):
        pass

# RealSubject
class RealDocument(Document):
    def __init__(self, content):
        self.content = content

    def display(self):
        print(f"Document content: {self.content}")

# Proxy
class ProtectionProxy(Document):
    def __init__(self, document, user_role):
        self.document = document
        self.user_role = user_role

    def display(self):
        if self.user_role == "admin":
            self.document.display()
        else:
            print("Access denied: insufficient permissions")

# Client
def main():
    document = RealDocument("Sensitive content")
    proxy = ProtectionProxy(document, "user")
    proxy.display()  # Access denied

    admin_proxy = ProtectionProxy(document, "admin")
    admin_proxy.display()  # Document content displayed

if __name__ == "__main__":
    main()
