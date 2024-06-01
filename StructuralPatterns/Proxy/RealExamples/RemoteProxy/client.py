import requests

class Client:
    def __init__(self, proxy_server_url):
        self.proxy_server_url = proxy_server_url

    def get_data(self):
        try:
            response = requests.get(self.proxy_server_url)
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

def main():
    proxy_server_url = 'http://localhost:5001/data'
    client = Client(proxy_server_url)
    data = client.get_data()
    print(f"Received data: {data}")

if __name__ == "__main__":
    main()
