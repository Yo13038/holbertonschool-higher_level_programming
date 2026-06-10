#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleAPIHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            
            data_to_serve = {"name": "John", "age": 30, "city": "New York"}
            json_string = json.dumps(data_to_serve)
            self.wfile.write(json_string.encode("utf-8"))
            
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"OK")
        
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"Endpoint not Found")

def run():
    server_address = ('', 8000)
    my_server = HTTPServer(server_address, SimpleAPIHandler)
    my_server.serve_forever()


if __name__ == "__main__":
    run()