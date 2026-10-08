#!/usr/bin/python3
"""Module for a simple API using Python and http.server"""
from http.server import BaseHTTPRequestHandler, HTTPServer
from json import dumps as dumps


class Handler(BaseHTTPRequestHandler):
    """Handler for GET resuqest"""

    def _send(self, status, content_type, body):
        """Method handling the response"""
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.end_headers()
        self.wfile.write(body.encode("utf-8"))

    def do_GET(self):
        if self.path == "/":
            self._send(200, "text/plain", "Hello, this is a simple API!")
        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            self._send(200, "application/json", dumps(data))
        elif self.path == "/status":
            self._send(200, "text/plain", "OK")
        elif self.path == "/info":
            info = {"version": "1.0",
                   "description": "A simple API built with http.server"}
            self.send(200, "application/json", dumps(info))
        else:
            self._send(404, "text/plain", "404 Not Found: this end point does \
                                          not exist")

def run(port=8000):
    server = HTTPServer(("", port), Handler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()

if __name__ == "__main__":
    run()
