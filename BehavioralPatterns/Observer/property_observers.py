# ÖRNEK 1
class ObservableProperty:
    def __init__(self, initial_value=None):
        self._value = initial_value
        self._observers = []

    def add_observer(self, observer_func):
        self._observers.append(observer_func)

    def notify_observers(self):
        for observer in self._observers:
            observer(self._value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value
        self.notify_observers()

# Kullanım
def observer_func(value):
    print(f"Property changed to {value}")

prop = ObservableProperty(10)
prop.add_observer(observer_func)
prop.value = 20  # Output: Property changed to 20

print("#"*70)

# ÖRNEK 2
class UserProfile:
    def __init__(self, username, email):
        self._username = username
        self._email = email
        self._observers = []

    def add_observer(self, observer_func):
        self._observers.append(observer_func)

    def notify_observers(self, property_name, value):
        for observer in self._observers:
            observer(property_name, value)

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, new_username):
        self._username = new_username
        self.notify_observers('username', new_username)

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email):
        self._email = new_email
        self.notify_observers('email', new_email)


def user_profile_observer(property_name, value):
    print(f'User profile updated: {property_name} changed to {value}')


# Kullanım
user_profile = UserProfile('john_doe', 'john@example.com')
user_profile.add_observer(user_profile_observer)

user_profile.username = 'johnny_doe'
user_profile.email = 'johnny@example.com'

# Çıktı:
# User profile updated: username changed to johnny_doe
# User profile updated: email changed to johnny@example.com
