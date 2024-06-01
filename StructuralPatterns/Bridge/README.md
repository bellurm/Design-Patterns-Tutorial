# Bridge #
Soyutlama ve implementasyon ayrı sınıflar hiyerarşilerinde yer alır ve birbirleriyle bir köprü (bridge) aracılığıyla bağlanırlar. Bu sayede, yeni soyutlamalar eklemek ya da mevcut implementasyonu değiştirmek, diğerine bağımlı olmadan gerçekleştirilebilir.

# Bridge Pattern'in Amaçları #
1. Bağımsız Değişiklik: Soyutlama ve implementasyonun bağımsız olarak değiştirilebilmesini sağlar.
2. Esneklik: Kodun daha esnek ve genişletilebilir olmasını sağlar.
3. Bakım Kolaylığı: Kodun bakımını ve yönetimini kolaylaştırır.

# Bridge Pattern'in Yapısı #
1. Abstraction (Soyutlama): Soyutlamayı temsil eden üst sınıf. Bu sınıf, bir Implementor (Gerçekleştirici) referansına sahiptir.
2. RefinedAbstraction (Gelişmiş Soyutlama): Abstraction sınıfının türetilmiş sınıfları. Bu sınıflar, Abstraction'dan miras alır ve ek işlevler sunar.
3. Implementor (Gerçekleştirici): Gerçekleştirici arayüzü veya soyut sınıfı. Bu arayüz, ConcreteImplementor sınıfları tarafından uygulanır.
4. ConcreteImplementor (Somut Gerçekleştirici): Implementor arayüzünü uygulayan somut sınıflar.

# Avantajları #
1. Soyutlama ve implementasyon arasındaki bağımlılığı azaltır.
2. Kodun esnekliğini ve genişletilebilirliğini artırır.
3. Bakım ve yönetim kolaylığı sağlar.

# Dezavantajları #
1. Daha karmaşık bir yapı oluşturabilir.
2. Ekstra soyutlama katmanları nedeniyle anlaşılırlığı zorlaştırabilir.

# Kullanım Durumları #
1. Bir sınıfın iki farklı boyutunu (örneğin, soyutlama ve implementasyon) bağımsız olarak genişletmek gerektiğinde.
2. Kodun esnekliğini artırmak ve değişiklikleri daha yönetilebilir hale getirmek istendiğinde.
3. Çapraz kesişen endişeleri olan sınıflar (örneğin, bir nesnenin hem şekli hem de rengi) için uygun bir yapı oluşturmak gerektiğinde.

