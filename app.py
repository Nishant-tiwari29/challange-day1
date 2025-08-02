from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    """Serve the main HTML page"""
    return render_template('index.html')

@app.route('/api/hello')
def hello():
    """Simple API endpoint"""
    return jsonify({'message': 'Hello from Flask backend!'})

@app.route('/api/data')
def get_data():
    """API endpoint that returns some sample data"""
    return jsonify({
        'items': [
            {'id': 1, 'name': 'Item 1', 'description': 'First item'},
            {'id': 2, 'name': 'Item 2', 'description': 'Second item'},
            {'id': 3, 'name': 'Item 3', 'description': 'Third item'}
        ]
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 