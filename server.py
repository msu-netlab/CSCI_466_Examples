import os
import functools
import shutil
from http import HTTPStatus
from http.server import CGIHTTPRequestHandler, HTTPServer, BaseHTTPRequestHandler
import json


class MyHTTPRequestHandler(CGIHTTPRequestHandler):
    """A custom HTTP Request Handler based on SimpleHTTPRequestHandler"""
    
    server_version = "My_HTTP_Server/"
    
    def __init__(self, *args, directory=None, **kwargs):
        super().__init__(*args, directory=os.getcwd()+directory, **kwargs)  # initialize the base handler
    
    def do_GET(self):
        """Serve a GET request."""
        
        # get info from the HTTP request
        # look at https://docs.python.org/3/library/http.server.html for other BaseHTTPRequestHandler instance variables
        print(self.client_address)
        
        # update the path with the prefix of server files
        self.path = self.directory + self.path
        print(self.path)
        
        # reply to client
        try:
            f = open(self.path, 'rb')
            self.send_response(HTTPStatus.OK)
            self.end_headers()
            shutil.copyfileobj(f, self.wfile)
            f.close()
        except OSError:
            self.send_response(HTTPStatus.NOT_FOUND)
            self.end_headers()

    def do_POST(self):
        print('path: ', self.path)
        json_bytes = self.rfile.read(int(self.headers['Content-Length']))
        print('json_bytes: ', json_bytes)
        json_string = json.loads(json_bytes)
        print('json_string: ', json_string)
        throw = json.loads(json_string)
        print('throw: ', throw['throw'])
        
        self.send_response(HTTPStatus.OK)
        self.end_headers()



def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', 8000)
    
    handler = functools.partial(handler_class, directory='/www')
    httpd = server_class(server_address, handler)
    httpd.serve_forever()


if __name__ == "__main__":
    run(HTTPServer, MyHTTPRequestHandler)
