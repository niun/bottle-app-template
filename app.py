#!/usr/bin/env python

import os
import sys

# change working directory to directory containing this file:
app_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(app_dir)

# import bottle from the bottle directory next to this file (if existent)
# in favor to the framework installed elsewhere in the search path.
# Can be used to distribute app with a specific bottle version included.
sys.path.insert(0, os.path.join(app_dir,'bottle'))
from bottle import default_app, route, run, debug

import socket

# enable tracebacks, disable template cache, ...
debug(True)


default_app.push()


@route('/hello')
def say_hello():
    return "Hallo Welt"


app = default_app.pop()


if __name__ == '__main__':
    server_port = 8080
    port_found = False

    while not port_found:
        try:
            run(app=app, host='0.0.0.0', port=server_port, reloader=True)
            port_found = True
        except socket.error:
            print "Not possible to listen on port {0}".format(server_port)
            print "Trying the next port..."
            server_port = server_port + 1

