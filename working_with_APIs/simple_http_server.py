# File name: simple_http_server.py

from http.server import HTTPServer, SimpleHTTPRequestHandler

# Define server address and port
HOST = "localhost"
PORT = 8000

# Create server
server = HTTPServer((HOST, PORT), SimpleHTTPRequestHandler)
print(f"Serving HTTP on {HOST}:{PORT}...")

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nServer stopped.")
    server.server_close()

