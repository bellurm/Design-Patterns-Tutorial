# Proxy Pattern
- Bir nesnenin temsilcisi olarak başka bir nesneyi kullanır ve bu şekilde orijinal nesneye erişimi kontrol eder. Proxy Pattern'in temel amacı, nesneler arasındaki bağımlılıkları yönetmek ve belirli durumlarda ek sorumluluklar üstlenmek için bir aracı sağlamaktır.

# Türleri
1. Virtual Proxy (Sanal Proxy): Gerçek nesnenin oluşturulması pahalı olduğu durumlarda kullanılır. Sanal proxy, gerçek nesneye yalnızca ihtiyaç duyulduğunda erişim sağlar.
- Örnek: Büyük bir veri kümesini temsil eden bir nesne, yalnızca veri gerçekten gerekli olduğunda yüklenir.

2. Remote Proxy (Uzaktan Proxy): Bir nesnenin başka bir adreste (örneğin bir ağ üzerinde) bulunması durumunda kullanılır. Uzaktan proxy, yerel bir nesne gibi davranarak uzaktaki nesneye erişimi sağlar.
- Örnek: Dağıtık sistemlerdeki nesnelere erişim sağlama.

3. Protection Proxy (Koruma Proxy): Bir nesneye erişimi kontrol etmek ve belirli erişim politikalarını uygulamak için kullanılır. Bu, yetkisiz erişimleri engellemek için kullanılabilir.
- Örnek: Bir kullanıcı nesnesine yalnızca belirli rollerin erişmesine izin verme.

4. Caching Proxy (Önbellek Proxy): Sık erişilen verileri geçici olarak saklamak için kullanılır. Bu, özellikle pahalı kaynaklara yapılan tekrar eden erişimleri azaltmak için faydalıdır.
- Örnek: Veritabanı sorgularının sonuçlarını önbellekte tutma.

5. Logging Proxy (Kayıt Proxy): Bir nesneye yapılan çağrıları kaydetmek ve izlemek için kullanılır. Bu, hata ayıklama ve denetim için yararlıdır.
- Örnek: Bir nesneye yapılan tüm işlemleri log dosyasına yazma.

# Yapısı
Proxy Pattern, temel olarak dört ana bileşenden oluşur:
1. Subject (Konu): Gerçek nesneyi temsil eden arabirim veya soyut sınıf.
2. RealSubject (Gerçek Konu): Subject arabirimini uygulayan gerçek nesne.
3. Proxy: Subject arabirimini uygulayan ve RealSubject nesnesine erişimi kontrol eden temsilci nesne.
4. Client (İstemci): Subject arabirimi üzerinden Proxy veya RealSubject nesnesi ile etkileşime giren sınıf.

# Avantajları
1. Kontrollü Erişim: Proxy, gerçek nesneye erişimi kontrol ederek belirli kurallar ve politikalar uygulamayı sağlar.
2. Performans İyileştirmesi: Özellikle sanal proxy ve önbellek proxy kullanımı, performans iyileştirmelerine yardımcı olabilir.
3. Ek Sorumluluklar: Proxy, gerçek nesneye yapılan çağrılar üzerine ek sorumluluklar eklemeyi sağlar (örneğin, kayıt tutma, erişim kontrolü).

# Dezavantajları
1. Ek Maliyet: Proxy nesnesi oluşturmak ve yönetmek ek maliyet ve karmaşıklık getirebilir.
2. Şeffaflık Kaybı: İstemci bazen proxy ile gerçek nesne arasındaki farkı bilmeyebilir ve bu da karmaşıklığa yol açabilir.

