import http.server
import socketserver
import threading

PORT = 8080

class ThreadedHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    """Handle requests in a separate thread."""

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            html = """
            <html>
            <head><title>Python Threaded Server</title></head>
            <body>
            <h1>Welcome to the Python Multi-threaded Web Server!</h1>
            <p>Try visiting <a href="/hello">/hello</a> for a greeting.</p>
            </body>
            </html>
            """
            self.wfile.write(html.encode("utf-8"))
        elif self.path == "/hello":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello! This is a threaded Python server.")
        else:
            # Serve files or 404
            super().do_GET()

def run_server():
    server = ThreadedHTTPServer(("0.0.0.0", PORT), Handler)
    print(f"🌐 Serving at http://localhost:{PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Server stopped.")

if __name__ == "__main__":
    run_server()

