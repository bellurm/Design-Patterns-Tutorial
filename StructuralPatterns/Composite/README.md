# Composite Pattern
Nesneleri ağaç yapısında hiyerarşik bir şekilde düzenlememize olanak tanır. Bu desen, nesnelerin bir arada gruplandırılmasını ve bu grupların bireysel nesneler gibi işlenebilmesini sağlar. Composite Pattern'ın temel amacı, nesnelerin hiyerarşik olarak düzenlendiği bir yapıda, hem bileşik (composite) nesneleri hem de yaprak (leaf) nesneleri aynı şekilde ele alabilmektir. Bu, istemcinin bileşik ve yaprak nesneler arasında ayrım yapmasına gerek kalmadan tüm nesneleri tek tip bir arayüzle kullanabilmesini sağlar.

# Composite Pattern, özellikle şu durumlarda kullanışlıdır:
1. Ağaç yapılarının (örneğin, dosya sistemleri, grafik sahneleri, GUI bileşenleri) temsil edilmesi gerektiğinde.
2. İstemcilerin, bileşenler ve bileşik nesneler arasındaki farkı bilmeden nesnelerle etkileşime geçmesi gerektiğinde.
3. Hiyerarşik bir yapının farklı düzeylerinde aynı işlemlerin yapılması gerektiğinde.

# Composite Pattern Bileşenleri
1. Component (Bileşen)
- Tüm nesneler için ortak olan arayüzü tanımlar.
- Bileşik ve yaprak nesneler için aynı arayüzü sağlar.
- İsteğe bağlı olarak, bileşik nesnelerin alt bileşenleri yönetmesi için bazı varsayılan davranışlar içerebilir.

2. Leaf (Yaprak)
- Hiyerarşinin en alt düzeyindeki nesneleri temsil eder.
- Gerçek işlevselliği uygular, ancak alt bileşen içermez.

3. Composite (Bileşik)
- Alt bileşenler (yapraklar veya diğer bileşikler) içeren nesneleri temsil eder.
- Alt bileşenlerin eklenmesi, kaldırılması ve yönetilmesi için yöntemler içerir.
- Component arayüzünü uygular ve genellikle alt bileşenlere çağrıları delege eder.

4. Client (İstemci)
- Bileşenler ve bileşik nesnelerle etkileşime girer.
- Component arayüzü üzerinden tüm nesneleri işler.

# Avantajları
1. Esneklik: İstemci kodu, bileşik ve yaprak nesneler arasında ayrım yapmadan, tüm nesnelerle aynı arayüz üzerinden etkileşime geçebilir.
2. Yeniden Kullanılabilirlik: Aynı bileşenler, farklı bileşik yapılar içinde yeniden kullanılabilir.
3. Kolay Bakım: Hiyerarşik yapıların yönetimi ve genişletilmesi daha kolaydır.

# Dezavantajları
1. Karmaşıklık: Basit yapıların gereksiz yere karmaşık hale gelmesine neden olabilir.
2. Performans: Büyük ve derin hiyerarşik yapılarda performans sorunlarına yol açabilir.
