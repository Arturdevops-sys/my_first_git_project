from http.server import BaseHTTPRequestHandler, HTTPServer
import os
from dotenv import load_dotenv

load_dotenv()


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        db = os.getenv("DATABASE")
        port = os.getenv("PORT")

        massage = f"DB: {db}, PORT: {port}, Status: 200"

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(massage.encode())


server = HTTPServer(("0.0.0.0", 8000), Handler)
print("Server running on port 8000...")
server.serve_forever()
