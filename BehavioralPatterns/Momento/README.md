# Memento Pattern
- Bir nesnenin iç durumunu dışarıdan erişilmez şekilde kaydetmek ve gerektiğinde bu durumu geri yüklemek için kullanılan davranışsal bir tasarım desenidir. Bu desen, özellikle geri alma (undo) işlemleri veya nesnelerin önceki durumlarına dönmesi gereken durumlar için faydalıdır.

# Temel Bileşenler
1. Originator (Oluşturan): İç durumunu bir Memento nesnesine kaydeden ve gerektiğinde bu durumu geri yükleyen sınıftır.

2. Memento: Originator'un durumunu depolayan ve dışarıdan erişilemeyen sınıftır. Bu sınıfın içeriği sadece Originator tarafından bilinir ve değiştirilir.

3. Caretaker (Bakıcı): Memento nesnelerini saklayan ve gerektiğinde bu nesneleri Originator'a ileterek durumu geri yükleyen sınıftır. Caretaker, Memento'nun iç yapısını bilmez ve değiştirmez.

# Avantajları
1. Durumun Korunması: Nesnenin iç durumunu dışarıya açmadan korur ve geri yükler.

2. Basit Geri Alma İşlemleri: Kullanıcıya basit ve etkili bir geri alma/yeniden yapma mekanizması sağlar.

3. Bağımsızlık: Originator ve Caretaker arasındaki bağımsızlığı korur, bu sayede Memento nesnesinin içeriği yalnızca Originator tarafından bilinir.

# Dezavantajları
1. Bellek Kullanımı: Çok sayıda veya büyük Memento nesnesi oluşturulması durumunda bellek kullanımı artabilir.

2. Performans: Durumun sık sık kaydedilip geri yüklenmesi performans problemlerine yol açabilir.
