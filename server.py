import os
import shutil
from http import HTTPStatus
from http.server import SimpleHTTPRequestHandler, HTTPServer, BaseHTTPRequestHandler


class MyHTTPRequestHandler(SimpleHTTPRequestHandler):
    """A custom HTTP Request Handler based on SimpleHTTPRequestHandler"""
    
    server_version = "My_HTTP_Server/"
    path_prefix = "www"
    
    def __init__(self, *args, directory=None, **kwargs):
        if directory is None:
            directory = os.getcwd()  # start file path with the current directory
        self.directory = directory  # or with the directory passed in the argument
        super().__init__(*args, **kwargs)  # initialize the base handler
    
    def do_GET(self):
        """Serve a GET request."""
        
        # get info from the HTTP request
        # look at https://docs.python.org/3/library/http.server.html for other BaseHTTPRequestHandler instance variables
        print(self.client_address)
        print(self.path)
        
        # update the path with the prefix of server files
        self.path = self.path_prefix + self.path
        
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


def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == "__main__":
    run(HTTPServer, MyHTTPRequestHandler)
