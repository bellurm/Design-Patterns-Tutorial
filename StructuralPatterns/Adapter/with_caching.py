# Bir veri kaynağından kullanıcı bilgilerini alan ve bu bilgileri önbellekte tutarak tekrar tekrar orijinal kaynağa erişimi azaltan bir adaptör.

class OldUserService:
    def get_user_data(self, user_id: int):
        # Orijinal kaynaktan veri alıyor (örneğin bir veritabanı)
        return f"User data for user_id {user_id}"

class UserService:
    def fetch_user(self, user_id: int):
        pass

class CachingUserAdapter(UserService):
    def __init__(self, old_user_service: OldUserService):
        self.old_user_service = old_user_service
        self.cache = {}

    def fetch_user(self, user_id: int):
        if user_id not in self.cache:
            self.cache[user_id] = self.old_user_service.get_user_data(user_id)
        return self.cache[user_id]

class UserClient:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def get_user(self, user_id: int):
        return self.user_service.fetch_user(user_id)

old_user_service = OldUserService()
caching_adapter = CachingUserAdapter(old_user_service)
user_client = UserClient(caching_adapter)

# Kullanıcı verisini al (ilk çağrı orijinal kaynağa gider, ikincisi önbellekten gelir)
print(user_client.get_user(1))  # İlk çağrı orijinal kaynağa gider
print(user_client.get_user(1))  # İkinci çağrı önbellekten gelir
