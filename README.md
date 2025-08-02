# Flask Backend Demo

A simple Flask web application that demonstrates a Python backend serving HTML pages and providing API endpoints.

## Features

- **Flask Backend**: Python web framework with RESTful API endpoints
- **Modern Frontend**: Responsive HTML/CSS/JavaScript interface
- **API Endpoints**: 
  - `/api/hello` - Simple greeting endpoint
  - `/api/data` - Returns sample data
- **Interactive UI**: Test API calls directly from the browser
- **Keyboard Shortcuts**: Quick access to API testing

## Project Structure

```
├── app.py              # Main Flask application
├── templates/
│   └── index.html      # Main HTML template
├── static/
│   └── script.js       # Frontend JavaScript
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Setup Instructions

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Application

```bash
python app.py
```

The application will start on `http://localhost:5000`

### 3. Access the Application

Open your web browser and navigate to:
- **Main Page**: http://localhost:5000
- **Hello API**: http://localhost:5000/api/hello
- **Data API**: http://localhost:5000/api/data

## Usage

### Web Interface

1. Open http://localhost:5000 in your browser
2. Click the buttons to test different API endpoints:
   - **Test Hello API**: Calls the `/api/hello` endpoint
   - **Test Data API**: Calls the `/api/data` endpoint
   - **Clear Responses**: Removes all displayed responses

### Keyboard Shortcuts

- `Ctrl/Cmd + 1`: Test Hello API
- `Ctrl/Cmd + 2`: Test Data API
- `Ctrl/Cmd + C`: Clear all responses

### API Endpoints

#### GET /api/hello
Returns a simple greeting message.

**Response:**
```json
{
  "message": "Hello from Flask backend!"
}
```

#### GET /api/data
Returns sample data items.

**Response:**
```json
{
  "items": [
    {
      "id": 1,
      "name": "Item 1",
      "description": "First item"
    },
    {
      "id": 2,
      "name": "Item 2",
      "description": "Second item"
    },
    {
      "id": 3,
      "name": "Item 3",
      "description": "Third item"
    }
  ]
}
```

## Development

### Adding New API Endpoints

1. Add a new route in `app.py`:
```python
@app.route('/api/new-endpoint')
def new_endpoint():
    return jsonify({'data': 'your data here'})
```

2. Add a corresponding JavaScript function in `static/script.js`:
```javascript
async function testNewAPI() {
    const response = await fetch('/api/new-endpoint');
    const data = await response.json();
    addResponse('New API Response', data);
}
```

3. Add a button in `templates/index.html`:
```html
<button class="button" onclick="testNewAPI()">Test New API</button>
```

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Styling**: Custom CSS with modern design
- **API**: RESTful JSON endpoints

## Requirements

- Python 3.7+
- Flask 2.3.3
- Modern web browser with JavaScript enabled

## Troubleshooting

### Port Already in Use
If port 5000 is already in use, modify the port in `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5001)  # Change to different port
```

### Module Not Found
Ensure you've installed the requirements:
```bash
pip install -r requirements.txt
```

### Browser Issues
- Ensure JavaScript is enabled
- Try refreshing the page
- Check browser console for any errors 