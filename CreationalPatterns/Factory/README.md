- Factory Pattern:
Bir sınıfın nesne yaratma sorumluluğunu alt sınıflara devrettiği bir tasarım desenidir.
Bu desen, bir sınıfın, hangi alt sınıfın oluşturulacağını belirlemesine izin vermek için kullanılır.
Bu, nesne oluşturma sürecini daha esnek ve genişletilebilir hale getirir.

- Factory Method Kullanım Alanları
1. Çeşitli Nesne Türlerinin Yaratılması: Factory Method, farklı türde nesneler yaratmak için kullanılır.
Örneğin, bir veritabanı bağlantısı oluşturmak veya farklı dosya formatları işlemek.
2. Nesne Yaratma Mantığının Merkezi Yönetimi: Nesne yaratma mantığını bir yerde toplamak ve yönetmek için kullanılır.
3. Karmaşık Nesne Yaratma Süreci: Karmaşık nesne yaratma süreçlerini soyutlayarak kodu daha temiz ve bakımı kolay hale getirmek için kullanılır.

- Avantajları
1. Açık/Kapalı Prensibi: Yeni türde nesneler eklemek, mevcut kodu değiştirmek zorunda kalmadan mümkündür.
2. Tek Sorumluluk Prensibi: Nesne yaratma mantığı ve nesnenin nasıl kullanıldığının ayrı ayrı ele alınmasını sağlar.

- Dezavantajları
1. Kod Karmaşıklığı: Ek sınıflar ve yöntemler eklemek, kodun karmaşıklığını artırabilir.
2. Bakım Zorluğu: Özellikle çok sayıda ConcreteProduct ve ConcreteCreator olduğunda, bunların yönetimi zor olabilir.

- Abstract Factory
Birbiriyle ilişkili veya bağımlı nesnelerden oluşan ailelerin yaratılmasını sağlayan bir yaratıcı tasarım desenidir.
Bu desen, somut sınıflarını belirtmeden nesne aileleri oluşturmak için kullanılan bir arayüz sağlar.

- Abstract Factory Tasarım Deseni
- Temel Bileşenler
1. AbstractFactory: Bir ürün ailesi yaratmak için arayüzü tanımlar.
2. ConcreteFactory: AbstractFactory arayüzünü uygulayan somut sınıflar. Her somut fabrika, belirli bir ürün ailesinin tüm somut ürünlerini yaratır.
3. AbstractProduct: Bir ürün ailesindeki nesnelerin ortak arayüzünü tanımlar.
4. ConcreteProduct: AbstractProduct arayüzünü uygulayan somut ürün sınıfları.
5. Client: Yalnızca AbstractFactory ve AbstractProduct arayüzlerini kullanarak nesnelerle etkileşime giren istemci kodu.

- Abstract Factory Deseninin Faydaları
1. Bağımlılıkların Azaltılması: İstemci kod, doğrudan somut sınıflarla değil, soyut arayüzlerle çalıştığı için bağımlılıklar azalır.
2. Kolay Genişletilebilirlik: Yeni ürün aileleri eklemek, mevcut kodu değiştirmeden mümkündür. Yeni bir fabrika ve ürün sınıfları ekleyerek sistem genişletilebilir.
3. Tutarlılık: Bir fabrika, bir ürün ailesinin tüm bileşenlerini tutarlı bir şekilde yaratır, bu da uyumsuz bileşenlerin kullanılmasını önler.