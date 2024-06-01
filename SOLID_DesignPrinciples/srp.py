# Tek Sorumluluk İlkesi (Single Responsibility Principle - SRP), yazılım geliştirme sürecinde önemli bir tasarım prensibidir.
# Bu ilke, her bir sınıf veya modülün yalnızca bir sorumluluğu olması gerektiğini belirtir.
# Başka bir deyişle, bir sınıf veya modül, yalnızca bir tek görev veya işlevi yerine getirmelidir.

# SRP'nin temel amacı, yazılım bileşenlerinin birbirlerine bağlılığını azaltmak ve kodu daha anlaşılır, bakımı daha kolay hale getirmektir.
# Bir bileşenin veya modülün birden fazla sorumluluğu varsa, bu durum kodun karmaşıklaşmasına, bakımının zorlaşmasına ve hata olasılığının artmasına neden olabilir.

# Örneğin, bir kullanıcı arayüzü sınıfı (UI class), kullanıcı girişini işlemek, veri doğrulamasını yapmak, veritabanına bağlanmak ve veri işleme işlevlerini içerebilir.
# Ancak, SRP'ye göre, bu sınıfın yalnızca kullanıcı arayüzüyle ilgili işlevleri yerine getirmesi gerekmektedir. Veri işleme veya doğrulama gibi işlevler ayrı sınıflara veya modüllere ayrılmalıdır.

# Bu prensip, yazılımın daha esnek, yeniden kullanılabilir ve bakımı daha kolay hale getirerek genel kalitesini artırır. Bu nedenle, SRP, yazılım geliştirme sürecinde önemli bir tasarım ilkesidir.

# AŞAĞIDAKİ KOD SRP'YE UYGUN DEĞİLDİR.

class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.entries.append(f"{self.count}: {text}")
        self.count += 1

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return "\n".join(self.entries)

    # break SRP
    def save(self, filename):
        file = open(filename, "w")
        file.write(str(self))
        file.close()

class PersistenceManager:
    def save_to_file(journal, filename):
        file = open(filename, "w")
        file.write(str(journal))
        file.close()


j = Journal()
j.add_entry("I cried today.")
j.add_entry("I ate a bug.")
print(f"Journal entries:\n{j}\n")

p = PersistenceManager()
file = r'c:\temp\journal.txt'
p.save_to_file(j, file)

# verify!
with open(file) as fh:
    print(fh.read())


# AŞAĞIDAKİ KOD SRP'YE UYGUNDUR.

class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.entries.append(f"{self.count}: {text}")
        self.count += 1

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return "\n".join(self.entries)


class PersistenceManager:
    @staticmethod
    def save_to_file(journal, filename):
        with open(filename, "w") as file:
            file.write(str(journal))

    @staticmethod
    def load_from_file(filename):
        with open(filename, "r") as file:
            return file.read()


j = Journal()
j.add_entry("I cried today.")
j.add_entry("I ate a bug.")
print(f"Journal entries:\n{j}\n")

file = r'c:\temp\journal.txt'
PersistenceManager.save_to_file(j, file)

# verify!
print(PersistenceManager.load_from_file(file))
