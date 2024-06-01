### 'def singleton(cls):' kısmı için ###
1. 'singleton' adlı bir decorator fonksiyon tanımlanır.
2. 'instances' adında bir sözlük tanımlanır. Bu sözlük, her sınıf için oluşturulan örnekleri saklar.
3. 'get_instance' adlı iç içe bir fonksiyon tanımlanır. Bu fonksiyon, dekore edilen sınıfın tek bir örneğini döndürür.
4. 'get_instance' fonksiyonu, eğer dekore edilen sınıfın örneği instances sözlüğünde yoksa yeni bir örnek oluşturur ve sözlüğe ekler; eğer zaten varsa mevcut örneği döndürür.
5. Son olarak, 'get_instance' fonksiyonu dekoratörün dönüş değeri olarak kullanılır.


###
'@singleton
class SupermarketCheckout:'
kısmı için
###
1. 'SupermarketCheckout' adında bir sınıf tanımlanır ve üzerine '@singleton' dekoratörü uygulanır.
2. Bu dekoratör, 'SupermarketCheckout' sınıfını singleton fonksiyonuna argüman olarak gönderir ve bu fonksiyon tarafından dönüştürülür.
3. Böylece, 'SupermarketCheckout' sınıfı artık Singleton Pattern'i takip eder. Herhangi bir kod, 'SupermarketCheckout' sınıfını çağırdığında, aslında bu sınıfın yalnızca bir örneği oluşturulur.



###
'if __name__ == "__main__":'
kısmı için
###
1. 'SupermarketCheckout' sınıfının iki örneği oluşturulur: 'checkout1' ve 'checkout2'.
2. Her iki örneğe de ürün taranır ve toplam satışlar kontrol edilir.
3. Her iki örneğin de aynı nesneye işaret ettiği, yani aynı Singleton örneğine refere ettikleri doğrulanır.

