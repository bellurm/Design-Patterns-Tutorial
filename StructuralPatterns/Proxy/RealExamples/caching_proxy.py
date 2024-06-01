from abc import ABC, abstractmethod

class WebsiteData(ABC):
    @abstractmethod
    def get_page_content(self, page_url):
        pass

class RealWebsiteData(WebsiteData):
    def __init__(self):
        self.cache = {}

    def get_page_content(self, page_url):
        # Gerçek web sitesinden sayfa içeriğini alır
        page_content = f"Content of {page_url}"
        self.cache[page_url] = page_content  # Önbelleğe kaydet
        return page_content

class CachingProxy(WebsiteData):
    def __init__(self, real_data):
        self.real_data = real_data
        self.cache = {}

    def get_page_content(self, page_url):
        if page_url not in self.cache:
            # Önbellekte sayfa yoksa gerçek veriyi alır ve önbelleğe kaydeder
            self.cache[page_url] = self.real_data.get_page_content(page_url)
        return self.cache[page_url]

# Örnek Kullanım
def main():
    # Gerçek veri ve önbellek proxy'si oluştur
    real_data = RealWebsiteData()
    proxy = CachingProxy(real_data)

    # Web sitesinden sayfa içeriği al
    print(proxy.get_page_content("example.com/page1"))  # Gerçek veriden alır
    print(proxy.get_page_content("example.com/page2"))  # Gerçek veriden alır
    print(proxy.get_page_content("example.com/page1"))  # Önbellekten alır

if __name__ == "__main__":
    main()
