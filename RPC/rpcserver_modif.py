"""
JSON-RPC Server
Menghitung jumlah huruf vokal, konsonan, dan kata dari sebuah kalimat
"""

from jsonrpc import JSONRPCResponseManager, dispatcher
from http.server import BaseHTTPRequestHandler, HTTPServer

# Fungsi untuk menghitung jumlah vokal
@dispatcher.add_method
def count_vowels(text: str):
    vowels = "aeiou"
    return sum(1 for ch in text.lower() if ch in vowels)

# Fungsi untuk menghitung jumlah konsonan
@dispatcher.add_method
def count_consonants(text: str):
    vowels = "aeiou"
    return sum(1 for ch in text.lower() if ch.isalpha() and ch not in vowels)

# Fungsi tambahan untuk menghitung jumlah kata
@dispatcher.add_method
def count_words(text: str):
    return len(text.split())

# Handler HTTP
class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        response = JSONRPCResponseManager.handle(post_data, dispatcher)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(response.json.encode())

# Jalankan server
def run(server_class=HTTPServer, handler_class=RequestHandler, port=4000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting JSON-RPC server on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()