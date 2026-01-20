#!/usr/bin/env python3
"""
Enkel HTTP-server for å kjøre kart-nettsiden lokalt.
Kjør denne filen og åpne http://localhost:5001/index.html i nettleseren.
"""

import http.server
import socketserver
import os

# Port for serveren
PORT = 5001

# Mappe hvor filene ligger
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

# Kjør serveren
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Server kjører på http://localhost:{PORT}")
    print("Åpne http://localhost:5001/index.html i nettleseren din.")
    httpd.serve_forever()