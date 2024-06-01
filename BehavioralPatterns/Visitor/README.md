# Visitor Pattern
- Bu desen, bir nesne yapısına yeni operasyonlar eklemenize olanak tanır; bu işlemi nesne yapısını değiştirmeden gerçekleştirir. Visitor Pattern, bir işlemi nesne yapısının her öğesi üzerinde gerçekleştirmek için kullanılır ve böylece yeni işlemler eklemek için sınıfların değiştirilmesi gerekmez.

# Temel Özellikler ve Amaç
1. Çift Dispatch (Double Dispatch): Visitor Pattern, çift dispatch sağlar. Yani, hangi işlemin gerçekleştirileceği hem ziyaret edilen nesneye hem de ziyaretçiye bağlıdır.
2. Ayrılmış Sorumluluklar: Nesne yapısı ve işlemler arasında sorumlulukları ayrıştırır. İşlemler Visitor sınıflarında tanımlanırken, nesne yapısı bu işlemlerden habersizdir.
3. Kolay Genişletilebilirlik: Yeni işlemler eklemek kolaydır, sadece yeni bir Visitor sınıfı ekleyerek mevcut nesne yapısında değişiklik yapmadan yeni işlemler tanımlayabilirsiniz.

# Yapısal Bileşenler
1. Visitor (Ziyaretçi) Arayüzü: Ziyaretçilerin gerçekleştireceği işlemleri tanımlar. Her nesne türü için bir ziyaret metodu içerir.
2. Concrete Visitor (Somut Ziyaretçi) Sınıfları: Visitor arayüzünü implemente eden ve her nesne türü için belirli işlemleri gerçekleştiren sınıflardır.
3. Element (Öğe) Arayüzü: Accept metodunu tanımlar, bu metod bir Visitor nesnesini parametre olarak alır.
4. Concrete Element (Somut Öğe) Sınıfları: Element arayüzünü implemente eden ve Accept metodunu kullanarak ziyaretçinin kendilerini ziyaret etmesini sağlayan sınıflardır.
5. Object Structure (Nesne Yapısı): Elementlerin koleksiyonudur ve bir veya daha fazla Visitor nesnesinin bu elementleri ziyaret etmesine olanak tanır.

# Avantajlar
1. Yeni İşlemler Eklemek Kolay: Yeni bir Visitor sınıfı eklemek, mevcut nesne yapısında değişiklik yapmadan yeni işlemler eklemenizi sağlar.

2. Ayrılmış Sorumluluklar: Nesne yapısı ve işlemler arasında sorumlulukları ayrıştırır. Nesne yapısı işlemlerden habersizdir, bu da kodun daha modüler ve yönetilebilir olmasını sağlar.

3. Çift Dispatch: Hangi işlemin gerçekleştirileceği, hem ziyaret edilen nesneye hem de ziyaretçiye bağlıdır. Bu, daha dinamik ve esnek bir yapı sağlar.

# Dezavantajlar
1. Yeni Nesne Türleri Eklemek Zor: Nesne yapısına yeni bir tür eklemek, tüm Visitor sınıflarının güncellenmesini gerektirir. Bu, bakım maliyetini artırabilir.

2. Karmaşıklık: Visitor Pattern, çift dispatch ve ziyaretçi yöntemleri nedeniyle kodun karmaşıklığını artırabilir.

3. Performans: Çok sayıda nesne ve ziyaretçi kombinasyonu, performans üzerinde olumsuz etkiler yaratabilir.

# Visitor Pattern Türleri
1. Intrusive Visitor
    - Intrusive Visitor, ziyaret edilecek sınıfların (elementler) ziyaretçiyi kabul etme (accept) metodunu kendilerinin implemente ettiği bir yaklaşımdır. Bu yöntem, nesne hiyerarşisinde değişiklik yapmayı gerektirir.

    # Avantajlar:
        - Uygulaması genellikle basit ve doğrudan.
        - Performans açısından optimize edilebilir.
    
    # Dezavantajlar:
        - Mevcut sınıflarda değişiklik yapmayı gerektirir.
        - Kapalı bir sistemde veya üçüncü taraf kütüphanelerde uygulanması zordur.
    
2. Reflective Visitor
    - Reflective Visitor, nesne yapısındaki elemanların türlerini dinamik olarak belirlemek için yansıma (reflection) kullanır. Bu, ziyaretçilerin element sınıflarını bilmesini gerektirmez.

    # Avantajlar:
        - Daha az intrusif.
        - Dinamik sistemlerde kullanışlı.
    
    # Dezavantajlar:
        - Performans maliyeti yüksektir.
        - Hata ayıklama ve bakım zorluğu artabilir.

3. Classic Visitor
    - Classic Visitor, en yaygın kullanılan Visitor Pattern türüdür. Bu yöntemde, element sınıfları accept metodunu ve visitor sınıfları her bir element türü için visit metodunu içerir.

    # Avantajlar:
        - Statik tür kontrolü.
        - Kolay hata ayıklama.
        
    # Dezavantajlar:
        - Yeni element türleri eklemek zor.
        - Mevcut element sınıflarında değişiklik yapmayı gerektirir.

4. Classic Visitor Refined
    - Classic Visitor Refined, klasik ziyaretçiye benzer ancak bazı eklemelerle daha esnek ve genişletilebilir hale getirilmiştir. Bu yöntemde, çift yönlü (double dispatch) tekniklerini kullanarak elementlerin ve ziyaretçilerin bağımsız olarak genişletilmesini sağlar.

    # Avantajlar:
        - Daha esnek ve genişletilebilir.
        - Mevcut sistemlerle entegrasyonu kolay.
    
    # Dezavantajlar:
        - Karmaşıklık artar.
        - Implementasyonu zor olabilir.

