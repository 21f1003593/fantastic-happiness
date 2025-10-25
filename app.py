from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# In-memory data store for demo purposes
data_store = []

@app.route('/')
def home():
    """Home page with website interface"""
    return render_template('index.html')

@app.route('/api/items', methods=['GET'])
def get_items():
    """API endpoint to get all items"""
    return jsonify({'items': data_store, 'count': len(data_store)}), 200

@app.route('/api/items', methods=['POST'])
def add_item():
    """API endpoint to add a new item"""
    if not request.json or 'name' not in request.json:
        return jsonify({'error': 'Bad request - name is required'}), 400
    
    item = {
        'id': len(data_store) + 1,
        'name': request.json['name'],
        'description': request.json.get('description', '')
    }
    data_store.append(item)
    return jsonify({'message': 'Item added successfully', 'item': item}), 201

@app.route('/api/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    """API endpoint to get a specific item by ID"""
    item = next((item for item in data_store if item['id'] == item_id), None)
    if item is None:
        return jsonify({'error': 'Item not found'}), 404
    return jsonify(item), 200

@app.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    """API endpoint to delete a specific item by ID"""
    global data_store
    initial_length = len(data_store)
    data_store = [item for item in data_store if item['id'] != item_id]
    
    if len(data_store) == initial_length:
        return jsonify({'error': 'Item not found'}), 404
    
    return jsonify({'message': 'Item deleted successfully'}), 200

@app.route('/api/health', methods=['GET'])
def health_check():
    """API endpoint for health check"""
    return jsonify({'status': 'healthy', 'service': 'Flask API Server'}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
