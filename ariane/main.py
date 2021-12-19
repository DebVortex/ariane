"""Top-level package for Ariane."""

__author__ = """Max Brauer"""
__email__ = 'max@max-brauer.de'
__version__ = '0.1.0'


from simple_websocket_server import WebSocketServer

from server import WebSocketHandler

HOST = 'localhost'
PORT = 8080

if __name__ == '__main__':
    server = WebSocketServer(HOST, PORT, WebSocketHandler)
    print()
    print("Starting websocket server on port {HOST}:{PORT}")
    print()
    print()
    print("Press Ctrl-C to quit.")
    server.serve_forever()
