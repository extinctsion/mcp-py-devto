# MCP Python Dev.to Integration

A Message Control Program (MCP) server implementation in Python that integrates with dev.to platform. This project allows you to interact with dev.to's API through a message-based architecture.

## Features

- RESTful API integration with dev.to
- Message queuing and routing
- Real-time content updates
- Article management capabilities

## Prerequisites

- Python 3.11 or higher
- pip (Python package manager)
- dev.to API key
- Latest Visual Studio Code

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/mcp-py-devto.git
   cd mcp-py-devto
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Unix or MacOS:
   source venv/bin/activate
   ```

3. Install required dependencies:
    cd to the `pyproject.toml` directory and write in terminal - 
   ```bash
   pip install .
   ```

## Configuration

1. Go to `.vscode/mcp.json` file and insert your dev.to API key

   ```json
   DEVTO_API_KEY=your_api_key_here
   ```

2. Get your dev.to API key from [dev.to/settings/account](https://dev.to/settings/account)

## Usage

1. Start the MCP server:
   - Go to `.vscode/mcp.json` and press on the start button.

2. The server will start listening on the configured port (default: 8080)

3. Send messages to the server using the provided client libraries or API endpoints:

   ```python
   from mcp_client import MCPClient

   client = MCPClient()
   response = client.send_message({
       "action": "create_article",
       "data": {
           "title": "My New Article",
           "content": "Article content here"
       }
   })
   ```

## API Documentation

### Available Endpoints

- `POST /message` - Send a message to the MCP server
- `GET /status` - Check server status
- `GET /metrics` - View server metrics

### Message Types

- `create_article`
- `update_article`
- `delete_article`
- `get_article`

## Development

To contribute to the project:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## Testing

Run the test suite:

```bash
pytest tests/
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md) for details on how to submit pull requests.

## Support

For support, please open an issue in the GitHub repository or contact the maintainers.
