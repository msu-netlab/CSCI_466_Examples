import email
import io
import mimetypes
import os
import posixpath
import shutil
import urllib
import datetime
import html
import sys
from http import HTTPStatus
from http.server import SimpleHTTPRequestHandler, HTTPServer, BaseHTTPRequestHandler


class MyHTTPRequestHandler(SimpleHTTPRequestHandler):
	"""A custom HTTP Request Handler based on SimpleHTTPRequestHandler"""
	
	server_version = "My_HTTP_Server/"
	
	def __init__(self, *args, directory=None, **kwargs):
		if directory is None:
			directory = os.getcwd()    # start file path with the current directory
		self.directory = directory    # or with the directory passed in the argument
		super().__init__(*args, **kwargs)   # initialize the base handler
	
	def do_GET(self):
		"""Serve a GET request."""
		
		# get info from the HTTP request
		# look at https://docs.python.org/3/library/http.server.html for other BaseHTTPRequestHandler instance variables
		print(self.client_address)
		print(self.path)

		# create an HTTP response
		# look for different responses by trying different completions of HTTPStatus.
		self.send_response(HTTPStatus.OK)
		self.end_headers()
		
		# send the requested file
		f = open(self.path.strip('/'), 'rb')   # open the requested file
		try:
			shutil.copyfileobj(f, self.wfile)   # copy the file for inclusion in the response
		finally:
			f.close()
	


def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
	server_address = ('', 8000)
	httpd = server_class(server_address, handler_class)
	httpd.serve_forever()



if __name__ == "__main__":
	run(HTTPServer, MyHTTPRequestHandler)
