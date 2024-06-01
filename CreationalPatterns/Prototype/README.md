- Prototype Pattern
Bu kalıp, bir nesnenin mevcut bir örneğini (prototipini) klonlayarak yeni nesneler oluşturmayı amaçlar.
Bu, özellikle yeni nesnelerin yaratılmasının maliyetli olduğu veya karmaşık bir yapılandırma gerektirdiği durumlarda faydalıdır.
Prototype Pattern, bir nesnenin mevcut durumunu kopyalayarak yeni bir örnek oluşturur.

- Ne Zaman Kullanılır?
1. Nesnelerin oluşturulması maliyetliyse.
2. Nesnelerin oluşturulması karmaşık bir yapılandırma gerektiriyorsa.
3. Farklı nesne türlerinin dinamik olarak belirlenmesi gerekiyorsa.
4. Nesneler arasında bağımsız kopyalar oluşturmak isteniyorsa.

- Avantajları
1. Nesne yaratma maliyetini düşürür.
2. Karmaşık yapılandırma süreçlerini basitleştirir.
3. Farklı türdeki nesnelerin dinamik olarak kopyalanabilmesini sağlar.

- Dezavantajları
1. Nesnelerin klonlanması için her nesnenin klonlanabilir (cloneable) olması gerekir, bu da bazı durumlarda zor olabilir.
2. Derin kopyalama (deep copy) ve sığ kopyalama (shallow copy) konularında dikkatli olunmalıdır. Yanlış türde kopyalama istenmeyen yan etkilere yol açabilir.

--> NOT: 'copy' modülü, bir nesnenin derin kopyasını oluşturur. Derin kopyalama, nesnenin kendisinin ve onun içerdiği tüm nesnelerin replikalarını oluşturur.
Bu, klonlanan nesnenin tamamen bağımsız bir kopyası anlamına gelir.

--> Sığ Kopya (Shallow Copy) ve Derin Kopya (Deep Copy) Arasındaki Fark
Sığ Kopya (Shallow Copy): Sığ kopyalama, sadece nesnenin kendisini kopyalar. Ancak, nesne başka nesnelere referans içeriyorsa, bu referanslar kopyalanmaz; yani, sığ kopya hala orijinal nesneye bağlıdır.

Örneğin: copy.copy()

--> Derin Kopya (Deep Copy): Derin kopyalama, nesnenin kendisini ve onun içerdiği tüm nesneleri de kopyalar. Bu, orijinal nesne ile klon arasında ***tam bağımsızlık*** sağlar.

Örneğin: copy.deepcopy()

