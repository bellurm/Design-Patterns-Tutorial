# Remote Proxy ile uzaktaki bir sunucuya yapılan çağrı
from abc import ABC, abstractmethod

# Subject
class DataSource(ABC):
    @abstractmethod
    def fetch_data(self):
        pass

# RealSubject
class RemoteDataSource(DataSource):
    def fetch_data(self):
        # Simulating a network call
        print("Fetching data from remote server")
        return {"data": "Sample data from remote server"}

# Proxy
class ProxyDataSource(DataSource):
    def __init__(self):
        self.remote_data_source = RemoteDataSource()

    def fetch_data(self):
        print("Proxy: Forwarding request to remote data source")
        return self.remote_data_source.fetch_data()

# Client
def main():
    data_source = ProxyDataSource()
    data = data_source.fetch_data()
    print(data)

if __name__ == "__main__":
    main()
