#!/usr/bin/env python3
"""
Simple HTTP Server for Face Music App
Run this to start the local development server
"""

import http.server
import socketserver
import os
import webbrowser
from pathlib import Path

PORT = 8000
DIRECTORY = Path(__file__).parent

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(DIRECTORY), **kwargs)
    
    def log_message(self, format, *args):
        print(f"[Server] {format % args}")

def run_server():
    os.chdir(DIRECTORY)
    
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        url = f"http://localhost:{PORT}"
        print("\n" + "="*60)
        print("🎵 Face Music App - Local Server")
        print("="*60)
        print(f"✅ Server running at: {url}")
        print(f"📁 Serving files from: {DIRECTORY}")
        print(f"🔴 Press Ctrl+C to stop the server")
        print("="*60 + "\n")
        
        # Open browser automatically
        try:
            webbrowser.open(url)
            print("🌐 Browser opened automatically\n")
        except:
            print("⚠️  Could not open browser automatically. Visit manually if needed.\n")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n🛑 Server stopped by user")

if __name__ == "__main__":
    run_server()
