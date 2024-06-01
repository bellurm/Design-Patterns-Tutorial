from abc import ABC, abstractmethod

class NotificationService(ABC):
    @abstractmethod
    def send_notification(self, message):
        pass

class EmailNotificationService(NotificationService):
    def send_notification(self, message):
        print(f"Sending email notification: {message}")

class SMSNotificationService(NotificationService):
    def send_notification(self, message):
        print(f"Sending SMS notification: {message}")

class PromotionService:
    def __init__(self, notification_service: NotificationService):
        self.notification_service = notification_service

    def send_promotional_message(self, message):
        self.notification_service.send_notification(message)

# Müşteriye bir bildirim gönderilceği zaman her işi NotificationService sınıfı yapıyor olsaydı bu, DIP yaklaşımına uygun bir kod olmazdı.
# Hep yaptığımız gibi ortak özellikleri NotificationService sınıfında topladık, bildirim gönderme çeşitlerini birer sınıf olarak atadık ve
# PromotionService sınıfının her şeye yetişmesini sağladık.

