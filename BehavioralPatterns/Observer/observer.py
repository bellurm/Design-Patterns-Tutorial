# ÖRNEK 1
class Subject:
    def __init__(self):
        self._observers = []

    def register_observer(self, observer):
        self._observers.append(observer)

    def unregister_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self)

class Observer:
    def update(self, subject):
        pass

# Concrete Subject
class ConcreteSubject(Subject):
    def __init__(self):
        super().__init__()
        self._state = None

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
        self.notify_observers()

# Concrete Observer
class ConcreteObserver(Observer):
    def update(self, subject):
        print(f'Observer: Subject state has been updated to {subject.state}')

# Kullanım
subject = ConcreteSubject()
observer1 = ConcreteObserver()
observer2 = ConcreteObserver()

subject.register_observer(observer1)
subject.register_observer(observer2)

subject.state = 'Yeni Durum'
# Çıktı:
# Observer: Subject state has been updated to Yeni Durum
# Observer: Subject state has been updated to Yeni Durum

print("#"*70)

# ÖRNEK 2
class NewsPublisher:
    def __init__(self):
        self._subscribers = {}
        self._news = {}

    def register_subscriber(self, category, subscriber):
        if category not in self._subscribers:
            self._subscribers[category] = []
        self._subscribers[category].append(subscriber)

    def unregister_subscriber(self, category, subscriber):
        if category in self._subscribers:
            self._subscribers[category].remove(subscriber)

    def notify_subscribers(self, category):
        if category in self._subscribers:
            for subscriber in self._subscribers[category]:
                subscriber.update(self._news[category])

    def add_news(self, category, news):
        if category not in self._news:
            self._news[category] = []
        self._news[category].append(news)
        self.notify_subscribers(category)


class Subscriber:
    def __init__(self, name):
        self._name = name

    def update(self, news):
        print(f'{self._name} received news: {news[-1]}')


# Kullanım
news_publisher = NewsPublisher()

# Aboneler oluştur
subscriber1 = Subscriber('Alice')
subscriber2 = Subscriber('Bob')

# Aboneleri kategorilere ekle
news_publisher.register_subscriber('Sports', subscriber1)
news_publisher.register_subscriber('Technology', subscriber2)
news_publisher.register_subscriber('Sports', subscriber2)

# Haber ekle ve abonelere bildir
news_publisher.add_news('Sports', 'New sports event coming up!')
news_publisher.add_news('Technology', 'New tech gadget released!')
news_publisher.add_news('Sports', 'Sports team wins championship!')

# Çıktı:
# Alice received news: New sports event coming up!
# Bob received news: New sports event coming up!
# Bob received news: New tech gadget released!
# Alice received news: Sports team wins championship!
# Bob received news: Sports team wins championship!
