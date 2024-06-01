# Bir veri kaynağından kullanıcı bilgilerini alan ve her seferinde orijinal kaynağı çağıran bir adaptör.

class OldUserService:
    def get_user_data(self, user_id: int):
        # Orijinal kaynaktan veri alıyor (örneğin bir veritabanı)
        return f"User data for user_id {user_id}"

class UserService:
    def fetch_user(self, user_id: int):
        pass

class NoCachingUserAdapter(UserService):
    def __init__(self, old_user_service: OldUserService):
        self.old_user_service = old_user_service

    def fetch_user(self, user_id: int):
        return self.old_user_service.get_user_data(user_id)

class UserClient:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def get_user(self, user_id: int):
        return self.user_service.fetch_user(user_id)

old_user_service = OldUserService()
no_cache_adapter = NoCachingUserAdapter(old_user_service)
user_client = UserClient(no_cache_adapter)

print(user_client.get_user(1))  # Her seferinde orijinal kaynağa çağrı yapar
print(user_client.get_user(2))
