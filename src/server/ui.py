import http.server, os, socketserver
from .info import generate_qr_code

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.path.join(os.getcwd(), "src", "client", "dist"), **kwargs)

def start():
    port = int(os.getenv('UI_PORT', 8000))
    generate_qr_code(port)
    
    handler = CustomHTTPRequestHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"Serving HTTP on port {port}")
        httpd.serve_forever()
