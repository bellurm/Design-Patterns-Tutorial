# Single Responsibility Principle (SRP), bir sınıfın veya modülün yalnızca tek bir sorumluluğu olması gerektiğini belirtir.
# Yani, bir sınıfın sadece bir işlevi yerine getirmesi ve bu işlevle ilgili nedenlerle değişmesi gerektiğini savunur.
# Örneğin, bir kullanıcı yönetim sistemi tasarlarken, kullanıcı veritabanı işlemlerini yöneten bir sınıf ile kullanıcı arayüz işlemlerini yöneten bir sınıfı ayrı tutmalısınız.
# Bu şekilde, kullanıcı arayüzünde bir değişiklik yapmanız gerektiğinde veritabanı işlemlerini etkileyen bir değişiklik yapmak zorunda kalmazsınız.

# ÖRNEK 1
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

class UserRepository:
    def save(self, user):
        # Save user to the database
        print(f"Saving user {user.username} to the database.")

class UserService:
    def send_email(self, user, message):
        # Send an email to the user
        print(f"Sending email to {user.email}: {message}")

# ÖRNEK 2
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

class UserRepository:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def save(self, user):
        # Code to save user to the database
        print(f"Saving user {user.username} to the database.")

    def find_by_username(self, username):
        # Code to find a user by username
        print(f"Finding user by username: {username}")
        return User(username, f"{username}@example.com")

class EmailService:
    def send_email(self, email, message):
        # Code to send an email
        print(f"Sending email to {email}: {message}")

class UserService:
    def __init__(self, user_repository, email_service):
        self.user_repository = user_repository
        self.email_service = email_service

    def register_user(self, username, email):
        user = User(username, email)
        self.user_repository.save(user)
        self.email_service.send_email(user.email, "Welcome!")

a = User("cw", "cw@gmail.com")
b = EmailService()
print(a.username, a.email)
print(b.send_email(a.email, "deneme"))


# ÖRNEK 3
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

class UserRepository:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def save(self, user):
        # Code to save user to the database
        print(f"Saving user {user.username} to the database.")

    def find_by_username(self, username):
        # Code to find a user by username
        print(f"Finding user by username: {username}")
        return User(username, f"{username}@example.com")

class EmailService:
    def send_email(self, email, subject, message):
        # Code to send an email
        print(f"Sending email to {email}: {subject} - {message}")

class UserService:
    def __init__(self, user_repository, email_service):
        self.user_repository = user_repository
        self.email_service = email_service

    def register_user(self, username, email):
        user = User(username, email)
        self.user_repository.save(user)
        self.email_service.send_email(user.email, "Welcome", "Welcome to our platform!")

    def reset_password(self, username):
        user = self.user_repository.find_by_username(username)
        new_password = self.generate_random_password()
        # Assume we save the new password to the database here
        self.email_service.send_email(user.email, "Password Reset", f"Your new password is: {new_password}")

    def generate_random_password(self):
        import random
        import string
        return ''.join(random.choices(string.ascii_letters + string.digits, k=8))
