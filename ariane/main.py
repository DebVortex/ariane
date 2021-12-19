"""Top-level package for Ariane."""

__author__ = """Max Brauer"""
__email__ = 'max@max-brauer.de'
__version__ = '0.1.0'



from ariane import WebSocketHandler
from simple_websocket_server import WebSocketServer


if __name__ == '__main__':
    server = WebSocketServer('', 8000, WebSocketHandler)
    server.serve_forever()
