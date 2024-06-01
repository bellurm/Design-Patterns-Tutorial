# ÖRNEK 1
class MyIterator:
    def __init__(self, collection):
        self._collection = collection
        self._index = 0

    def __next__(self):
        try:
            value = self._collection[self._index]
            self._index += 1
            return value
        except IndexError:
            raise StopIteration

class MyCollection:
    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    def __iter__(self):
        return MyIterator(self._items)

# Kullanım
collection = MyCollection()
collection.add_item(1)
collection.add_item(2)
collection.add_item(3)

for item in collection:
    print(item)

print("#"*70)

# ÖRNEK 2
import itertools

# sonsuz bir sayı dizisi oluşturma
counter = itertools.count(start=0, step=1)

for number in counter:
    if number > 10:
        break
    print(number)

# iki koleksiyonu ardışık olarak birleştirme
combined = itertools.chain([1, 2, 3], ['a', 'b', 'c'])
for item in combined:
    print(item)

print("#"*70)

# ÖRNEK 3
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        return f"'{self.title}' by {self.author}"

class LibraryIterator:
    def __init__(self, books):
        self._books = books
        self._index = 0

    def __next__(self):
        if self._index < len(self._books):
            book = self._books[self._index]
            self._index += 1
            return book
        else:
            raise StopIteration

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def __iter__(self):
        return LibraryIterator(self._books)

# Kullanım
library = Library()
library.add_book(Book("1984", "George Orwell"))
library.add_book(Book("To Kill a Mockingbird", "Harper Lee"))
library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald"))

for book in library:
    print(book)
