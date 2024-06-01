# Chain of Responsibility
- Bu desen, bir isteğin bir zincir boyunca iletilmesini sağlar ve bu zincirin her halkası (obje) isteği işleyebilir veya bir sonraki halkaya iletebilir. Bu yaklaşım, istemcinin (client) hangi nesnenin isteği işleyeceğini bilmesi gerekmeksizin isteklerin işlenmesini sağlar. 

# Temel Kavramlar ve Bileşenler
1. Handler (İşleyici):
    - İşlemi gerçekleştiren temel arabirim veya soyut sınıf.
    - İsteği işleyebilme yeteneğine sahip olmalıdır.
    - Sonraki işleyiciye isteği iletebilmek için bir referans içermelidir.

2. ConcreteHandler (Somut İşleyici):
    - Handler sınıfından türeyen ve belirli bir isteği işleyebilen somut sınıf veya sınıflar.
    - İsteği işleyemezse, bu sorumluluğu zincirdeki bir sonraki işleyiciye devreder.

3. Client (İstemci):
    - İsteği zincirin başına gönderir.
    - Hangi işleyicinin isteği işleyeceği hakkında bilgi sahibi değildir.

# Yararları
1. Sorumluluğun Dağıtılması: İşlemin sorumluluğu birden fazla işleyici arasında paylaştırılabilir.
2. Gevşek Bağlılık (Loose Coupling): İstemcinin hangi nesnenin isteği işleyeceğini bilmesi gerekmez, böylece istemci ile işleyiciler arasında gevşek bir bağ kurulur.
3. Esneklik ve Genişletilebilirlik: Yeni işleyiciler eklemek veya mevcut işleyicileri değiştirmek kolaydır, bu da sistemin bakımını ve genişletilmesini kolaylaştırır.

# Zararları
- Performans: İsteğin zincirdeki tüm işleyicilerden geçmesi gerekebilir, bu da performans sorunlarına yol açabilir.
- Zincirin Sonu: Eğer zincirdeki hiçbir işleyici isteği işleyemezse, bu durumda özel bir durum veya hata yönetimi gerektirebilir.

# Chain of Responsibility Türleri
1. Method Chain
    - Bir nesneye peş peşe birden fazla metot çağrısı yapma tekniğidir. Her metot çağrısı nesnenin kendisini (yani `self`) döndürür, böylece bir sonraki metot çağrısı hemen ardından yapılabilir. Bu, daha okunabilir ve daha az kod yazmaya olanak tanır.

    # Yararları:
        - Okunabilirlik: Kodun okunabilirliğini artırır ve daha az satırda daha çok iş yapılmasını sağlar.
        - Akış Kontrolü: Akış kontrolü sağlar ve işlemlerin sıralı bir şekilde yapılmasına olanak tanır.
        - Daha Temiz Kod: Daha temiz ve anlaşılır bir kod yazımı sağlar.
        
    # Zararları:
        - Hata Ayıklama: Zincirleme metodlarda hata ayıklama zor olabilir, çünkü hatanın hangi metodda meydana geldiğini tespit etmek zorlaşabilir.
        - Bağımlılık: Metodlar arasındaki sıkı bağımlılık, metotların bağımsız olarak test edilmesini zorlaştırabilir.
        - Uzun Zincirler: Çok uzun zincirler okunabilirliği azaltabilir ve bakımı zorlaştırabilir.

2. Command Query Separation (CQS)
    - Bu prensip, bir metot ya bir komut (değişiklik yapar) ya da bir sorgu (değer döner) olmalıdır, ancak ikisi birden olmamalıdır. Yani, bir metot ya bir şey yapmalı ya da bir şey söylemelidir, fakat her ikisini birden yapmamalıdır.

    # Yararları:
        - Temiz ve Anlaşılır Tasarım: Komutlar ve sorguların ayrılması, kodun daha anlaşılır ve bakımı kolay olmasını sağlar.
        - Kolay Test Edilebilirlik: Komutlar ve sorgular ayrı ayrı test edilebilir, bu da test sürecini kolaylaştırır.
        - Güvenlik ve Kararlılık: Sorguların sistemi değiştirmemesi, sistemin kararlılığını ve güvenliğini artırır.
    # Zararları:
        - Çok Sayıda Metot: Komutlar ve sorguların ayrılması, sınıfların çok sayıda metot içermesine neden olabilir.
        - Ekstra Kod: CQS prensibini uygulamak, daha fazla kod yazılmasını gerektirebilir.
        - Tasarımsal Karmaşıklık: İlk başta tasarımı anlamak ve uygulamak karmaşık gelebilir.

3. Broker Chain
    - Genellikle bir mesaj veya isteğin birden fazla alıcıya iletilmesini sağlamak için kullanılır. Bu desen, isteklerin bir dizi aracıyı (broker) geçerek uygun işleyiciye ulaşmasını sağlar. Her aracı, isteği işleyebilir veya bir sonraki aracıya iletebilir.

    # Yararları:
        - Esneklik: Mesajların veya isteklerin dinamik olarak işlenmesi esneklik sağlar.
        - Gevşek Bağlılık: İşleyiciler arasındaki gevşek bağlılık, sistemin daha modüler olmasını sağlar.
        - Kolay Genişletilebilirlik: Yeni işleyiciler eklemek veya mevcut işleyicileri değiştirmek kolaydır.
    # Zararları:
        - Performans: Mesajların veya isteklerin zincirdeki tüm işleyicilerden geçmesi performans sorunlarına yol açabilir.
        - Hata Yönetimi: Zincirin sonuna ulaşan ve işlenmeyen istekler için özel hata yönetimi gerekebilir.
        - Karmaşıklık: Zincirlerin yönetimi ve işleyicilerin sırası karmaşık hale gelebilir.

