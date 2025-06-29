#!/usr/bin/python3
import json

from http.server import BaseHTTPRequestHandler, HTTPServer

class MySimpleHandle(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/data":
            dataSet = {"name": "John", "age": 30, "city": "New York"}
            jsonData = json.dumps(dataSet).encode('utf-8')

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(jsonData)

        elif self.path == "/":
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/status":
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")
        
        elif self.path == "/info":
             dataSet = {"version": "1.0", "description": "A simple API built with http.server"}
             jsonData = json.dumps(dataSet).encode('utf-8')
             self.send_response(200)
             self.send_header('Content-type', 'application/json')
             self.end_headers()
             self.wfile.write(jsonData)

        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Endpoint not found")
    

def run(server_class=HTTPServer, handler_class=MySimpleHandle):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server..")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
