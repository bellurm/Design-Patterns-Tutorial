# Dependency Inversion Principle (DIP), yazılım tasarımında sıkça kullanılan bir prensiptir ve SOLID prensiplerinden biridir.
# Bu prensip, yazılım bileşenlerinin birbirlerine olan bağımlılıklarını zayıf tutmayı ve daha esnek, yeniden kullanılabilir kodlar oluşturmayı amaçlar.

# Dependency Inversion Principle'ın temel fikirleri şunlardır:

# Üst seviye modüller, alt seviye modüller üzerine bağımlı olmamalıdır. Her iki seviyede de soyutlamalar olmalıdır.

# Soyutlamalar, detaylara bağımlı olmamalıdır. Detaylar, soyutlamalara bağımlı olmalıdır.

# Bu prensibe göre, yazılım bileşenleri arasındaki bağımlılıklar, yüksek seviyeli bileşenlerin düşük seviyeli bileşenlere doğrudan bağımlı olmaması ve
# her iki seviyede de soyutlamaların (interface veya abstract class) kullanılması gerektiğini belirtir.
# Böylece, bileşenler arasındaki bağımlılıklar, soyutlamalara yönlendirilir ve bu da kodun daha esnek, bakımı kolay ve yeniden kullanılabilir olmasını sağlar.

# DIP'nin temel avantajları şunlardır:

# Esneklik: Soyutlamalar aracılığıyla yapılan bağımlılıklar, kodun daha esnek olmasını sağlar. Bu sayede, değişikliklere daha kolay adapte olunabilir.

# Yeniden Kullanılabilirlik: DIP, bileşenler arasındaki sıkı bağımlılıkları azaltarak, kodun yeniden kullanılabilirliğini artırır.
# Bileşenlerin daha az bağımlı olması, onların daha farklı bağlamlarda tekrar kullanılabilmesini sağlar.

# Test Edilebilirlik: DIP, yazılım bileşenlerinin test edilebilirliğini artırır.
# Çünkü soyutlamalar aracılığıyla yapılan bağımlılıklar, bileşenlerin bağımlılıklarını sahte (mock) nesnelerle kolayca değiştirmeyi mümkün kılar.

# Özetle, Dependency Inversion Principle, yazılım bileşenleri arasındaki bağımlılıkları zayıf tutarak daha esnek, bakımı kolay ve yeniden kullanılabilir kodlar oluşturmayı hedefler.

from abc import ABC, abstractmethod

class BildirimServisi(ABC):
    @abstractmethod
    def bildirim_gonder(self, iletisim_bilgisi, icerik):
        pass

class EpostaServisi(BildirimServisi):
    def bildirim_gonder(self, iletisim_bilgisi, icerik):
        # E-posta gönderme kodu
        print(f"E-posta gönderildi: {iletisim_bilgisi}, İçerik: {icerik}")

class SMSServisi(BildirimServisi):
    def bildirim_gonder(self, iletisim_bilgisi, icerik):
        # SMS gönderme kodu
        print(f"SMS gönderildi: {iletisim_bilgisi}, İçerik: {icerik}")

class BildirimUygulamasi:
    def __init__(self, bildirim_servisi):
        self.bildirim_servisi = bildirim_servisi

    def bildirim_gonder(self, iletisim_bilgisi, icerik):
        self.bildirim_servisi.bildirim_gonder(iletisim_bilgisi, icerik)

eposta_servisi = EpostaServisi()
sms_servisi = SMSServisi()

bildirim_uygulamasi_eposta = BildirimUygulamasi(eposta_servisi)
bildirim_uygulamasi_eposta.bildirim_gonder("ornek@example.com", "Merhaba, bu bir bildirim e-postası!")

bildirim_uygulamasi_sms = BildirimUygulamasi(sms_servisi)
bildirim_uygulamasi_sms.bildirim_gonder("5551234567", "Merhaba, bu bir SMS bildirimi!")

############################################################################################################################################################################################################
############################################################################################################################################################################################################
############################################################################################################################################################################################################
############################################################################################################################################################################################################
############################################################################################################################################################################################################
############################################################################################################################################################################################################
############################################################################################################################################################################################################
############################################################################################################################################################################################################
############################################################################################################################################################################################################
############################################################################################################################################################################################################
############################################################################################################################################################################################################

from abc import ABC, abstractmethod

class SiparisAlmaServisi(ABC):
    @abstractmethod
    def siparis_al(self, siparis):
        pass

class OdemeAlmaServisi(ABC):
    @abstractmethod
    def odeme_al(self, miktar):
        pass

class WebSiparisAlmaServisi(SiparisAlmaServisi):
    def siparis_al(self, siparis):
        # Web sipariş alma kodu
        pass

class TelefonSiparisAlmaServisi(SiparisAlmaServisi):
    def siparis_al(self, siparis):
        # Telefonla sipariş alma kodu
        pass

class KrediKartiOdemeServisi(OdemeAlmaServisi):
    def odeme_al(self, miktar):
        # Kredi kartı ödeme kodu
        pass

class BankaHavalesiOdemeServisi(OdemeAlmaServisi):
    def odeme_al(self, miktar):
        # Banka havalesi ödeme kodu
        pass

class Siparis:
    def __init__(self, urun, adet):
        self.urun = urun
        self.adet = adet

class SiparisUygulamasi:
    def __init__(self, siparis_alma_servisi, odeme_alma_servisi):
        self.siparis_alma_servisi = siparis_alma_servisi
        self.odeme_alma_servisi = odeme_alma_servisi

    def siparis_al(self, siparis):
        self.siparis_alma_servisi.siparis_al(siparis)

    def odeme_al(self, miktar):
        self.odeme_alma_servisi.odeme_al(miktar)

class OdemeAlmaServisi(ABC):
    @abstractmethod
    def odeme_al(self, miktar):
        pass

class KrediKartiOdemeServisi(OdemeAlmaServisi):
    def odeme_al(self, miktar):
        print(f"{miktar} TL kredi kartı ile ödendi.")

siparis = Siparis("Ürün", 3)
miktar = 150

kredi_karti_odeme_servisi = KrediKartiOdemeServisi()
siparis_uygulamasi = SiparisUygulamasi(None, kredi_karti_odeme_servisi)
siparis_uygulamasi.odeme_al(miktar)

############################################################################################################################################################################################################
############################################################################################################################################################################################################
############################################################################################################################################################################################################
############################################################################################################################################################################################################
############################################################################################################################################################################################################
############################################################################################################################################################################################################
############################################################################################################################################################################################################
############################################################################################################################################################################################################
############################################################################################################################################################################################################
############################################################################################################################################################################################################
############################################################################################################################################################################################################

from abc import ABC, abstractmethod
from enum import Enum


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name):
        self.name = name


class RelationshipBrowser(ABC):
    @abstractmethod
    def find_all_children_of(self, name):
        pass


class Relationships(RelationshipBrowser):  
    relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.PARENT, parent))

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name


class Research:
    def __init__(self, browser: RelationshipBrowser):
        self.browser = browser

    def find_children_of(self, name):
        for p in self.browser.find_all_children_of(name):
            print(f'{name} has a child called {p}')


parent = Person('John')
child1 = Person('Chris')
child2 = Person('Matt')

relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

research = Research(relationships)
research.find_children_of('John')
