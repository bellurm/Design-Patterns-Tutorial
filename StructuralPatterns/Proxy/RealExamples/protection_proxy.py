from abc import ABC, abstractmethod

class LibraryResource(ABC):
    @abstractmethod
    def borrow_book(self, user):
        pass

class RealLibraryResource(LibraryResource):
    def __init__(self):
        self.books = {
            "Python Programming": "Available",
            "Data Structures and Algorithms": "Available",
            "Machine Learning Basics": "Not Available"
        }

    def borrow_book(self, user, book_name):
        if self.books.get(book_name) == "Available":
            self.books[book_name] = user.role  # Kitabın durumunu kullanıcının rolü olarak güncelle
            return f"{book_name} successfully borrowed by {user.name}"
        else:
            return f"{book_name} is not available or already borrowed"


class ProtectionProxy(LibraryResource):
    def __init__(self, real_resource):
        self.real_resource = real_resource

    def borrow_book(self, user, book_name):
        if user.role == "Student":
            return "Students are not allowed to borrow books"
        elif user.role == "Librarian" or user.role == "Teacher":
            return self.real_resource.borrow_book(user, book_name)

class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

# Örnek Kullanım
def main():
    # Kullanıcılar oluştur
    student = User("Alice", "Student")
    librarian = User("Bob", "Librarian")

    # Gerçek kaynak ve koruma proxy'si oluştur
    real_resource = RealLibraryResource()
    proxy = ProtectionProxy(real_resource)

    # Öğrenci kitap ödünç alır (koruma proxy engeller)
    print(proxy.borrow_book(student, "Python Programming"))  # Çıktı: Students are not allowed to borrow books

    # Kütüphaneci kitap ödünç alır (koruma proxy'i izin verir)
    print(proxy.borrow_book(librarian, "Python Programming"))  # Çıktı: Python Programming successfully borrowed by Bob

    # Öğrenci kitap ödünç alır (koruma proxy engeller)
    print(real_resource.borrow_book(student, "Machine Learning Basics"))

if __name__ == "__main__":
    main()
