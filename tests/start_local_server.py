from http.server import HTTPServer, CGIHTTPRequestHandler
import os

from time import sleep
import sys


# Use the following command to run testing server
#      python start_local_server.py hostnamehere portnumberhere
# e.g: python start_local_server.py 127.0.0.1 8080
# NOTE: make sure to run file in local directory

arguments = sys.argv


def start_server(host_address="127.0.0.1", port=80):
    os.chdir('.')
    server = HTTPServer(server_address=(str(host_address), int(port)), RequestHandlerClass=CGIHTTPRequestHandler)
    server.serve_forever()

    return server


server = start_server(*arguments[1:])
