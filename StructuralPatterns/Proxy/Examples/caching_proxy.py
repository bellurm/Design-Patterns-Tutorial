# Caching Proxy ile veritabanı sorgularının sonuçlarını önbellekte tutmak
from abc import ABC, abstractmethod

# Subject
class Database(ABC):
    @abstractmethod
    def query(self, sql):
        pass

# RealSubject
class RealDatabase(Database):
    def query(self, sql):
        # Simulating a database query
        print(f"Executing query: {sql}")
        return f"Result of '{sql}'"

# Proxy
class CachingProxy(Database):
    def __init__(self):
        self.real_database = RealDatabase()
        self.cache = {}

    def query(self, sql):
        if sql in self.cache:
            print("Returning cached result")
            return self.cache[sql]
        else:
            result = self.real_database.query(sql)
            self.cache[sql] = result
            return result

# Client
def main():
    db = CachingProxy()
    # First query, result will be fetched from the database
    result1 = db.query("SELECT * FROM users")
    print(result1)
    # Second query, result will be returned from the cache
    result2 = db.query("SELECT * FROM users")
    print(result2)

if __name__ == "__main__":
    main()
