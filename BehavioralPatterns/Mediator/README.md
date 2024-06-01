# Mediator Pattern
- Bir nesneler grubunun doğrudan birbirleriyle iletişim kurmak yerine, aralarındaki etkileşimi bir arabulucu (mediator) nesnesi aracılığıyla gerçekleştirmesini sağlayan bir davranışsal tasarım desenidir. Bu desen, nesneler arasındaki karmaşık bağımlılıkları azaltır ve sistemin daha esnek ve yönetilebilir olmasını sağlar.

# Mediator Pattern Neden Kullanılır?
1. Bağımlılıkların Azaltılması: Nesneler arasındaki doğrudan iletişimi azaltarak bağımlılıkları en aza indirir.

2. Karmaşıklığın Yönetimi: Karmaşık nesne etkileşimlerini merkezi bir noktada toplayarak yönetmeyi kolaylaştırır.

3. Kodun Yeniden Kullanılabilirliği: Nesneler arasındaki etkileşimlerin arabulucuya taşınması, bu nesnelerin bağımsız olarak yeniden kullanılabilmesini sağlar.

4. Kolay Bakım: Etkileşim mantığı merkezi bir yerde toplandığı için, değişiklikler kolayca uygulanabilir ve yönetilebilir.

# Temel Bileşenler
1. Mediator (Arabulucu): Nesneler arasındaki iletişimi tanımlar ve yönetir. Genellikle bir arayüz veya soyut sınıf olarak tanımlanır.

2. Concrete Mediator (Somut Arabulucu): Mediator arayüzünü uygular ve nesneler arasındaki belirli iletişim mantığını içerir.

3. Colleague (Meslektaş): Arabulucu aracılığıyla iletişim kuran nesneler. Bu nesneler doğrudan birbirleriyle değil, arabulucu ile iletişim kurar.

# Avantajları
1. Bağımlılıkların Azaltılması: Nesneler arasındaki doğrudan bağımlılıkları azaltır ve sistemin esnekliğini artırır.

2. Kolay Bakım ve Genişletme: Etkileşim mantığı merkezi bir arabulucu tarafından yönetildiği için, değişiklikler ve genişletmeler daha kolay uygulanabilir.

3. Daha Temiz ve Anlaşılır Kod: Karmaşık nesne etkileşimlerini merkezi bir noktada toplayarak kodun daha temiz ve anlaşılır olmasını sağlar.

# Dezavantajları
1. Arabulucunun Karmaşıklığı: Arabulucu, çok fazla iş yükü ve mantık içerdiğinde karmaşık hale gelebilir ve bu da bakımı zorlaştırabilir.

2. Tek Bir Başarısızlık Noktası: Tüm iletişim arabulucu üzerinden gerçekleştiği için, arabulucunun başarısız olması durumunda tüm sistem etkilenebilir.

# Mediator with Events
- Mediator Pattern'ın bir genişlemesidir ve genellikle olay tabanlı programlama ile birlikte kullanılır. Bu yaklaşımda, mediator, nesneler arasındaki iletişimi yönetir ve olaylar (events) kullanarak bu iletişimi daha esnek ve genişletilebilir hale getirir. Bu, özellikle GUI uygulamaları, oyunlar ve karmaşık iş mantıklarının olduğu uygulamalar için faydalıdır.
- Bu desen, nesneler arasında doğrudan bağımlılıkları azaltarak, bir olay aracısı (event mediator) üzerinden iletişim kurmalarını sağlar. Nesneler, belirli olayları yayımlar (publish) ve bu olaylara abone olan (subscribe) diğer nesneler, bu olaylar gerçekleştiğinde tepki verir.

# Temel Bileşenler
1. Mediator (Arabulucu): Olayları yönetir ve nesneler arasındaki iletişimi sağlar.

2. Events (Olaylar): Belirli bir eylemi veya durumu temsil eden tetiklenebilir olaylar.

3. Colleagues (Meslektaşlar): Olayları yayımlayan veya bu olaylara abone olan nesneler.

# Avantajları
1. Gevşek Bağlılık: Nesneler arasında gevşek bağlılık sağlar, böylece bir nesne diğerlerinin varlığından haberdar olmaz.

2. Esneklik ve Genişletilebilirlik: Olay tabanlı yapı, sistemin esnek ve genişletilebilir olmasını sağlar.

3. Merkezi Yönetim: Olayların merkezi bir noktada yönetilmesi, sistemin daha düzenli ve yönetilebilir olmasını sağlar.

# Dezavantajları
1. Karmaşıklık: Olayların izlenmesi ve yönetimi zor olabilir.
2. Performans: Çok sayıda olay ve abone varsa performans sorunları olabilir.
