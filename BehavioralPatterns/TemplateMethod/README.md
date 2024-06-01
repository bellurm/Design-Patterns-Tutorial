# Template Method Pattern
- Bu desen, bir algoritmanın iskeletini tanımlar ve bazı adımlarını alt sınıfların belirlemesine olanak tanır. Template Method, algoritmanın yapısını korurken, alt sınıfların belirli adımları değiştirmesine veya genişletmesine izin verir.

# Temel Özellikler ve Amaç
1. Kod Tekrarını Azaltma: Ortak algoritma adımları üst sınıfta tanımlanır, böylece alt sınıflar yalnızca özelleştirilmesi gereken kısımları sağlar.
2. Kontrolü Sağlama: Algoritmanın ana yapısını kontrol ederken, özelleştirme noktalarını alt sınıflara bırakır.
3. İskelet Yöntemi: Algoritmanın iskeleti bir şablon (template) yöntem olarak üst sınıfta tanımlanır ve alt sınıflar bu şablonun belirli kısımlarını değiştirir veya uygular.

# Yapısal Bileşenler
1. Abstract Class (Soyut Sınıf): Template Method'u tanımlar ve algoritmanın bazı adımlarını soyut metotlar olarak belirtir.
2. Concrete Class (Somut Sınıf): Soyut sınıfı genişletir ve gerekli adımları uygular.

# Avantajlar
1. Kod Tekrarının Azaltılması: Ortak algoritma adımları bir kez tanımlanır ve tekrar kullanılabilir. Bu, kod tekrarını azaltır.

2. Kontrol ve Esneklik: Algoritmanın ana yapısı korunurken, özelleştirme noktaları alt sınıflara bırakılır. Bu, esneklik sağlar ve alt sınıfların belirli adımları değiştirmesine olanak tanır.

3. Kolay Bakım: Algoritmanın iskeleti tek bir yerde tanımlandığı için, değişiklikler merkezi olarak yönetilebilir ve bakım kolaylığı sağlar.

# Dezavantajlar
1. Alt Sınıfların Artması: Çok sayıda alt sınıf, sınıf sayısının artmasına ve kod tabanının karmaşıklaşmasına neden olabilir.

2. Özelleştirme Zorunluluğu: Her somut sınıfın, soyut sınıfın tüm soyut metotlarını uygulaması gereklidir. Bu, bazı durumlarda gereksiz metodların implementasyonuna neden olabilir.
