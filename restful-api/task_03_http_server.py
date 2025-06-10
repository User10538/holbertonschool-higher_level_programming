#!/usr/bin/python3
import json

from http.server import BaseHTTPRequestHandler, HTTPServer

def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server..")
    httpd.serve_forever()

class mySimpleHandle(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/data":
            dataSet = {"name": "John", "age": 30, "city": "New York"}
            jsonData = json.dumps(dataSet).encode('utd-8')

            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(jsonData)
        else:
            self.wfile.write("Hello, this is a simple API!")
