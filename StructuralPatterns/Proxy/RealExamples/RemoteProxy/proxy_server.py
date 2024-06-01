from flask import Flask, jsonify
import requests

class ProxyServer:
    def __init__(self):
        self.main_server_url = 'http://localhost:5000/data'

    def get_data(self):
        try:
            response = requests.get(self.main_server_url)
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

app = Flask(__name__)
proxy_server = ProxyServer()

@app.route('/data')
def get_data():
    data = proxy_server.get_data()
    return jsonify(data)

if __name__ == "__main__":
    app.run(port=5001)
