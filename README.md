# Flask API Server

A basic Flask server hosting a website with a REST API.

## Features

- RESTful API with CRUD operations
- In-memory data storage for items
- Clean web interface
- Health check endpoint
- JSON request/response format

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Server

Start the Flask server:
```bash
python app.py
```

The server will run on `http://localhost:5000`

### Development Mode

For development purposes, you can enable debug mode (NOT recommended for production):
```bash
FLASK_DEBUG=true python app.py
```

**Security Note:** Debug mode should never be enabled in production as it allows arbitrary code execution through the debugger.

## API Endpoints

### Health Check
- **GET** `/api/health` - Check if the server is running

### Items Management
- **GET** `/api/items` - Get all items
- **GET** `/api/items/<id>` - Get a specific item by ID
- **POST** `/api/items` - Add a new item (requires JSON body with "name" field)
- **DELETE** `/api/items/<id>` - Delete an item by ID

## Example API Usage

### Add an item:
```bash
curl -X POST http://localhost:5000/api/items \
  -H "Content-Type: application/json" \
  -d '{"name": "Example Item", "description": "This is a test item"}'
```

### Get all items:
```bash
curl http://localhost:5000/api/items
```

### Health check:
```bash
curl http://localhost:5000/api/health
```

## Web Interface

Visit `http://localhost:5000` in your browser to see the web interface with API documentation.
