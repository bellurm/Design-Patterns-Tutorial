# Command Pattern
- Yazılım geliştirmede sıkça kullanılan davranışsal tasarım desenlerinden biridir. Bu desen, bir işlemi veya isteği nesne olarak kapsüller ve bu sayede işlemleri parametre olarak iletebilir, istekleri kuyruklayabilir, günlüğe kaydedebilir ve geri alabilirsiniz.

# Amacı
- Command Pattern'ın temel amacı, bir işlemi veya isteği nesne olarak kapsüllemektir. Bu desen şu durumlarda kullanışlıdır:
    - İşlemleri parametre olarak geçmek: İşlemleri fonksiyonel bir arayüz veya lambda ifadesi yerine nesne olarak temsil etmek.
    - İstekleri sıraya koymak: İşlemleri kuyruklayıp daha sonra çalıştırmak.
    - Geri alma operasyonları: İşlemleri geri alabilir veya tekrar edebilir şekilde yapılandırmak.
    - Günlüğe kaydetme: İşlemleri kaydedip gerektiğinde tekrar oynatmak.

# Yapısal Elemanlar
1. Command: İstekleri kapsülleyen soyut arayüz veya soyut sınıf.
2. ConcreteCommand: Command arayüzünü/sınıfını implemente eden somut sınıflar. Gerçek işlemi gerçekleştirir.
3. Invoker: İsteği gerçekleştiren sınıf. Command nesnesini çağırır.
4. Receiver: İsteği gerçekleştiren sınıf. ConcreteCommand tarafından kullanılır.

# Avantajlar
1. Modülerlik ve Ayrışma:
- İşlem mantığını (komut) işlemi gerçekleştiren bileşenden (alıcıdan) ayırarak modüler bir yapı sağlar. Bu ayrışma, kodun okunabilirliğini ve bakımını kolaylaştırır.
İşlem mantığının ve alıcı nesnelerin birbirinden bağımsız olarak değiştirilebilmesi, kodun esnekliğini artırır.

2. Geri Alma (Undo) ve Yeniden Yapma (Redo) Desteği:
- İşlemleri kapsülleyerek her işlemi geri almayı veya yeniden yapmayı kolaylaştırır. Her komut nesnesi, işlemi geri almak için gereken bilgileri içerebilir.
Bu özellik, özellikle kullanıcı arayüzlerinde veya karmaşık işlem dizilerinde kullanışlıdır.

3. İşlem Kuyruklama ve Planlama:
- Komut nesneleri sıraya konulabilir ve belirli bir sırayla veya belirli bir zamanda çalıştırılabilir. Bu, işlemlerin zamanlamasını ve sıralamasını yönetmeyi kolaylaştırır.
Kuyruklama, özellikle asenkron işlemler veya belirli bir sırada çalıştırılması gereken görevler için faydalıdır.

4. İşlem Günlüğü (Logging):
- Komutlar günlüğe kaydedilebilir, böylece gerçekleştirilen işlemler izlenebilir ve gerektiğinde tekrar oynatılabilir. Bu özellik, hata ayıklama ve sistem izleme için yararlıdır.
Günlüğe kaydedilen komutlar, sistemin geçmiş durumlarının yeniden oluşturulmasına olanak tanır.

5. Esnek Komut Yapısı:
- Komut nesneleri, dinamik olarak oluşturulabilir ve farklı işlem türlerini desteklemek için kolayca genişletilebilir. Bu esneklik, yeni işlemlerin eklenmesini veya mevcut işlemlerin değiştirilmesini kolaylaştırır. Bu esneklik, aynı invoker'ın farklı komutları çağırabilmesini sağlar, böylece kodun yeniden kullanılabilirliği artar.

6. Yüksek Bakım Kolaylığı:
- Komutlar bağımsız sınıflar olarak tanımlandığından, her komutun ayrı ayrı test edilmesi ve bakımı yapılabilir. Bu, özellikle büyük ve karmaşık projelerde hata ayıklamayı ve yeni özellikler eklemeyi kolaylaştırır. Komut deseninin kullanımı, tek sorumluluk ilkesi (Single Responsibility Principle) ve açık/kapalı ilke (Open/Closed Principle) gibi SOLID prensiplerine uygunluğu artırır.

7. Karmaşıklığın Yönetimi:
- Karmaşık işlemler veya iş mantığı, basit ve yönetilebilir komut nesnelerine bölünebilir. Bu, kodun anlaşılmasını ve yönetilmesini kolaylaştırır. Komutlar, çeşitli işlem türlerini (örneğin, veritabanı işlemleri, ağ istekleri, kullanıcı eylemleri) tutarlı bir şekilde ele almayı sağlar.

# Örnek Senaryolar
- Kullanıcı Arayüzleri:
    - Bir kelime işlemci uygulamasında "geri al" ve "yeniden yap" işlevleri için Command Pattern kullanılır. Her komut (örneğin, "yazı yaz", "sil") geri alınabilir şekilde tasarlanır.

- Makro Komutlar:
    - Bir dizi işlemi bir araya getirerek tek bir komut olarak çalıştırmak için Command Pattern kullanılabilir. Örneğin, bir grafik düzenleme yazılımında, bir dizi düzenleme işlemi tek bir makro komut altında toplanabilir.

- İşlem Kuyruklama:
    - Asenkron işlem yönetimi ve görev kuyruklama sistemlerinde, işlemler komut nesneleri olarak sıraya alınır ve belirli bir sırada veya belirli koşullarda çalıştırılır.

- Oyun Geliştirme:
    - Bir oyun motorunda, oyuncu hareketleri veya oyun içi eylemler komut nesneleri olarak temsil edilir. Bu sayede, oyuncu hareketleri geri alınabilir ve tekrar edilebilir.

# Dezavantajlar
1. Artan Sınıf ve Nesne Sayısı:
    - Her işlem için ayrı bir Command sınıfı oluşturulmasını gerektirir. Bu, özellikle çok sayıda işlem olduğunda, sınıf sayısında ve nesne sayısında büyük bir artışa neden olabilir.
Bu artış, kod tabanını karmaşıklaştırabilir ve yönetimini zorlaştırabilir.

2. Karmaşıklık:
    - Küçük ve basit projeler için gereksiz derecede karmaşık olabilir. Basit işlemler için bu desenin kullanımı, kodun anlaşılmasını zorlaştırabilir ve gereksiz yük oluşturabilir.
Özellikle geri alma (undo) gibi gelişmiş özelliklerin eklenmesi, desenin uygulanmasını daha da karmaşık hale getirebilir.

3. Bellek ve Performans:
    - Her işlem için yeni nesneler oluşturmak, bellek kullanımını artırabilir ve performansı olumsuz etkileyebilir. Özellikle yüksek frekansta işlem gerektiren uygulamalarda, bu durum önemli bir sorun olabilir. Gereksiz nesne oluşturma ve yönetimi, bellek yönetimi ve çöp toplayıcı üzerinde ek yük oluşturabilir.

4. Bakım Zorluğu:
    - Command Pattern ile yazılmış bir kod tabanında, yeni bir işlem eklemek veya mevcut bir işlemi değiştirmek, ilgili Command sınıfının da değiştirilmesini veya yeniden yazılmasını gerektirebilir. Çok sayıda Command sınıfı olduğunda, bu sınıfların bakımı zorlaşabilir ve bu da hata yapma olasılığını artırabilir.

5. Bağımlılıklar:
    - Command Pattern, Invoker, Command ve Receiver arasında sıkı bir bağımlılık oluşturur. Bu, modülerlik sağlasa da, aynı zamanda bu bileşenler arasında güçlü bir bağ oluşturarak esnekliği azaltabilir. Bağımlılıkların iyi yönetilmemesi durumunda, bu desen istenilen esnekliği sağlayamayabilir.

# Composite Command
- Composite Command, Command Pattern'ın bir genişletmesidir ve bir dizi komutun bir araya getirilerek tek bir komut gibi çalıştırılmasını sağlar. Bu yaklaşım, karmaşık işlemleri basit ve yönetilebilir bileşenlere ayırarak aynı anda birden çok komutu çalıştırmayı kolaylaştırır.

# Temel Amacı
- Composite Command, tek bir komut gibi davranan ve içinde birden fazla komut barındıran bir yapıdır. Bu, özellikle aşağıdaki durumlarda kullanışlıdır:

1. Birden Çok Komutu Tek Bir Komut Olarak Yönetme: Bir dizi işlemi tek bir işlem gibi ele almak.

2. Komutların Gruplanması: Bir grup komutu bir arada çalıştırmak veya geri almak.

3. İşlemleri Sıralı veya Paralel Olarak Çalıştırma: Birden çok komutu belirli bir sırayla veya aynı anda çalıştırmak.

# Yapısal Elemanları
- Composite Command, klasik Command Pattern bileşenlerine ek olarak aşağıdaki bileşenleri içerir:

1. CompositeCommand (Kompozit Komut): Bir veya daha fazla komutu içeren ve bunları yönetebilen özel bir komut sınıfı.

2. Leaf Commands (Yaprak Komutlar): Tek tek komutları temsil eden ve CompositeCommand tarafından yönetilen komut sınıfları.

# Avantajları
1. Basitlik ve Yönetilebilirlik:
    - Karmaşık işlemleri daha küçük ve yönetilebilir parçalara ayırarak kodun anlaşılabilirliğini artırır.

2. Esneklik:
    - Farklı komutları bir araya getirerek dinamik olarak yeni kompozit komutlar oluşturabilir.

3. Tekrar Kullanılabilirlik:
    - Mevcut komutları yeniden kullanarak yeni işlevsellikler oluşturmak kolaydır.

4. Bakım Kolaylığı:
    - Tek bir komut üzerinde yapılan değişiklikler, onu kullanan tüm kompozit komutlarda otomatik olarak geçerli olur.

# Dezavantajları
1. Artan Karmaşıklık:
    - Çok sayıda komutun bir araya getirilmesi, kompozit komutların yönetimini zorlaştırabilir.
2. Performans Sorunları:
    - Özellikle büyük ve karmaşık kompozit komutlar, bellek ve işlemci üzerinde ek yük oluşturabilir.

