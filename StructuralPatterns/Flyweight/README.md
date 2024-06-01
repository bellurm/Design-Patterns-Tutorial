# Flyweight Pattern
- Yazılım geliştirme sürecinde bellek kullanımını optimize etmek ve nesne yaratma maliyetlerini azaltmak için kullanılan yapısal bir tasarım desenidir. Bu desen, çok sayıda küçük nesnenin bulunduğu sistemlerde bellek tasarrufu sağlamak amacıyla kullanılır.

# Temel Özellikler
1. Paylaşımlı Nesneler: Flyweight Pattern, çok sayıda nesnenin yaratılmasını ve saklanmasını gerektiren uygulamalarda bellek tasarrufu sağlar. Bu nesnelerin büyük çoğunluğu aynı veya benzer verilere sahip olabilir. Flyweight Pattern, bu ortak verileri paylaşarak bellek kullanımını azaltır.

2. İç ve Dış Durum: Flyweight nesneleri iki tür durumda saklanır; iç durum (intrinsic state) ve dış durum (extrinsic state). İç durum, nesnenin paylaşılan ve değişmez özelliklerini içerir ve nesne içinde saklanır. Dış durum ise nesnenin bağlamını ifade eder ve bu durum nesne dışında tutulur, böylece aynı nesne farklı bağlamlarda kullanılabilir.

3. Flyweight Factory: Flyweight Pattern, genellikle bir fabrika (factory) nesnesi ile birlikte kullanılır. Bu fabrika, mevcut Flyweight nesnelerini yönetir ve gerektiğinde yeni Flyweight nesneleri oluşturur. Eğer istenen Flyweight nesnesi zaten mevcutsa, fabrika bu nesneyi tekrar yaratmak yerine mevcut nesneyi döndürür.

# Yapısı
1. Flyweight Arayüzü (Flyweight Interface): Bu arayüz, Flyweight nesnelerinin ortak operasyonlarını tanımlar.
2. ConcreteFlyweight: Flyweight arayüzünü implemente eden ve iç durumu saklayan sınıftır.
3. UnsharedConcreteFlyweight: Flyweight arayüzünü implemente eden ancak paylaşılmayan nesnelerdir. Bazı durumlarda Flyweight nesnelerinin hepsi paylaşılabilir değildir.
4. FlyweightFactory: Flyweight nesnelerinin yaratılmasını ve yönetilmesini sağlar. Nesneler arasında paylaşımı organize eder.
5. Client: Flyweight nesnelerini kullanan sınıftır. Dış durumu yönetir ve Flyweight nesnelerine bu durumu geçirir.

# Kullanım Durumları
1. Büyük Miktarda Nesne Gereksinimi: Uygulamanız çok sayıda küçük nesne yaratmayı gerektiriyorsa ve bu nesnelerin büyük bir kısmı aynı veya benzer verilere sahipse, Flyweight Pattern bellek kullanımını azaltmak için ideal bir çözümdür.
2. Bellek Kısıtlamaları: Bellek kullanımı önemli bir kısıtlamaysa ve uygulamanızın performansını etkileyecek seviyede bellek kullanımı varsa, Flyweight Pattern bu durumu hafifletebilir.
3. Paylaşımlı Durum: Nesneler arasında paylaşılan durumlar varsa ve bu durumlar büyük miktarda veri içeriyorsa, Flyweight Pattern bu verileri paylaşarak bellek tasarrufu sağlar.

# Avantajları
1. Bellek Tasarrufu:
- Flyweight Pattern, büyük miktarda benzer nesne yaratılmasını ve saklanmasını gerektiren durumlarda bellek kullanımını optimize eder. Paylaşılan nesneler sayesinde aynı veriyi tekrar tekrar saklamak yerine tek bir kopya kullanılır.

2. Performans İyileştirmesi:
- Bellek tasarrufu, genellikle uygulamanın genel performansını da iyileştirir. Daha az bellek kullanımı, daha az çöp toplama işlemi ve daha hızlı bellek erişimi anlamına gelir.

3. Merkezi Yönetim:
- Flyweight nesneleri bir fabrika (factory) tarafından yönetildiği için, nesnelerin yaratılması ve paylaşılması merkezi bir şekilde kontrol edilir. Bu, nesne yaratma ve yönetme sürecini daha düzenli ve verimli hale getirir.

4. Tutarlılık:
- Paylaşılan nesneler sayesinde aynı veri birden fazla yerde tutarlı bir şekilde kullanılabilir. Bu, veri tutarlılığını ve bütünlüğünü artırır.

# Dezavantajları
1. Artan Kod Karmaşıklığı:
- Flyweight Pattern, uygulamaya eklenen yeni sınıflar ve katmanlar nedeniyle kodun karmaşıklığını artırabilir. Bu, bakım ve anlama sürecini zorlaştırabilir.

2. Dış Durumun Yönetimi:
- Flyweight nesneleri ile çalışırken dış durumun yönetimi zor olabilir. Dış durumun her kullanımda Flyweight nesnesine geçirilmesi gerekir, bu da ek kod gerektirebilir ve hata yapma olasılığını artırabilir.

3. Thread Safety (İş Parçacığı Güvenliği):
- Paylaşılan nesnelerin aynı anda birden fazla iş parçacığı tarafından kullanılma olasılığı olduğunda, thread safety (iş parçacığı güvenliği) ile ilgili sorunlar ortaya çıkabilir. Bu, özellikle çok iş parçacıklı ortamlarda dikkatli bir şekilde ele alınmalıdır.

4. Önbellek Yönetimi:
- Flyweight Pattern, bellek tasarrufu sağlarken, önbellekte tutulan nesnelerin yönetimi konusunda da ek bir sorumluluk getirir. Eğer çok sayıda farklı dış durum varsa, bu önbellek yönetimi karmaşık hale gelebilir ve performans sorunlarına yol açabilir.

