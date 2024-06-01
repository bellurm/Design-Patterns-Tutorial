# Strategy Pattern
- Bu desenin temel amacı, bir sınıfın belirli bir işlevselliği farklı algoritmalar veya yöntemlerle gerçekleştirmesi gerektiği durumlarda kullanılır. Strategy Pattern, bu algoritmaların birbirlerinin yerine kullanılabilmesini ve kolayca değiştirilebilmesini sağlar.

# Temel Özellikler ve Amaç
1. Değişikliklerin Kolay Yönetimi: Farklı algoritmaların veya stratejilerin uygulanabilirliğini artırarak kodun esnekliğini ve bakımını kolaylaştırır.

2. Open/Closed Principle: Yazılım bileşenlerinin yeni özellikler eklemek için genişlemeye açık, ancak mevcut özelliklerin değiştirilmesine kapalı olması prensibini destekler.

3. Kod Tekrarlamayı Azaltma: Aynı işlevselliği farklı yöntemlerle gerçekleştiren kod parçalarının merkezi bir yerden yönetilmesini sağlar, bu da kod tekrarını azaltır.

# Yapısal Bileşenler
1. Strategy (Strateji) Arayüzü: Algoritmaların ortak arayüzünü tanımlar. Bu arayüz, algoritmaların birbirinin yerine kullanılabilmesini sağlar.

2. Concrete Strategy (Somut Strateji) Sınıfları: Strategy arayüzünü implemente eden ve farklı algoritmaları içeren sınıflardır. Her biri Strategy arayüzünde tanımlanan metodları kendi spesifik algoritmasına göre uygular.

3. Context (Bağlam) Sınıfı: Bir Strategy nesnesi ile çalışır ve istemcinin Strategy arayüzünü kullanarak belirli bir algoritmayı çalıştırmasına olanak tanır. Algoritma seçimini ve uygulamasını bu sınıf yönetir.

# Avantajlar
1. Esneklik ve Genişletilebilirlik:
    - Yeni Strateji Ekleme: Yeni bir strateji eklemek, mevcut sınıflarda minimum değişiklik gerektirir. Yeni bir Concrete Strategy sınıfı oluşturmak yeterlidir.
    - Dinamik Değişiklik: Uygulama çalışırken stratejiyi değiştirme olanağı sağlar. Bu, runtime'da farklı algoritmaları test etmek veya kullanıcı tercihlerine göre strateji değiştirmek için yararlıdır.

2. Bakım Kolaylığı:
    - Modülerlik: Algoritmaların ayrı sınıflar halinde tanımlanması, kodun daha anlaşılır ve bakımı kolay olmasını sağlar. Her bir algoritma kendi sınıfında tanımlandığı için, değişiklikler sadece ilgili sınıfta yapılır.
    - Sorumlulukların Ayrılması: Kodun sorumluluklarını ayrıştırır, böylece her sınıf sadece tek bir görevi yerine getirir.

3. Kod Tekrarının Azaltılması:
    - Tekrar Kullanılabilirlik: Farklı sınıflar arasında aynı işlevselliği sağlamak için ortak stratejileri kullanma imkanı verir, bu da kod tekrarını azaltır.

4. Test Edilebilirlik:
    - Bağımsız Test: Her bir strateji bağımsız olarak test edilebilir. Bu, bir stratejideki hatanın diğerlerini etkilemesini önler.

# Dezavantajlar
1. Kod Karmaşıklığı:
    - Sınıf Sayısının Artması: Birden çok strateji sınıfı yaratmak, kod tabanında sınıf sayısının artmasına neden olabilir, bu da kodu daha karmaşık hale getirebilir.
    - Yönetim Zorluğu: Çok sayıda stratejiyi yönetmek zor olabilir ve geliştiricilerin bu stratejiler arasındaki ilişkileri anlamaları zaman alabilir.

2. Performans:
    - Ekstra Yönlendirme: Strateji deseninde, stratejinin seçimi ve uygulanması sırasında ekstra yönlendirme katmanları eklenir. Bu, özellikle performans kritik uygulamalarda bir miktar performans kaybına yol açabilir.
    - Bellek Kullanımı: Birden fazla strateji sınıfının mevcut olması, bellek kullanımını artırabilir.
