# Hello World MCP Server

This is a Model Context Protocol (MCP) server implementation that provides Hello World functionality to Cursor. The server exposes Hello World commands that can be used directly within the Cursor editor.

## Project Structure

```
.
├── README.md
├── mcp_hello_world.py
├── cursor_integration.py
└── mcp_server.py
```

## Features

- MCP server implementation for Cursor integration
- Two commands:
  - `hello_world`: Displays a simple Hello World message
  - `hello_world_with_name`: Displays Hello World with a given name
- Dynamic port allocation for easy setup
- Full MCP protocol support

## Setting Up the MCP Server

1. Start the MCP server:
```bash
python mcp_server.py
```

2. The server will start and display its URL, for example:
```
Starting Hello World MCP Server on localhost:12345
To add this server to Cursor:
1. Click '+ Add new MCP server' in Cursor
2. Enter the URL: http://localhost:12345
```

3. In Cursor:
   - Click the "+ Add new MCP server" button
   - Enter the URL displayed by the server
   - The Hello World commands will now be available in Cursor

## Available Commands

### 1. hello_world
- Description: Display a simple Hello World message
- Parameters: None
- Example output: "Hello World!"

### 2. hello_world_with_name
- Description: Display Hello World with a given name
- Parameters:
  - name (string): Name to include in greeting
- Example output: "Hello World, Alice!"

## Implementation Details

### MCP Server (mcp_server.py)
- Implements the MCP protocol endpoints:
  - `/capabilities`: Returns available commands
  - `/execute`: Executes requested commands
- Uses HTTP/JSON for communication
- Automatic port assignment for easy deployment

### Model Implementation (mcp_hello_world.py)
- Implements the core Hello World functionality
- Maintains context and state
- Provides clean API for text generation

## Requirements

- Python 3.6+
- No additional dependencies required

## Development

To modify or extend the MCP server:

1. Update the commands list in `MCPRequestHandler`
2. Add new command handlers in the `/execute` endpoint
3. Implement new functionality in the model
4. Test the changes in Cursor

## Error Handling

The server includes proper error handling for:
- Invalid commands
- Missing parameters
- Invalid endpoints
- Connection issues

## Best Practices

1. Always start the server before adding it to Cursor
2. Use the dynamic port allocation for development
3. Test new commands in Cursor before deployment
4. Monitor server output for potential issues