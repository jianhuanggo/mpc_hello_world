from typing import Dict, Any, List
import json
import http.server
import socketserver
from mcp_hello_world import HelloWorldModel

class MCPRequestHandler(http.server.BaseHTTPRequestHandler):
    def _send_response(self, data: Dict[str, Any], status: int = 200):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        request = json.loads(post_data.decode('utf-8'))

        if self.path == '/capabilities':
            # Return the server's capabilities
            response = {
                "name": "Hello World MCP",
                "version": "1.0.0",
                "description": "A simple Hello World MCP server",
                "commands": [
                    {
                        "name": "hello_world",
                        "description": "Display Hello World message",
                        "parameters": []
                    },
                    {
                        "name": "hello_world_with_name",
                        "description": "Display Hello World with name",
                        "parameters": [
                            {
                                "name": "name",
                                "type": "string",
                                "description": "Name to include in greeting"
                            }
                        ]
                    }
                ]
            }
            self._send_response(response)
            
        elif self.path == '/execute':
            command = request.get('command')
            params = request.get('parameters', {})
            model = HelloWorldModel()
            
            if command == 'hello_world':
                result = model.display_hello_world()
                self._send_response({"result": result})
            
            elif command == 'hello_world_with_name':
                name = params.get('name', '')
                result = model.display_hello_world_with_name(name)
                self._send_response({"result": result})
            
            else:
                self._send_response(
                    {"error": "Unknown command"},
                    status=400
                )
        else:
            self._send_response(
                {"error": "Invalid endpoint"},
                status=404
            )

class MCPServer:
    def __init__(self, host: str = 'localhost', port: int = 0):
        """Initialize MCP server with host and port.
        Using port 0 lets the OS assign an available port."""
        self.host = host
        self.server = socketserver.TCPServer((host, port), MCPRequestHandler)
        # Get the actual port assigned by the OS
        self.port = self.server.server_address[1]

    def start(self):
        """Start the MCP server"""
        print(f"Starting Hello World MCP Server on {self.host}:{self.port}")
        print("To add this server to Cursor:")
        print(f"1. Click '+ Add new MCP server' in Cursor")
        print(f"2. Enter the URL: http://{self.host}:{self.port}")
        self.server.serve_forever()

def main():
    # Start the server on localhost with a dynamic port
    server = MCPServer()
    server.start()

if __name__ == "__main__":
    main() 