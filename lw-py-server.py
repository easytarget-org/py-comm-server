'''
So here it is.. lw-py-server

V1 ONLY DOES GRBL (and FluidNC)
'''

from http import server
from socketserver import TCPServer
from functools import partial

appdir = 'web_app'
PORT = 8000

Handler = partial(server.SimpleHTTPRequestHandler, directory=appdir)

with TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
