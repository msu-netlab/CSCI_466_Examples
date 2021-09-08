import os
import functools
import shutil
from http import HTTPStatus
from http.server import SimpleHTTPRequestHandler, HTTPServer, BaseHTTPRequestHandler


class MyHTTPRequestHandler(SimpleHTTPRequestHandler):
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




def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', 8000)
    
    handler = functools.partial(handler_class, directory='/www')
    httpd = server_class(server_address, handler)
    httpd.serve_forever()


if __name__ == "__main__":
    run(HTTPServer, MyHTTPRequestHandler)
