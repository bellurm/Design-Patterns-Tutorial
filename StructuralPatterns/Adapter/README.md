# Adapter Pattern #

Farklı arayüzlere sahip sınıfların birlikte çalışabilmesini sağlamak için kullanılır. Bu desen, mevcut bir sınıfın arayüzünü, istemci tarafından beklenen bir arayüze dönüştürerek çalışır.

# Adapter Pattern'in Amaçları #
1. Uyumluluk Sağlama: Farklı arayüzlere sahip sınıflar arasında uyumluluk sağlayarak, mevcut kodun değiştirilmeden kullanılabilmesini mümkün kılar.
2. Yeniden Kullanılabilirlik: Var olan kodun yeniden kullanılabilirliğini artırır. Yeni bir sınıf yazmak yerine adaptör kullanarak mevcut sınıflar kullanılabilir.
3. Esneklik ve Bakım Kolaylığı: Kodun daha esnek ve bakımı kolay hale gelmesini sağlar, çünkü adaptörler arayüz değişikliklerine karşı bir tampon görevi görür.

# Adapter Pattern Türleri #

1. Class Adapter (Sınıf Adaptörü): Kalıtım yoluyla adapte edilen sınıf. Bu tür adaptör, adaptör sınıfının hem hedef arayüzü hem de adapte edilen sınıfı miras aldığı durumlardır.
2. Object Adapter (Nesne Adaptörü): Kompozisyon yoluyla adapte edilen sınıf. Adaptör, hedef arayüzü uygular ve adapte edilen sınıfın bir örneğini içerir.

# Kullanım Durumları #
1. Var olan bir sınıfın arayüzünü istemciye uyarlamak gerektiğinde.
2. Mevcut bir sınıfın yeniden kullanılabilmesi için arayüzünün değiştirilmesi gerektiğinde.
3. Eski sistemlerin yeni sistemlerle entegre edilmesi gerektiğinde.

# Adapter Pattern'in Yapısı #
- Target (Hedef) Arayüz: İstemcinin kullanmak istediği arayüzdür.
- Adapter (Adaptör) Sınıfı: Target arayüzünü implemente eder ve adapte edilen sınıfa çağrılar yapar.
- Adaptee (Adapte Edilen) Sınıf: Adaptör tarafından uyumlu hale getirilen mevcut sınıftır.
- Client (İstemci): Target arayüzünü kullanarak işlemleri gerçekleştiren sınıftır.

# Avantajları #
1. Mevcut kodun yeniden kullanılmasını sağlar.
2. Kodun modülerliğini artırır.
3. Esneklik sağlar ve arayüz değişikliklerinden kaynaklanan sorunları azaltır.

# Dezavantajları #
1. Ekstra bir soyutlama katmanı ekler, bu da bazen gereksiz karmaşıklığa yol açabilir.
2. Performans üzerinde minimal de olsa bir etkisi olabilir.

# ÖRNEK 2 AÇIKLAMASI #
OldCreditCardPayment: Eski kredi kartı ödeme sistemini temsil eden sınıf.
PaymentProcessor: Yeni ödeme arayüzü.
PaymentAdapter: Eski kredi kartı ödeme sistemini yeni ödeme arayüzü ile uyumlu hale getiren adaptör sınıfı. Hem kredi kartı hem de PayPal ödemelerini işleyebilir.
PaymentClient: PaymentProcessor arayüzünü kullanan istemci sınıfı.

Adapte Edilen Sınıf (OldCreditCardPayment): Eski sistemden kalan ve sadece kredi kartı ödemelerini işleyebilen sınıf.
Hedef Arayüz (PaymentProcessor): Hem kredi kartı hem de PayPal ödemelerini işleyebilen yeni arayüz.
Adaptör Sınıfı (PaymentAdapter): OldCreditCardPayment sınıfını PaymentProcessor arayüzü ile uyumlu hale getirir. Kredi kartı ödemelerini OldCreditCardPayment sınıfı ile, PayPal ödemelerini ise kendi içinde basit bir metot ile işleyebilir.
İstemci Kodu (PaymentClient): PaymentProcessor arayüzünü kullanarak ödemeleri gerçekleştirir. PaymentAdapter'ı kullanarak hem kredi kartı hem de PayPal ödemelerini işleyebilir.

# Adapter No-Caching #
No-Caching Adapter, adaptörün herhangi bir önbellekleme (caching) yapmadığı, her çağrıda orijinal kaynağa erişim sağladığı bir adaptör türüdür. Bu tür adaptör, her istekte orijinal kaynağı çağırarak gerçek zamanlı ve taze veri sağlar. Ancak, performans açısından, sürekli olarak orijinal kaynağa erişim yapıldığında maliyetli olabilir.

# With-Caching Adapter #
With-Caching Adapter, adaptörün önbellekleme (caching) yaptığı, belirli süreler veya şartlar altında önbellekteki veriyi kullandığı bir adaptör türüdür. Bu tür adaptör, performansı artırmak ve aynı veriye tekrar tekrar erişimi azaltmak için kullanılır. Ancak, önbellekte tutulan veri zamanla eskiyebilir ve güncel olmayabilir.