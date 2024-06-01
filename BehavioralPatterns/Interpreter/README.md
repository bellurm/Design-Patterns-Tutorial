# Interpreter Pattern
- Bu desen, belirli bir dilin veya problem alanının ifadelerini yorumlamak ve yürütmek için kullanılır. Genellikle bir dilin gramerini tanımlayan bir yapıyla birlikte kullanılır ve bu grameri izleyen ifadeleri yorumlamak için bir yorumlayıcı sağlar

# Temel Amacı
- Interpreter Pattern'ın ana amacı, bir dil veya belirli bir problem alanının ifadelerini yorumlamak ve işlemek için bir mekanizma sağlamaktır. Bu desen, aşağıdaki durumlarda kullanışlıdır:

1. Belirli Bir Dilin İfadelerinin İşlenmesi: Bir dilin belirli bir gramerine dayalı ifadelerin yorumlanması ve işlenmesi.

2. Özelleştirilmiş İfadelerin Yorumlanması: Belirli bir problem alanına özgü ifadelerin yorumlanması ve işlenmesi (örneğin, matematiksel ifadeler, mantıksal ifadeler, düzenli ifadeler vb.).

3. Dil Yönetimi: Bir dili yorumlamak ve yürütmek için bir arayüz sağlayarak, dili kullanarak problem çözme sürecini kolaylaştırmak.

# Yapısal Elemanlar
1. AbstractExpression (Soyut İfade): Dildeki herhangi bir ifadeyi temsil eden soyut bir sınıf veya arayüz. Yorumlama işlemi için bir interpret() yöntemi içerir.

2. TerminalExpression (Terminal İfade): Soyut ifade sınıfını uygulayan ve belirli bir dilin terminal ifadelerini temsil eden somut sınıflar.

3. NonTerminalExpression (Non-Terminal İfade): Soyut ifade sınıfını uygulayan ve belirli bir dilin non-terminal ifadelerini temsil eden somut sınıflar. İfadeleri bir araya getirerek veya diğer ifadelerle birleştirerek yorumlamak için kullanılır.

4. Context (Bağlam): Yorumlayıcıya verileri sağlayan veya yorumlama sürecini yöneten sınıf. Genellikle dilin durumunu ve yorumlama sırasında kullanılacak diğer bilgileri içerir.

# Avantajlar
1. Esneklik: Yeni ifade türleri kolayca eklenebilir.
2. Modülerlik: Dilin farklı bileşenleri ayrı sınıflarda temsil edilir.
3. Özelleştirme: Her ifade türü için özel davranışlar tanımlanabilir.

# Dezavantajlar
1. Karmaşıklık: Karmaşık dil yapılarının yorumlanması ve yönetilmesi zor olabilir.
2. Performans: Yorumlama işlemi yavaş olabilir, özellikle büyük ifade ağaçlarında.

# Lexing - Parsing
- Lexing ve Parsing, derleyicilerin ve yorumlayıcıların temel bileşenlerinden ikisidir ve birlikte bir dilin kaynak kodunu analiz etmek için kullanılırlar. İlk olarak, Lexing (Tokenization) işlemi, girdi metni (kaynak kod) üzerinde bir tarama işlemi yapar ve metni sembolik anlamları olan parçalara ayırır, bunlara "token" denir. Ardından, Parsing, bu tokenleri bir gramer kuralı setine göre yapılandırarak, metnin yapısını analiz eder ve yorumlar.

# Lexing (Tokenization)
- Lexing, girdi metni (kaynak kod) üzerinde bir tarama işlemi gerçekleştirir ve belirli semantik anlamlara sahip parçalara ayırır, bunlara "token" denir. Her bir token, dilin semantik yapısını temsil eder. Örneğin, bir programlama dilinde bir değişken, bir anahtar kelime, bir sayı veya bir operatör gibi.

# Lexing'in Adımları:
1. Girdi Metnini Tarama: Girdi metni karakter karakter taranır ve semantik olarak anlamlı parçalar bulunur.

2. Token Oluşturma: Bulunan parçalar, belirli türlerde tokenlere dönüştürülür.

3. Tokenlerin Ayıklanması: Gereksiz karakterler (boşluklar, yorumlar gibi) atılır veya tokenler arasında ayrım yapılır.

4. Tokenlerin Döndürülmesi: Elde edilen tokenler bir listeye eklenir veya birer birer işlenir.

# Parsing
- Parsing, Lexing işlemi sonucunda elde edilen tokenlerin dilin gramer kurallarına uygun olarak yapılandırılması işlemidir. Bu işlem, dilin sentaksının doğru olup olmadığını belirler ve ifadeyi bir ağaç veri yapısına dönüştürür.

# Parsing'in Adımları:
1. Tokenlerin Okunması: Lexing işlemi sonucunda elde edilen tokenler okunur.

2. Dilin Gramer Kurallarına Göre Analiz: Tokenler, dilin belirli gramer kurallarına göre analiz edilir ve yapılandırılır.

3. Sözdizimi Ağacının Oluşturulması: Tokenler, bir sentaks ağacı veya sözdizimi ağacı adı verilen bir ağaç veri yapısına dönüştürülür.

4. Doğrulama ve İşlem Yapılması: Oluşturulan ağaç, dilin belirli yapılarına karşılık gelir ve bu yapılar üzerinde doğrulama ve işlem yapılır.

# Lexing ve Parsing'in Önemi
1. Dil Analizi: Lexing ve Parsing, bir dilin yapısını anlamak ve analiz etmek için kullanılır.
2. Derleme ve Yorumlama: Lexing ve Parsing, derleyiciler ve yorumlayıcılar gibi yazılımların temel bileşenleridir.
3. Hata Yakalama: Yanlış yazılmış kodlar veya sentaks hataları, Lexing ve Parsing işlemi sırasında tespit edilir ve rapor edilir.
4. Optimizasyon: Derleyiciler, Parsing sırasında elde edilen yapıları optimize etmek için kullanılabilir.

# lexing_parsing.py Açıklaması
Kodda, `lexer` fonksiyonu girdi matematiksel ifadeyi tokenlere ayırır. Daha sonra, `parser` fonksiyonu bu tokenleri kullanarak bir parse ağacı oluşturur. Örneğin, girdi olarak `"3 + 4 * (5 - 2)"` ifadesi verildiğinde, `lexer` fonksiyonu bunu `"3", "+", "4", "*", "(", "5", "-", "2", ")"` tokenlerine ayırır. `parser` fonksiyonu ise bu tokenleri kullanarak bir parse ağacı oluşturur. Oluşturulan parse ağacı şu şekildedir:

['3', '4', '5', '2', '-', '*', '+']

Bu parse ağacı, orijinal ifadenin matematiksel önceliğine göre doğru bir şekilde yapılandırılmış bir ifadeyi temsil eder. Bu örnek, basit bir lexer ve parser kullanarak bir matematiksel ifadeyi analiz etmenin temel bir örneğidir.
