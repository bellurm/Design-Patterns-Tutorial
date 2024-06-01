# State Pattern
- Bir nesnenin iç durumuna göre davranışını değiştirmesini sağlayan davranışsal bir tasarım desenidir. Bu desen, nesnelerin farklı durumlarda farklı davranışlar sergilemesini kolaylaştırır ve kodun okunabilirliğini ve bakımını iyileştirir.

# Temel Prensipler
1. Context (Bağlam) Nesnesi: Durumları yöneten ve durum değişikliklerini başlatan ana nesne. Bu nesne, mevcut durumu temsil eden bir durum nesnesini (State) tutar.
2. State (Durum) Arayüzü: Farklı durumların ortak davranışlarını tanımlayan bir arayüz.
3. ConcreteState (Somut Durum) Sınıfları: Bu arayüzü implement eden sınıflar. Her biri Context nesnesinin belirli bir durumda nasıl davranacağını belirler.

# State Pattern’in Yapısı
1. Context: Durum nesnesini tutar ve istemcilere durumlar arasında geçiş yapma imkanı sağlar.
2. State: Context tarafından çağrılan işlemleri tanımlayan arayüz veya soyut sınıf.
3. ConcreteState: State arayüzünü implement eden ve Context'in farklı durumlarda nasıl davranacağını belirleyen sınıflar.

# Avantajları
1. Kodun Okunabilirliği ve Bakımı: Kodun durumlara göre nasıl değiştiği açıkça belirlenir, bu da bakım ve anlaşılabilirliği artırır.
2. Tek Sorumluluk İlkesi: Her durum sınıfı, yalnızca o duruma özgü davranışları içerir, bu da kodun daha modüler ve yönetilebilir olmasını sağlar.
3. Açık Kapalı İlkesi: Yeni durumlar eklemek kolaydır, mevcut kodda değişiklik yapmadan yeni durum sınıfları ekleyebilirsiniz.

# Dezavantajları
1. Kod Karmaşıklığı: Durum sayısı arttıkça, durumu yöneten sınıf sayısı da artar, bu da kodun karmaşıklığını artırabilir.
2. Bağımlılıklar: Context nesnesi ve durum nesneleri arasında güçlü bağımlılıklar oluşabilir, bu da kodun esnekliğini azaltabilir.

# Switch-Based
- State Pattern'da "Switch-Based" yaklaşım, durumu ve duruma bağlı davranışları yönetmek için duruma dayalı switch veya if-else yapılarını kullanmayı ifade eder. Bu yaklaşımda, durumlar arasındaki geçişleri ve her durumda gerçekleştirilecek işlemleri kontrol etmek için genellikle if-else veya switch-case (bazı programlama dillerinde) gibi koşullu yapılar kullanılır. Switch-Based yaklaşımda, durumlar ve davranışlar genellikle bir enum veya benzeri bir yapı ile temsil edilir.