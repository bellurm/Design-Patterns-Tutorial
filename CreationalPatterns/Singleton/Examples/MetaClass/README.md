--> SingletonMeta Metaclass'ı:

'_instances' adında bir sınıf değişkeni tanımlar ve bu değişken, her sınıf için oluşturulan örnekleri saklar.
'__call__' metodu, bir sınıfın örneklendiği zaman çalışır. Bu metod, verilen sınıfın örneğinin _instances sözlüğünde olup olmadığını kontrol eder. Eğer örnek yoksa, super(SingletonMeta, cls).__call__(*args, **kwargs) ile yeni bir örnek oluşturur ve sözlüğe ekler; eğer zaten varsa mevcut örneği döner.
SupermarketCheckout Sınıfı:

--> SupermarketCheckout sınıfı,

SingletonMeta metaclass'ını kullanarak tanımlanır. Bu sayede, SupermarketCheckout sınıfı oluşturulurken SingletonMeta metaclass'ının '__call__' metodu devreye girer ve Singleton davranışını sağlar.
'total_sales' ve 'transactions' adlı özellikler, süpermarketin toplam satışlarını ve işlem listesini saklar.
'scan_item' metodu, bir ürünün fiyatını tarar, toplam satışları günceller ve işlem listesine ekler.
'get_total_sales' ve 'get_transactions' metodları, toplam satışları ve işlem listesini döner.

--> Kullanım ve Doğrulama:

checkout1 ve checkout2 değişkenleri, SupermarketCheckout sınıfının örnekleri olarak oluşturulur. Ancak metaclass sayesinde aslında aynı örneğe referans verirler.
checkout1 ve checkout2 üzerinden yapılan ürün tarama işlemleri, aynı nesne üzerinde gerçekleşir ve bu nedenle her iki değişkende de aynı toplam satış ve işlem listesi görüntülenir.
checkout1 is checkout2 ifadesi True döner, çünkü her iki değişken de aynı nesneyi işaret eder.
