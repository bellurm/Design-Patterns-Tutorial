# Decorator Pattern
Bu desen, bir nesneye dinamik olarak yeni davranışlar eklemenin bir yolunu sağlar. Temel olarak, nesnenin çekirdek fonksiyonelliğini değiştirmeden, ona ek sorumluluklar yüklemek için kullanılır.

# Bileşenşeri:
1. Component (Bileşen): Temel arayüz veya soyut sınıf. Hem temel sınıf hem de dekoratörler bu arayüzü veya sınıfı uygular.
2. ConcreteComponent (Somut Bileşen): Temel arayüzün somut bir implementasyonudur. Temel işlevselliği sağlar.
3. Decorator (Dekoratör): Bu sınıf, temel arayüzü uygular ve bir Component örneği içerir. Ek işlevselliği sağlamanın yanı sıra, bileşen arayüzünü korur.
4. ConcreteDecorator (Somut Dekoratör): Dekoratör sınıfını genişletir ve ek davranışlar ekler.

# Avantajlar
1. Esneklik:
Nesnenin işlevselliğini değiştirmek veya genişletmek için sınıf hiyerarşisini değiştirmeden yeni davranışlar ekleyebilirsiniz. Bu, tasarımda daha fazla esneklik sağlar.

2. Modülerlik:
Davranışları küçük ve bağımsız bileşenler halinde paketleyerek bu bileşenleri bir araya getirip farklı kombinasyonlar oluşturabilirsiniz. Bu, kodun yeniden kullanılabilirliğini ve bakımını kolaylaştırır.

3. Kod Tekrarını Azaltma:
Aynı veya benzer işlevselliği sağlayan kodları birden fazla sınıfta tekrar etmek yerine, dekoratörler kullanarak bu işlevselliği tek bir yerde tanımlayabilirsiniz. Bu, kodun daha temiz ve düzenli olmasını sağlar.

4. Dinamik Davranış Ekleyebilme:
Çalışma zamanı sırasında nesnelere yeni işlevsellik ekleyebilirsiniz. Bu, özellikle nesnelerin davranışlarının dinamik olarak değişmesi gerektiğinde yararlıdır.

5. Tek Sorumluluk İlkesi (Single Responsibility Principle):
Dekoratörler, bir sınıfın tek bir sorumluluğa sahip olmasını sağlar. Eklenen her yeni davranış, ayrı bir dekoratör sınıfı olarak eklenir, bu da sınıfların daha odaklı ve yönetilebilir olmasını sağlar.

6. Açık/Kapalı İlkesi (Open/Closed Principle):
Mevcut kodu değiştirmeden yeni işlevsellik eklemeyi mümkün kılar. Sınıflar, mevcut işlevsellikleri bozmadan genişletilebilir.

7. Bakım Kolaylığı:
İşlevselliği *bağımsız dekoratörler* halinde düzenlemek, bakımını ve test edilmesini kolaylaştırır. Her dekoratörün ayrı ayrı test edilebilir olması, hataların bulunmasını ve düzeltilmesini hızlandırır.

# Dezavantajlar
1. Kod Karmaşıklığı:
Dekoratörler, bir nesnenin işlevselliğini genişletmek için zincirleme bir yapı oluşturabilir. Bu, özellikle birçok dekoratör kullanıldığında kodun izlenmesini zorlaştırabilir. Her dekoratörün birbirine nasıl bağlı olduğunu anlamak karmaşık olabilir.

2. Debuggingle İlgili Zorluklar:
Dekoratörler zincirinin neresinde bir hata olduğunu bulmak zor olabilir. Her dekoratör, temel işlevselliği bir başka dekoratöre veya orijinal nesneye devrettiği için, hata ayıklama işlemi zorlaşabilir.

3. Bakım Zorlukları:
Birçok dekoratör kullanıldığında, bu dekoratörlerin bakımı ve yönetimi zorlaşabilir. Her dekoratörün ayrı ayrı test edilmesi ve güncellenmesi gerektiğinden, bakım maliyeti artabilir.

4. Performans Etkisi:
Her dekoratör, temel işlevselliği başka bir dekoratöre devrettiği için, dekoratör zinciri uzadıkça performans üzerinde olumsuz etkiler olabilir. Her bir arama ek bir fonksiyon çağrısı anlamına gelir ve bu da performans kaybına yol açabilir.

5. İhtiyaç Fazlası Kullanım:
Bazı durumlarda, Decorator Pattern yerine daha basit bir çözüm kullanılabilecekken, gereğinden fazla karmaşıklık katılabilir. Örneğin, basit bir genişletme işlemi için inheritance (kalıtım) veya strateji deseni daha uygun olabilir.

6. Objeler Arasındaki İlişkilerin Yönetimi:
Dekoratörler, temel nesneleri süslemek için birçok küçük nesne kullanır. Bu da nesneler arasındaki ilişkilerin yönetimini zorlaştırabilir. Özellikle nesneler arası bağımlılıkların artması, kodun anlaşılabilirliğini ve sürdürülebilirliğini olumsuz etkileyebilir.

# Classic Decorator
Classic Decorator, bir nesnenin işlevselliğini genişletmek veya değiştirmek için yeni nesneler yaratır.

# Özellikleri:
1. Statik ve Hiyerarşik:
Bir sınıf hiyerarşisi üzerinden işlevsellik ekler. Her dekoratör, belirli bir işlevselliği temsil eder ve diğer dekoratörlerle birleştirilebilir.

2. Sınıf Tabanlı:
Genellikle sınıf yapıları kullanılarak uygulanır. Bu sayede, nesnelerin davranışları sınıfın yapısı üzerinden değiştirilir.

3. Ekstra Sınıf Gereksinimi:
Her yeni işlevsellik için yeni bir dekoratör sınıfı oluşturulması gerekebilir. Bu da kodun karmaşıklığını artırabilir.

# Dynamic Decorator
Dynamic Decorator, fonksiyon tabanlı dekoratörlerdir ve Python'da @ işareti ile belirtilir. Bu dekoratörler, fonksiyonların ve metodların çalışma zamanında davranışlarını değiştirmek veya genişletmek için kullanılır.

# Özellikleri:
1. Dinamik ve Esnek:
Çalışma zamanı sırasında fonksiyonların veya metodların davranışlarını değiştirebilir. Daha esnek ve hafif bir yapı sağlar.

2. Fonksiyon Tabanlı:
Genellikle fonksiyonlar veya lambdalar kullanılarak uygulanır. @ işareti ile fonksiyonların veya metodların üzerine uygulanır.

3. Basit ve Hafif:
Ekstra sınıf oluşturma gerektirmez. Fonksiyonel programlama paradigmalarına daha yakın bir yaklaşım sağlar.

# Karşılaştırma ve Sonuç

- Classic Decorator:
Daha çok OOP tasarım desenlerinde kullanılır.
Sınıf tabanlıdır ve nesne hiyerarşisi ile çalışır.
Daha fazla kod karmaşıklığı yaratabilir.
Nesnelerin işlevselliğini genişletmek için uygundur.

- Dynamic Decorator:
Python'da @ işareti ile kullanılan fonksiyon tabanlı dekoratörlerdir.
Dinamik ve esnektir.
Ekstra sınıf gerektirmez, daha basit ve hafif bir yapıdadır.
Fonksiyonların ve metodların davranışlarını çalışma zamanında değiştirmek için uygundur.
